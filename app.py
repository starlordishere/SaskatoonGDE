import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit
from flask_mail import Mail, Message

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# Enhanced security configurations
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "saskatoon-garage-experts"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Configure database with SSL
database_url = os.environ.get("DATABASE_URL")
if database_url and database_url.startswith("postgresql://"):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
        "connect_args": {
            "sslmode": "require"
        }
    }
    logger.info("PostgreSQL database configured with SSL")
else:
    logger.warning("DATABASE_URL not properly configured")

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

# Initialize extensions
logger.info("Initializing database connection...")
db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
mail = Mail(app)

@app.before_request
def before_request():
    # Log each request for debugging
    logger.info(f"Incoming request: {request.method} {request.path}")
    # Remove HTTPS redirect since Replit handles HTTPS automatically
    return None

@app.after_request
def after_request(response):
    # Add security headers
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('index.html')

@app.route('/services')
def services():
    logger.info("Serving services page")
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    logger.info("Serving gallery page")
    return render_template('gallery.html')

@app.route('/faq')
def faq():
    logger.info("Serving FAQ page")
    return render_template('faq.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    from models import ContactInquiry
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        service_type = request.form.get('service_type')
        
        new_inquiry = ContactInquiry(
            name=name,
            email=email,
            phone=phone,
            message=message,
            service_type=service_type,
            created_at=datetime.utcnow()
        )
        
        try:
            # Save to database
            db.session.add(new_inquiry)
            db.session.commit()
            logger.info(f"New contact inquiry saved from {email}")

            # Send email notification
            msg = Message(
                'New Contact Form Submission',
                recipients=[app.config['MAIL_USERNAME']]
            )
            msg.body = f"""
New contact form submission received:

Name: {name}
Email: {email}
Phone: {phone}
Service Type: {service_type}
Message:
{message}

Submitted at: {datetime.utcnow()}
"""
            mail.send(msg)
            logger.info("Admin notification email sent")

            # Send confirmation email to customer
            customer_msg = Message(
                'Thank you for contacting Saskatoon Garage Door Experts',
                recipients=[email]
            )
            customer_msg.body = f"""
Dear {name},

Thank you for contacting Saskatoon Garage Door Experts. We have received your inquiry about {service_type} service.

We will review your request and get back to you shortly.

Your message:
{message}

Best regards,
Saskatoon Garage Door Experts Team
"""
            mail.send(customer_msg)
            logger.info("Customer confirmation email sent")

            flash('Thank you for your inquiry! We will contact you soon.', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            logger.error(f"Error processing contact form: {str(e)}")
            flash('An error occurred. Please try again.', 'error')
            
    return render_template('contact.html')

@app.route('/blog')
def blog():
    from models import BlogPost
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('blog/index.html', posts=posts)

@app.route('/blog/<string:slug>')
def blog_post(slug):
    from models import BlogPost
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/post.html', post=post)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('send_message')
def handle_message(data):
    # Log incoming chat messages
    logger.info("Received chat message")
    
    # Emit the message to all connected clients
    emit('receive_message', {'message': data['message'], 'is_support': False}, broadcast=True)
    
    # Forward the chat message to support email
    try:
        msg = Message(
            'New Chat Message',
            recipients=[app.config['MAIL_USERNAME']]
        )
        msg.body = f"""
New chat message received:

Message: {data['message']}
Time: {datetime.utcnow()}

This message was sent through the live chat system.
"""
        mail.send(msg)
    except Exception as e:
        logger.error(f"Error sending chat email: {str(e)}")
    
    # Simulate support response after customer message
    support_response = "Thank you for your message. Our support team will be with you shortly. You can also reach us via WhatsApp at (474) 774-0269 or send us an SMS."
    emit('receive_message', {'message': support_response, 'is_support': True}, broadcast=True)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

with app.app_context():
    try:
        import models
        logger.info("Creating database tables...")
        db.create_all()
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting application on port {port}")
    socketio.run(app, host='0.0.0.0', port=port, debug=False)
