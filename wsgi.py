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

# Ensure all production configurations are set
application.config.update(
    ENV='production',
    DEBUG=False,
    PREFERRED_URL_SCHEME='https',
    SERVER_NAME='saskatoongaragedoorexpets.ca',
    SQLALCHEMY_ENGINE_OPTIONS={
        'pool_size': 10,
        'pool_recycle': 300,
        'pool_pre_ping': True,
        'max_overflow': 5,
        'connect_args': {
            'sslmode': 'require'
        }
    }
)

# Configure logging for production
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

# Add HSTS and security headers
@application.after_request
def add_security_headers(response):
    # HSTS header
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    
    # Security headers
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Cache control for static files
    if request.path.startswith('/static/'):
        response.cache_control.max_age = 2592000  # 30 days
        response.cache_control.public = True
        response.headers['Vary'] = 'Accept-Encoding'
    
    return response

# HTTPS and WWW redirect
@application.before_request
def before_request():
    # Redirect HTTP to HTTPS
    if not application.debug and not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

    # Redirect non-www to www
    if (request.host.startswith('saskatoongaragedoorexpets.ca') and 
        not request.host.startswith('www.')):
        url = request.url.replace('://', '://www.', 1)
        return redirect(url, code=301)

if __name__ == '__main__':
    application.run()
