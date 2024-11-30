from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.models import setup_db
from app.routes import setup_routes

# Initialiser les extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Charger la configuration
    app.config.from_object("config.Config")

    # Initialiser les extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Configurer la base de données
    setup_db(app)

    # Ajouter les routes
    setup_routes(app)

    return app
