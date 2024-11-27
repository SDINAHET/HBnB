from flask import Flask
from app import db, create_app
from flask_migrate import Migrate

# Créer l'application Flask
app = create_app()

# Configurer Flask-Migrate pour la gestion des migrations
migrate = Migrate(app, db)

# Point d'entrée pour démarrer le serveur Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
