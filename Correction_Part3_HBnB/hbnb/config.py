import os

class Config:
    """Configuration de base pour l'application."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///instance/development.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "super_secret_jwt_key")

class DevelopmentConfig(Config):
    """Configuration pour l'environnement de développement."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration pour l'environnement de production."""
    DEBUG = False

# Dictionnaire pour le choix de configuration
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

