import os
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit

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
db.init_app(app)
socketio = SocketIO(app)

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
            db.session.add(new_inquiry)
            db.session.commit()
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
