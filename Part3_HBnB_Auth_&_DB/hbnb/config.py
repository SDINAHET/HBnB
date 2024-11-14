#!/usr/bin/python3

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = SECRET_KEY  # add SD
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}



# pip install python-dotenv


# Créez un fichier .env à la racine de votre projet et ajoutez-y les clés sensibles :
# Dans un fichier .env (qui doit être ajouté à votre .gitignore pour ne pas le versionner), ajoutez votre clé secrète :

# SECRET_KEY=votre_clé_secrète_ici

# load_dotenv()  # Charger les variables d'environnement depuis le fichier .env
