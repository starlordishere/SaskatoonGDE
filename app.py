import os
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, emit
from flask_mail import Mail, Message
import logging
from logging.handlers import RotatingFileHandler
from config import config

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
mail = Mail()

def create_app(config_name='production'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    
    # Configure logging for production
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/saskatoon_garage.log', 
                                         maxBytes=10240, 
                                         backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Saskatoon Garage Door Experts startup')
    
    return app

# Create app instance
app = create_app(os.getenv('FLASK_ENV', 'production'))
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins='*')

# Import routes after app creation to avoid circular imports
from routes import *

with app.app_context():
    import models
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
