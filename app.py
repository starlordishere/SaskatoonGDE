import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_mail import Mail, Message
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from tenacity import retry, stop_after_attempt, wait_exponential
import bleach
from flask_wtf.csrf import CSRFProtect
import re
import json
from pathlib import Path
from flask_socketio import SocketIO

# Hey there! Let's set up logging to keep track of what's happening in our app
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Let's configure our app with all the settings it needs
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "saskatoon-garage-experts")


# Initialize Socket.IO
socketio = SocketIO(app)

# Email configuration - we're using Gmail SMTP for sending emails
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Standard TLS port for Gmail
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_MAX_EMAILS'] = 10
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.config['WTF_CSRF_ENABLED'] = True

# Initialize our protective shields (security features)
csrf = CSRFProtect(app)
mail = Mail(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Create data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)
contact_file = data_dir / 'contact_inquiries.json'
blog_file = data_dir / 'blog_posts.json'

def load_blog_posts():
    """Load blog posts from JSON file and convert date strings to datetime objects"""
    if blog_file.exists():
        with open(blog_file, 'r') as f:
            posts = json.load(f)
            # Convert string dates to datetime objects
            for post in posts:
                post['created_at'] = datetime.fromisoformat(post['created_at'])
                post['updated_at'] = datetime.fromisoformat(post['updated_at'])
            return posts
    return []

def sanitize_input(text):
    """Keep our app safe by cleaning user input to prevent XSS attacks"""
    return bleach.clean(text, strip=True)

def validate_phone(phone):
    """Make sure phone numbers are exactly 10 digits"""
    digits_only = ''.join(filter(str.isdigit, phone))
    return len(digits_only) == 10

def validate_email(email):
    """Check if an email looks legitimate"""
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_pattern.match(email))

def validate_email_template(msg):
    """Double-check our email messages before sending them out"""
    if not msg.subject:
        raise ValueError("Email subject cannot be empty")
    if not msg.recipients:
        raise ValueError("Email must have at least one recipient")
    if not msg.body and not msg.html:
        raise ValueError("Email must have either body or HTML content")
    return True

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def send_email_with_retry(msg):
    """Send emails with a retry mechanism in case of temporary failures"""
    try:
        validate_email_template(msg)
        with app.app_context():
            mail.send(msg)
            logger.info(f"Email sent successfully to {msg.recipients}")
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        if "Username and Password not accepted" in str(e):
            logger.error("Authentication failed. Please check your Gmail credentials.")
        raise

@app.route('/')
def index():
    """Our homepage - the first thing visitors see"""
    return render_template('index.html')

@app.route('/services')
def services():
    """Show our available garage door services"""
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    """Display our work portfolio"""
    return render_template('gallery.html')

@app.route('/blog')
def blog():
    """Show our blog posts about garage door maintenance and tips"""
    posts = load_blog_posts()
    return render_template('blog/index.html', posts=posts)

@app.route('/blog/<string:slug>')
def blog_post(slug):
    """Display a specific blog post"""
    posts = load_blog_posts()
    post = next((post for post in posts if post['slug'] == slug), None)
    if post is None:
        return render_template('404.html'), 404
    return render_template('blog/post.html', post=post)

@app.route('/faq')
def faq():
    """Answer common questions about our services"""
    return render_template('faq.html')

@app.route('/contact', methods=['GET', 'POST'])
@limiter.limit("10 per hour")
def contact():
    """Handle contact form submissions and inquiries"""
    if request.method == 'POST':
        try:
            # Clean and validate all the form inputs
            name = sanitize_input(request.form.get('name', ''))
            email = sanitize_input(request.form.get('email', ''))
            phone = sanitize_input(request.form.get('phone', ''))
            message = sanitize_input(request.form.get('message', ''))
            service_type = sanitize_input(request.form.get('service_type', ''))

            # Make sure we have all required information
            if not all([name, email, phone, message, service_type]):
                logger.warning(f"Invalid form submission from {request.remote_addr}: Missing required fields")
                flash('All fields are required.', 'danger')
                return redirect(url_for('contact'))

            # Verify email format
            if not validate_email(email):
                logger.warning(f"Invalid email format from {request.remote_addr}: {email}")
                flash('Please enter a valid email address.', 'danger')
                return redirect(url_for('contact'))

            # Check phone number format
            if not validate_phone(phone):
                logger.warning(f"Invalid phone format from {request.remote_addr}: {phone}")
                flash('Please enter exactly 10 digits for the phone number.', 'danger')
                return redirect(url_for('contact'))

            # Save inquiry to file
            inquiry = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
                'service_type': service_type,
                'created_at': datetime.utcnow().isoformat()
            }

            inquiries = []
            if contact_file.exists():
                with open(contact_file, 'r') as f:
                    inquiries = json.load(f)
            
            inquiries.append(inquiry)
            
            with open(contact_file, 'w') as f:
                json.dump(inquiries, f, indent=2)

            # Prepare email for our team
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

            # Prepare confirmation email for the customer
            customer_msg = Message(
                'Thank you for contacting Saskatoon Garage Door Experts',
                recipients=[email]
            )
            customer_msg.body = f"""
Dear {name},

Thank you for contacting Saskatoon Garage Door Experts. We have received your inquiry about {service_type} service.

We will review your request and get back to you shortly. All our services include a comprehensive 1-year warranty on parts and labor.

Your message:
{message}

Best regards,
Saskatoon Garage Door Experts Team
"""

            try:
                # Send both emails
                send_email_with_retry(admin_msg)
                send_email_with_retry(customer_msg)
                flash('Thank you for your inquiry! We will contact you soon.', 'success')
            except Exception as e:
                logger.error(f"Error sending email: {str(e)}")
                flash('An error occurred while processing your request. Please try again.', 'danger')

            return redirect(url_for('contact'))

        except Exception as e:
            logger.error(f"Error processing contact form: {str(e)}")
            flash('An error occurred. Please try again.', 'danger')
            return redirect(url_for('contact'))
            
    return render_template('contact.html')
