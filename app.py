import os
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit
from flask_mail import Mail, Message

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "saskatoon-garage-experts"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

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
    
    # Simulate support response after customer message
    support_response = "Thank you for your message. Our support team will be with you shortly."
    emit('receive_message', {'message': support_response, 'is_support': True}, broadcast=True)

with app.app_context():
    import models
    db.create_all()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
