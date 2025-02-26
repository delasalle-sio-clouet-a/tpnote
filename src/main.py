import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

def create_app(_config) -> Flask:
    app:Flask = Flask()

    return app

def create_database(_app:Flask, _config, _db) -> SQLAlchemy:
# générer la chaîne utilisée pour accéder à la base de données
    param_bdd = f"{_config.dbDialect}://{_config.dbUser}:{_config.dbPassword}@{_config.dbServer}/{_config.dbBase}"
    _app.logger.debug("URL de connexion vers la base SQL : '%s'", param_bdd)
    _app.config['SQLALCHEMY_DATABASE_URI'] = param_bdd
    # à désactiver car gourmand en ressources
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # créer une instance de la base de données
    _db.init_app(_app)

    # connection à la base de données
    with _app.app_context():
        essais = 0
        dbConnectee = False
        while(essais < 5 and dbConnectee == False):
            essais += 1
            try:
                _db.session.execute(text('SELECT 1'))
                dbConnectee = True
            except Exception as e:
                dbConnectee = False
                _app.logger.warning(f"Echec de la connexion à la base de données : {str(e)} (tentative {essais}/5)")
            if(dbConnectee == False):
                time.sleep(5)
    if(dbConnectee):
        _app.logger.info("Connexion à la base de données réussie. Tables générées.")
    else:
        _app.logger.critical("Echec de la connexion à la base de données.")

    return _db

def fill_database():
    pass

def import_controllers():
    pass