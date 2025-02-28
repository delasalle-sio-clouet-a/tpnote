import os, yaml, re

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from datetime import timedelta, date, datetime

from src.classes.CDataHandler import DataHandler
from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

from src.exceptions.DuplicataException import DuplicataException
from src.exceptions.InvalidFormatException import InvalidFormatException
from src.exceptions.InvalidIsbnException import InvalidIsbnException
from src.exceptions.InvalidTypeException import InvalidTypeException
from src.exceptions.MissingDataException import MissingDataException
from src.exceptions.UndefinedMethodException import UndefinedMethodException

from src.models.Adherents import Adherents
from src.models.Auteurs import Auteurs
from src.models.Editeurs import Editeurs
from src.models.Formats import Formats
from src.models.Livres import Livres
from src.models.Reservations import Reservations

class SqlHandler(DataHandler):
    """
    Classe héritant de DataHandler.
    Permet d'interagir avec des données de d'une base de données SQL.
    """
    def __init__(self):
        super().__init__()

        self.db = SQLAlchemy()
        self.app = None

    def set_app(self, _app:Flask):
        self.app = _app
    
    def set_connection_data(self, prefixe:str, server:str, user:str, password:str, base:str):
        self.connectionString = f"{prefixe}://{user}:{password}@{server}/{base}"
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.connectionString
        # à désactiver car gourmand en ressources
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    def init_db(self):
        self.db.init_app(self.app)


    #############
    # ADHERENTS #
    #############
    def adherents_get_all(self) -> list:
        lesAdherentsSql = self.db.session.query(Adherents).all()
        return [self._sql_to_local(unAdherent) for unAdherent in lesAdherentsSql]
    

    def adherents_get_by_code(self, code:str) -> Adherent:
        unAdherent = self.db.session.query(Adherents).filter(Adherents.code_adherent==code).first()
        return self._sql_to_local(unAdherent)
    

    def adherents_insert(self, _adherent:Adherent) -> bool:
        adherentSql = self._local_to_sql(_adherent)
        try:
            self.db.session.add(adherentSql)
            self.db.session.commit()
            return True # ajout réussi
        except Exception as e:
            self.app.logger.error(e)
            return False










    



    def _sql_to_local(self, objet_sql):
        if(objet_sql == None): return None

        objet_local = globals()[type(objet_sql).__name__[:-1]]()
        for uneVariable in objet_sql.__dict__:
            if(str(uneVariable).startswith("__") == False):
                objet_local.__dict__[uneVariable] = objet_sql.__dict__[uneVariable]
        return objet_local
    
    def _local_to_sql(self, objet_local):
        if(objet_local == None): return None

        objet_sql = globals()[f"{type(objet_local).__name__}s"]()
        for uneVariable in objet_local.__dict__:
            if(str(uneVariable).startswith("__") == False):
                objet_sql.__dict__[uneVariable] = objet_local.__dict__[uneVariable]
        return objet_sql