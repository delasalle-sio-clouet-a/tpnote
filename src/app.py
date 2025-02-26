from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def start():
    import os
    from src.main import create_app, create_database, fill_database, import_controllers
    from src.classes.CConfig import Config

    modulesCharges:list = [] # pour importer les controllers 1 seule fois (voir 'import_controllers()')

    # chargement de la configuration (fichier 'config.yaml')
    repertoireConfig = os.path.abspath(f"{os.path.split(__file__)[0]}/../config")
    config = Config(os.path.join(repertoireConfig, "config.yaml"))

    # création de l'application Flask
    app:Flask = create_app(config)

    # url de l'api
    urlApi = config.urlApi

    # base de données
    db:SQLAlchemy = create_database(config, app)

    # insertion du jeu de test
    fill_database(app, db, config, repertoireConfig)

    # import des controllers
    repertoireControllers:str = os.path.abspath(f"{os.path.split(__file__)[0]}/controllers")
    modulesCharges = import_controllers(repertoireControllers, modulesCharges, app)