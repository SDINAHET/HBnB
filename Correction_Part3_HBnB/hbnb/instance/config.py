import os

class InstanceConfig:
    """Configuration spécifique pour l'instance."""

    # Base de données utilisée par défaut
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///instance/development.db")

    # Configuration Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "instance_default_secret_key")

    # Configuration JWT (si utilisée)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "instance_jwt_secret_key")

    # Debug mode, désactivé par défaut pour éviter les erreurs accidentelles en production
    DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "yes"]

    # Configuration optionnelle pour d'autres services (par exemple Swagger)
    SWAGGER_UI_DOC_EXPANSION = os.getenv("SWAGGER_UI_DOC_EXPANSION", "list")
    SWAGGER_UI_OPERATION_ID = True
    SWAGGER_UI_JSONEDITOR = True
