import os
import sys

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

# PythonAnywhere deployment instructions
"""
1. Domain Configuration (saskatoongaragedoorexpets.ca):
   - Log in to PythonAnywhere dashboard
   - Go to Web tab
   - Add new web app
   - Choose manual configuration (Python)
   - Set Python version to 3.11
   - Configure WSGI file path: /var/www/yourusername_pythonanywhere_com_wsgi.py
   - Set working directory to your project directory
   - Add domain name in the Web tab

2. Static Files:
   - In Web tab, add static file mapping:
     URL: /static/
     Directory: /home/yourusername/saskatoon-garage-door-experts/static/

3. HTTPS/SSL:
   - Enable HTTPS by clicking "Enable HTTPS" in Web tab
   - PythonAnywhere provides free SSL certificates

4. Environment Variables:
   - Add the following in the Web tab's "Environment variables" section:
     - FLASK_SECRET_KEY
     - MAIL_USERNAME
     - MAIL_PASSWORD
     - DATABASE_URL
     - PGHOST
     - PGPORT
     - PGUSER
     - PGPASSWORD
     - PGDATABASE

5. Database:
   - Use the provided PostgreSQL database URL
   - Ensure all tables are created using Flask-SQLAlchemy

6. Files to Upload:
   - All Python files (*.py)
   - Requirements file (requirements.txt)
   - Templates directory
   - Static directory
   - Log directory (create if not exists)

7. Final Steps:
   - Install requirements: pip install -r requirements.txt
   - Reload web app
   - Check error logs in /var/log/
"""

if __name__ == '__main__':
    application.run()
