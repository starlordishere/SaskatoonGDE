import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from tenacity import retry, stop_after_attempt, wait_exponential
import bleach
from database import db
import sqlalchemy.exc

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enhanced security configurations
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "saskatoon-garage-experts"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_TIME_LIMIT'] = 3600

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize rate limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

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
app.config['MAIL_MAX_EMAILS'] = 10
app.config['MAIL_RETRY_ATTEMPTS'] = 3

# Initialize extensions
logger.info("Initializing database connection...")
db.init_app(app)
mail = Mail(app)

def sanitize_input(text):
    """Sanitize user input to prevent XSS attacks"""
    return bleach.clean(text, strip=True)

def validate_phone(phone):
    """Validate phone number format"""
    import re
    phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
    return bool(phone_pattern.match(phone))

def validate_email(email):
    """Validate email format"""
    import re
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_pattern.match(email))

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def send_email_with_retry(msg):
    """Send email with retry mechanism"""
    try:
        mail.send(msg)
        logger.info(f"Email sent successfully to {msg.recipients}")
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        raise

@app.before_request
def before_request():
    # Log each request for debugging
    logger.info(f"Incoming request: {request.method} {request.path} from {request.remote_addr}")
    return None

@app.after_request
def after_request(response):
    # Add security headers
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' cdn.jsdelivr.net unpkg.com; style-src 'self' 'unsafe-inline' cdn.replit.com; img-src 'self' data: placehold.co"
    return response

# Existing routes remain unchanged
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
@limiter.limit("10 per hour")
def contact():
    from models import ContactInquiry
    
    if request.method == 'POST':
        try:
            # Sanitize and validate input
            name = sanitize_input(request.form.get('name', ''))
            email = sanitize_input(request.form.get('email', ''))
            phone = sanitize_input(request.form.get('phone', ''))
            message = sanitize_input(request.form.get('message', ''))
            service_type = sanitize_input(request.form.get('service_type', ''))

            # Input validation
            if not all([name, email, phone, message, service_type]):
                logger.warning(f"Invalid form submission from {request.remote_addr}: Missing required fields")
                flash('All fields are required.', 'danger')
                return redirect(url_for('contact'))

            if not validate_email(email):
                logger.warning(f"Invalid email format from {request.remote_addr}: {email}")
                flash('Please enter a valid email address.', 'danger')
                return redirect(url_for('contact'))

            if not validate_phone(phone):
                logger.warning(f"Invalid phone format from {request.remote_addr}: {phone}")
                flash('Please enter a valid phone number.', 'danger')
                return redirect(url_for('contact'))

            # Create new inquiry
            new_inquiry = ContactInquiry(
                name=name,
                email=email,
                phone=phone,
                message=message,
                service_type=service_type,
                created_at=datetime.utcnow()
            )

            # Database transaction
            try:
                db.session.begin_nested()
                db.session.add(new_inquiry)
                db.session.commit()
                logger.info(f"New contact inquiry saved from {email}")

                # Prepare admin notification email
                admin_msg = Message(
                    'New Contact Form Submission',
                    recipients=[app.config['MAIL_USERNAME']]
                )
                admin_msg.body = f"""
New contact form submission received:

Name: {name}
Email: {email}
Phone: {phone}
Service Type: {service_type}
Message:
{message}

Submitted at: {datetime.utcnow()}
"""
                # Send admin notification with retry
                send_email_with_retry(admin_msg)

                # Prepare customer confirmation email
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
                # Send customer confirmation with retry
                send_email_with_retry(customer_msg)

                flash('Thank you for your inquiry! We will contact you soon.', 'success')
                return redirect(url_for('contact'))

            except sqlalchemy.exc.SQLAlchemyError as e:
                db.session.rollback()
                logger.error(f"Database error processing contact form: {str(e)}")
                flash('An error occurred while processing your request. Please try again.', 'danger')
                return redirect(url_for('contact'))

        except Exception as e:
            logger.error(f"Error processing contact form: {str(e)}")
            flash('An error occurred. Please try again.', 'danger')
            return redirect(url_for('contact'))
            
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

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(429)
def ratelimit_handler(e):
    logger.warning(f"Rate limit exceeded for IP: {request.remote_addr}")
    return render_template('429.html', message=str(e.description)), 429

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    logger.error(f"Internal server error: {str(error)}")
    return render_template('500.html'), 500

# Initialize database tables
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
    app.run(host='0.0.0.0', port=port, debug=False)
