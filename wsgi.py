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
    PREFERRED_URL_SCHEME='https'
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

# Add HSTS header
@application.after_request
def add_security_headers(response):
    if application.config['STRICT_TRANSPORT_SECURITY']:
        hsts_header = 'max-age={}'.format(application.config['STRICT_TRANSPORT_SECURITY_MAX_AGE'])
        if application.config['STRICT_TRANSPORT_SECURITY_INCLUDE_SUBDOMAINS']:
            hsts_header += '; includeSubDomains'
        if application.config['STRICT_TRANSPORT_SECURITY_PRELOAD']:
            hsts_header += '; preload'
        response.headers['Strict-Transport-Security'] = hsts_header

    # Add CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = ', '.join(application.config['CORS_HEADERS'])
    
    # Cache control for static files
    if request.path.startswith('/static/'):
        response.cache_control.max_age = application.config['STATIC_CACHE_TIMEOUT']
        response.cache_control.public = True
    
    return response

# HTTPS and WWW redirect
@application.before_request
def before_request():
    # Redirect HTTP to HTTPS
    if not application.debug and not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

    # Redirect non-www to www
    if (application.config.get('FORCE_WWW') and 
        request.host.startswith('saskatoongaragedoorexpets.ca') and 
        not request.host.startswith('www.')):
        url = request.url.replace('://', '://www.', 1)
        return redirect(url, code=301)

if __name__ == '__main__':
    application.run()
