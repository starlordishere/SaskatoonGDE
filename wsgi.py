import os
import sys
import logging
from logging.handlers import RotatingFileHandler

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

# HTTPS redirect
@application.before_request
def before_request():
    if not application.debug and not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

if __name__ == '__main__':
    application.run()
