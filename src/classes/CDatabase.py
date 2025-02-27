from src.classes.CDataHandler import DataHandler

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

from src.exceptions.InvalidFormatException import InvalidFormatException

class Database:
    """
    Classe permettant à l'api de communiquer avec un système de stockage de données (sql, mock, ...)
    """
    def __init__(self, _handler:DataHandler):
        self.handler = _handler

    #############
    # ADHERENTS #
    #############
    def adherents_get_by_code(self, code:str) -> Adherent:
        return self.handler.adherents_get_by_code(code)
    
    def adherents_insert(self, _adherent:Adherent) -> bool:
        return self.handler.adherents_insert(_adherent)

    ###########
    # AUTEURS #
    ###########
    def auteurs_get_by_id(self, id:int) -> Auteur:
        return self.handler.auteurs_get_by_id(id)
    
    def auteurs_insert(self, _auteur:Auteur) -> bool:
        return self.handler.auteurs_insert(_auteur)

    ############
    # EDTIEURS #
    ############
    def editeurs_get_by_id(self, id:int) -> Editeur:
        return self.handler.editeurs_get_by_id(id)
    
    def editeurs_insert(self, _editeur:Editeur) -> bool:
        return self.handler.editeurs_insert(_editeur)

    ###########
    # FORMATS #
    ###########
    def formats_get_by_id(self, id:int) -> Format:
        return self.handler.formats_get_by_id(id)
    
    def formats_insert(self, _format:Format) -> bool:
        return False

    ##########
    # LIVRES #
    ##########
    def livres_get_by_isbn(self, isbn:str) -> Livre:
        return self.handler.livres_get_by_isbn(isbn)
    
    def livres_insert(self, _livre:Livre) -> bool:
        return False
    
    ################
    # RESERVATIONS #
    ################
    def reservations_insert(self, _reservation:Reservation) -> bool:
        return False
    
    def reservations_get_all_by_code_adherent(self, ) -> list:
        return False
    
    def reservations_get_en_cours_by_code_adherent(self, _code_adherent:str) -> list:
        return False
    
    def reservations_get_retards_by_code_adherent(self, _code_adherent:str) -> list:
        return False
    
    def reservations_get_retards_all(self) -> list:
        return False
    
    def reservations_set_rendu(self, _id_reservation:int, _rendu:bool) -> bool:
        return False