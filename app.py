import os
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit
from flask_mail import Mail, Message
from flask_talisman import Talisman

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# Production configurations
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "saskatoon-garage-experts"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Security configurations
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PREFERRED_URL_SCHEME'] = 'https'

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

db.init_app(app)
socketio = SocketIO(app)
mail = Mail(app)

# Initialize Talisman with security configurations for custom domain
talisman = Talisman(
    app,
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    content_security_policy={
        'default-src': ["'self'"],
        'img-src': ["'self'", 'data:', 'https:', '*'],
        'script-src': ["'self'", "'unsafe-inline'", 'https://cdn.jsdelivr.net', 'https://unpkg.com'],
        'style-src': ["'self'", "'unsafe-inline'", 'https://cdn.replit.com'],
        'connect-src': ["'self'", 'wss:', 'https:', '*'],
        'font-src': ["'self'", 'data:'],
        'frame-ancestors': ["'none'"],
        'upgrade-insecure-requests': []
    }
)

# Domain configuration middleware
@app.before_request
def redirect_to_domain():
    if request.headers.get('X-Forwarded-Proto', 'http') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

    host = request.host.lower()
    target_domain = 'saskatoongaragedoorexperts.ca'
    
    # Skip redirect for development environment
    if 'replit' in host or 'localhost' in host:
        return None
        
    if host != target_domain and host != f'www.{target_domain}':
        return redirect(f'https://{target_domain}{request.full_path}', code=301)
    return None

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/faq')
def faq():
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

            flash('Thank you for your inquiry! We will contact you soon.', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
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
        print(f"Error sending email: {e}")
    
    # Simulate support response after customer message
    support_response = "Thank you for your message. Our support team will be with you shortly. You can also reach us via SMS at (474) 774-0269 or send us an email."
    emit('receive_message', {'message': support_response, 'is_support': True}, broadcast=True)

with app.app_context():
    import models
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
