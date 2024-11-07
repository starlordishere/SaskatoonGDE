from flask_migrate import Migrate
from app import app, db

# Initialize Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        # Import models to ensure they're known to Flask-Migrate
        import models
        
        # Create initial migration
        from flask_migrate import upgrade, migrate
        migrate()
        upgrade()
