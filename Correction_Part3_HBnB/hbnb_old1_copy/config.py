import os
from datetime import timedelta

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Durée de validité des tokens
    CORS_HEADERS = "Content-Type"
    API_TITLE = "HBnB API"
    API_VERSION = "v1"
    SWAGGER_UI_DOC_EXPANSION = "list"
    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_OPERATION_ID = True

class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URI", "sqlite:///instance/development.db")

class TestingConfig(Config):
    """Configuration for testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URI", "sqlite:///instance/test.db")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=5)  # Tokens expirent rapidement pour les tests

class ProductionConfig(Config):
    """Configuration for production."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DATABASE_URI", "postgresql://user:password@localhost/hbnb")

# Configuration mapping
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
