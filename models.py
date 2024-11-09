from datetime import datetime
from database import db

class ContactInquiry(db.Model):
    """
    Store and manage customer inquiries from the contact form.
    This helps us keep track of all customer communications.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Customer's name
    email = db.Column(db.String(120), nullable=False)  # Contact email
    phone = db.Column(db.String(20), nullable=False)   # Phone number in (XXX) XXX-XXXX format
    message = db.Column(db.Text, nullable=False)       # Customer's inquiry or message
    service_type = db.Column(db.String(50), nullable=False)  # Type of service requested
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # When the inquiry was made

class BlogPost(db.Model):
    """
    Manage our blog posts about garage door maintenance and tips.
    This helps us share knowledge and build trust with customers.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)  # Post title
    slug = db.Column(db.String(200), unique=True, nullable=False)  # URL-friendly title
    content = db.Column(db.Text, nullable=False)  # Main content in HTML format
    summary = db.Column(db.String(300), nullable=False)  # Short preview text
    image_url = db.Column(db.String(200))  # Optional featured image
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # When post was created
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Last update time
