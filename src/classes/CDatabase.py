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
        return self.handler.formats_insert(_format)

    ##########
    # LIVRES #
    ##########
    def livres_get_by_isbn(self, isbn:str) -> Livre:
        return self.handler.livres_get_by_isbn(isbn)
    
    def livres_insert(self, _livre:Livre) -> bool:
        return self.handler.livres_insert(_livre)
    
    ################
    # RESERVATIONS #
    ################
    def reservations_get_by_id(self, _id:int) -> bool:
        return self.handler.reservations_get_by_id(_id)

    def reservations_insert(self, _reservation:Reservation) -> bool:
        return self.handler.reservations_insert(_reservation)
    
    def reservations_get_all_by_code_adherent(self, _code_adherent:str) -> list:
        return self.handler.reservations_get_all_by_code_adherent(_code_adherent)
    
    def reservations_get_all_by_code_isbn(self, _isbn:str) -> list:
        return self.handler.reservations_get_all_by_code_isbn(_isbn)
    
    def reservations_get_en_cours_by_code_adherent(self, _code_adherent:str) -> list:
        return False
    
    def reservations_get_retards_by_code_adherent(self, _code_adherent:str) -> list:
        return False
    
    def reservations_get_retards_all(self) -> list:
        return False
    
    def reservations_set_rendu(self, _id_reservation:int, _rendu:bool) -> bool:
        return self.handler.reservations_set_rendu(_id_reservation, _rendu)