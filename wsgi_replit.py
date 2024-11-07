import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from flask import request, redirect

# Add the application directory to the Python path
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

# Import the Flask application
from app import app as application

# Configure production settings
application.config.update(
    ENV='production',
    DEBUG=False,
    PREFERRED_URL_SCHEME='https'
)

# Configure logging
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler(
    'logs/saskatoon_garage.log',
    maxBytes=10240,
    backupCount=10
)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
application.logger.addHandler(file_handler)
application.logger.setLevel(logging.INFO)
application.logger.info('Saskatoon Garage Door Experts startup')

# Add security headers
@application.after_request
def add_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Cache control for static files
    if request.path.startswith('/static/'):
        response.cache_control.max_age = 2592000  # 30 days
        response.cache_control.public = True
        response.headers['Vary'] = 'Accept-Encoding'
    
    return response

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
