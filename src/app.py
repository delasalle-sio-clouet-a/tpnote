from flask import Flask
from src.classes.CDatabase import Database

def start():
    import os
    from src.main import create_app
    from src.classes.CConfig import Config

    modulesCharges:list = [] # pour importer les controllers 1 seule fois (voir 'import_controllers()')

    # chargement de la configuration (fichier 'config.yaml')
    repertoireConfig = os.path.abspath(f"{os.path.split(__file__)[0]}/../config")
    config = Config(os.path.join(repertoireConfig, "config.yaml"))

    # création de l'application Flask
    _app, _database = create_app(config)

    return _app, _database




from sqlalchemy.orm import declarative_base
Base = declarative_base()

app:Flask
database:Database
app, database = start()

from src.controllers.ApiController import apiBP
app.register_blueprint(apiBP)