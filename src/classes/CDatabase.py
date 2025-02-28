import re
from datetime import timedelta

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

class Database:
    """
    Classe permettant à l'api de communiquer avec un système de stockage de données (sql, mock, ...)
    """
    def __init__(self, _handler:DataHandler):
        self.handler = _handler

    #############
    # ADHERENTS #
    #############
    def adherents_get_all(self) -> list:
        return self.handler.adherents_get_all()

    def adherents_get_by_code(self, code:str) -> Adherent:
        return self.handler.adherents_get_by_code(code)
    
    def adherents_insert(self, _adherent:Adherent) -> bool:
        lesExistants = self.adherents_get_all()
        unExistant:Adherent

        # controle code adhérent unique
        for unExistant in lesExistants:
            if(unExistant.code_adherent == _adherent.code_adherent):
                raise DuplicataException("Ce code adhérent est déjà utilisé.")
            
        # controle email valide
        regex = r"^[a-zA-Z0-9_.+-]+\@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if(_adherent.email == None or re.match(regex, str(_adherent.email)) is None):
            print(_adherent.email)
            raise InvalidFormatException("Format de l'email invalide.")
        
        # contrôle code adhérent (longueur + numérique)
        if(len(_adherent.code_adherent) != 5):
            raise InvalidFormatException("Le code adhérent ne fait pas 5 caractères.")
        if(_adherent.code_adherent.isdigit() == False):
            raise InvalidFormatException("Le code adhérent contient des caractères non numériques.")
        
        return self.handler.adherents_insert(_adherent)

    ###########
    # AUTEURS #
    ###########
    def auteurs_get_all(self) -> list:
        return self.handler.auteurs_get_all()
    
    def auteurs_get_by_id(self, id:int) -> Auteur:
        return self.handler.auteurs_get_by_id(id)
    
    def auteurs_insert(self, _auteur:Auteur) -> bool:
        lesExistants = self.auteurs_get_all()
        unExistant:Auteur

        # controle id unique
        for unExistant in lesExistants:
            if(unExistant.id == _auteur.id):
                raise DuplicataException("Un auteur possède déjà cet identifiant.")
            
        return self.handler.auteurs_insert(_auteur)

    ############
    # EDTIEURS #
    ############
    def editeurs_get_all(self) -> list:
        return self.handler.editeurs_get_all()
    
    def editeurs_get_by_id(self, id:int) -> Editeur:
        return self.handler.editeurs_get_by_id(id)
    
    def editeurs_insert(self, _editeur:Editeur) -> bool:
        lesExistants = self.editeurs_get_all()
        unExistant:Editeur

        # controle id unique
        for unExistant in lesExistants:
            if(unExistant.id == _editeur.id):
                raise DuplicataException("Un éditeur possède déjà cet identifiant.")
            
        return self.handler.editeurs_insert(_editeur)

    ###########
    # FORMATS #
    ###########
    def formats_get_all(self) -> list:
        return self.handler.formats_get_all()
    
    def formats_get_by_id(self, id:int) -> Format:
        return self.handler.formats_get_by_id(id)
    
    def formats_insert(self, _format:Format) -> bool:
        lesExistants = self.formats_get_all()
        unExistant:Format

        # controle id unique
        for unExistant in lesExistants:
            if(unExistant.id == _format.id):
                raise DuplicataException("Un format possède déjà cet identifiant.")
            
        return self.handler.formats_insert(_format)

    ##########
    # LIVRES #
    ##########
    def livres_get_all(self) -> list:
        return self.handler.livres_get_all()
    
    def livres_get_by_isbn(self, isbn:str) -> Livre:
        return self.handler.livres_get_by_isbn(isbn)
    
    def livres_insert(self, _livre:Livre) -> bool:
        lesExistants = self.livres_get_all()
        unExistant:Livre

        # controle aucun champ vide
        interdit = [None, ""]
        if(_livre.code_isbn.strip() in interdit or _livre.id_auteur in interdit or _livre.id_editeur in interdit or _livre.id_format in interdit or _livre.titre in interdit):
            raise MissingDataException("Données incomplètes.")

        # controle isbn unique
        for unExistant in lesExistants:
            if(unExistant.code_isbn == _livre.code_isbn):
                raise DuplicataException("Un livre possède déjà ce code isbn.")
        
        # transformation de l'isbn s'il contient des tirets
        _livre.code_isbn = _livre.code_isbn.replace("-", "")

        # controle longueur du code isbn
        if(len(_livre.code_isbn) != 10):
            raise InvalidIsbnException("Le code isbn doit faire 10 caractères.")
        
        # controle des caracteres du code isbn (sauf dernier caractere qui accepte le 'X')
        caracteresAutorisesHorsClef = ["0","1","2","3","4","5","6","7","8","9"]
        for index, unCaractere in enumerate(str(_livre.code_isbn)[:-1]):
            if(unCaractere not in caracteresAutorisesHorsClef):
                raise InvalidIsbnException("Le code isbn contient des caractères non autorisés.")
        if(str(_livre.code_isbn)[-1] not in caracteresAutorisesHorsClef+["X"]):
            raise InvalidIsbnException("Le code isbn contient des caractères non autorisés.")
        
        # controle de la clef du code isbn
        poids:int = len(_livre.code_isbn)
        modulo:int = poids + 1
        total:int = 0
        total = sum( [ (poids-index)*int(unCaractere.replace("X","10")) for index, unCaractere in enumerate(_livre.code_isbn) ] )
        if(total%modulo != 0):
            raise InvalidIsbnException("La clé du code isbn est incorrecte.")
        
        # controle auteur existant
        unAuteur = self.auteurs_get_by_id(_livre.id_auteur)
        if(unAuteur == None or isinstance(unAuteur, Auteur) == False):
            raise MissingDataException("L'auteur du livre n'existe pas.")
        
        # controle editeur existant
        unEditeur = self.editeurs_get_by_id(_livre.id_editeur)
        if(unEditeur == None or isinstance(unEditeur, Editeur) == False):
            raise MissingDataException("L'éditeur du livre n'existe pas.")
        
        # controle format existant
        unFormat = self.formats_get_by_id(_livre.id_format)
        if(unFormat == None or isinstance(unFormat, Format) == False):
            raise MissingDataException("Le format du livre n'existe pas.")
        
        return self.handler.livres_insert(_livre)
    
    ################
    # RESERVATIONS #
    ################
    def reservations_get_all(self) -> list:
        return self.handler.reservations_get_all()
    
    def reservations_get_by_id(self, _id:int) -> bool:
        return self.handler.reservations_get_by_id(_id)

    def reservations_insert(self, _reservation:Reservation) -> bool:
        # controle adherent existant
        unAdherent = self.adherents_get_by_code(_reservation.code_adherent)
        if(unAdherent == None or isinstance(unAdherent, Adherent) == False):
            raise MissingDataException("L'adhérent n'existe pas.")
        
        # controle livre existant
        unLivre = self.livres_get_by_isbn(_reservation.code_isbn)
        if(unLivre == None or isinstance(unLivre, Livre) == False):
            raise MissingDataException("Le livre n'existe pas.")
        
        # controle cohérence date fin
        if(_reservation.date_heure_fin < _reservation.date_heure_debut):
            raise ValueError("La date de fin est inférieure à la date de début.")
        
        # controle duree de la reservation
        delta:timedelta = _reservation.date_heure_fin - _reservation.date_heure_debut
        nbJours:float = delta.total_seconds() / 60 / 60 / 24
        print(nbJours)
        if(nbJours > 4*30):
            raise ValueError("La réservation fait plus de quatre mois.")

        # controle collision
        lesReservationsDuLivre:list = self.reservations_get_all_by_code_isbn(_reservation.code_isbn)
        uneReservation:Reservation
        for uneReservation in lesReservationsDuLivre:
            if(uneReservation.rendu == False):  # ignorer les réservations déjà closes (livre rendu)
                if(uneReservation.date_heure_fin > _reservation.date_heure_debut < uneReservation.date_heure_fin
                    or uneReservation.date_heure_debut > _reservation.date_heure_fin < uneReservation.date_heure_fin):
                    raise ValueError("Ce livre est déjà réservé dans cet intervalle.")
                
        # controle nombre de reservations en cours de l'adherent
        lesReservationsEnCours = self.reservations_get_en_cours_by_code_adherent(_reservation.code_adherent)
        if(len(lesReservationsEnCours) >= 3):
            raise ValueError("L'adhérent a déjà atteint le nombre maximal de réservations en cours.")
        
        return self.handler.reservations_insert(_reservation)
    
    def reservations_get_all_by_code_adherent(self, _code_adherent:str) -> list:
        return self.handler.reservations_get_all_by_code_adherent(_code_adherent)
    
    def reservations_get_all_by_code_isbn(self, _isbn:str) -> list:
        return self.handler.reservations_get_all_by_code_isbn(_isbn)
    
    def reservations_get_en_cours_by_code_adherent(self, _code_adherent:str) -> list:
        return self.handler.reservations_get_en_cours_by_code_adherent(_code_adherent)
    
    def reservations_get_retards_by_code_adherent(self, _code_adherent:str) -> list:
        return self.handler.reservations_get_retards_by_code_adherent(_code_adherent)
    
    def reservations_get_retards_all(self) -> list:
        return self.handler.reservations_get_retards_all()
    
    def reservations_set_rendu(self, _id_reservation:int, _rendu:bool) -> bool:
        # controle reservation existante
        uneReservation = self.reservations_get_by_id(_id_reservation)
        if(uneReservation == None or isinstance(uneReservation, Reservation) == False):
            raise MissingDataException("Cette réservation n'existe pas.")
        
        return self.handler.reservations_set_rendu(_id_reservation, _rendu)