from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    Our base database model class.
    This sets up the foundation for all our database models.
    """
    pass

# Create our database interface
# We'll use this to interact with our PostgreSQL database
db = SQLAlchemy(model_class=Base)
