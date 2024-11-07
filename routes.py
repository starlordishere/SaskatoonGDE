from datetime import datetime
from flask import render_template, request, flash, redirect, url_for, abort
from app import app, db, mail, socketio
from flask_mail import Message
from flask_socketio import emit
from models import ContactInquiry, BlogPost

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
            app.logger.error(f"Error processing contact form: {str(e)}")
            flash('An error occurred. Please try again.', 'error')
            
    return render_template('contact.html')

@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('blog/index.html', posts=posts)

@app.route('/blog/<string:slug>')
def blog_post(slug):
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
        app.logger.error(f"Error sending chat email: {str(e)}")
    
    # Simulate support response after customer message
    support_response = "Thank you for your message. Our support team will be with you shortly. You can also reach us via SMS at (474) 774-0269 or send us an email."
    emit('receive_message', {'message': support_response, 'is_support': True}, broadcast=True)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
