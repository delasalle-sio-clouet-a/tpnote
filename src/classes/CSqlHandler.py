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


    ###########
    # AUTEURS #
    ###########
    def auteurs_get_all(self) -> list:
        return self.getData("Auteur")
    
    def auteurs_get_by_id(self, id:int) -> Auteur:
        lesExistants:list = self.auteurs_get_all()
        unExistant:Auteur
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def auteurs_insert(self, _auteur:Auteur) -> bool:
        return True # ajout réussi


    ############
    # EDITEURS #
    ############
    def editeurs_get_all(self) -> list:
        return self.getData("Editeur")
    

    def editeurs_get_by_id(self, id:int) -> Editeur:
        lesExistants:list = self.editeurs_get_all()
        unExistant:Editeur
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def editeurs_insert(self, _editeur:Editeur) -> bool:
        return True # ajout réussi


    ###########
    # FORMATS #
    ###########
    def formats_get_all(self) -> list:
        return self.getData("Format")
    
    def formats_get_by_id(self, id:int) -> Format:
        lesExistants:list = self.formats_get_all()
        unExistant:Format
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def formats_insert(self, _format:Format) -> bool:
        return True # ajout réussi


    ##########
    # LIVRES #
    ##########
    def livres_get_all(self) -> list:
        return self.getData("Livre")
    

    def livres_get_by_isbn(self, _isbn:str) -> Livre:
        lesLivres:list = self.livres_get_all()
        unLivre:Livre
        for unLivre in lesLivres:
            if(unLivre.code_isbn == _isbn):
                return unLivre
        return None
    
    def livres_insert(self, _livre:Livre) -> bool:
        return True # ajout réussi
    

    ################
    # RESERVATIONS #
    ################
    def reservations_get_all(self) -> list:
        return self.getData("Reservation")
    

    def reservations_get_by_id(self, _id):
        lesExistants:list = self.reservations_get_all()
        unExistant:Reservation
        for unExistant in lesExistants:
            if(unExistant.id == _id):
                return unExistant
        return None
    
    
    def reservations_get_all_by_code_isbn(self, _isbn):
        lesExistants:list = self.reservations_get_all()
        unExistant:Reservation
        reservationsLivre:list = []
        for unExistant in lesExistants:
            if(unExistant.code_isbn == _isbn):
                reservationsLivre.append(unExistant)
        return reservationsLivre
    

    def reservations_get_all_by_code_adherent(self, _code_adherent):
        lesExistants:list = self.reservations_get_all()
        unExistant:Reservation
        reservationsLivre:list = []
        for unExistant in lesExistants:
            if(unExistant.code_adherent == _code_adherent):
                reservationsLivre.append(unExistant)
        return reservationsLivre
    

    def reservations_insert(self, _reservation:Reservation) -> bool:
        return True # ajout réussi
    

    def reservations_set_rendu(self, _id_reservation, _rendu) -> bool:
        return True # modification réussie
    

    def reservations_get_en_cours_by_code_adherent(self, _code_adherent):
        lesReservations:list = self.reservations_get_all_by_code_adherent(_code_adherent)
        lesResEnCours:list = []
        uneReservation:Reservation
        for uneReservation in lesReservations:
            if( (uneReservation.date_heure_fin >= datetime.now() and uneReservation.rendu == True) or uneReservation.rendu == False):
                lesResEnCours.append(uneReservation)
        return lesResEnCours
    

    def reservations_get_retards_by_code_adherent(self, _code_adherent):
        lesReservations:list = self.reservations_get_all_by_code_adherent(_code_adherent)
        lesResEnRetard:list = []
        uneReservation:Reservation
        for uneReservation in lesReservations:
            if(uneReservation.date_heure_fin < datetime.now() and uneReservation.rendu == False):
                lesResEnRetard.append(uneReservation)
        return lesResEnRetard
    

    def reservations_get_retards_all(self):
        lesReservations = self.reservations_get_all()
        lesRetards:list = []
        uneReservation:Reservation
        for uneReservation in lesReservations:
            if(uneReservation.date_heure_fin < datetime.now() and uneReservation.rendu == False):
                lesRetards.append(uneReservation)
        return lesRetards
    



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