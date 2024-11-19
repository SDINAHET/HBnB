# Configuration file for settings
import os

class Config:
    """
    Base configuration class for HBnB project.

    Attributes:
    -----------
    - SECRET_KEY (str): Secret key for the Flask application, used for securely signing the session cookie.
    - JWT_SECRET_KEY (str): Secret key for JWT encoding and decoding.
    - DEBUG (bool): Enable or disable debug mode.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'supersecretjwtkey')
    DEBUG = False

class DevelopmentConfig(Config):
    """
    Development configuration class for HBnB project, inherits from Config.

    Attributes:
    -----------
    - DEBUG (bool): Enable debug mode.
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configuration class for HBnB project, inherits from Config.

    Attributes:
    -----------
    - TESTING (bool): Enable testing mode.
    """
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configuration class for HBnB project, inherits from Config.
    """
    DEBUG = False

# Configuration mapping for different environments.
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
