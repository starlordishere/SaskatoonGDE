import os
from datetime import timedelta

class Config:
    # Base configuration
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'saskatoon-garage-experts'
    STATIC_FOLDER = 'static'
    STATIC_URL_PATH = '/static'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

    # Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = timedelta(days=31)
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_recycle": 300,
        "pool_pre_ping": True,
        "max_overflow": 5
    }

    # Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
    MAIL_MAX_EMAILS = None
    MAIL_ASCII_ATTACHMENTS = False

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    PREFERRED_URL_SCHEME = 'https'
    SERVER_NAME = 'saskatoongaragedoorexpets.ca'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
