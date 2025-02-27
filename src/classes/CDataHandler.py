from src.exceptions.UndefinedMethodException import UndefinedMethodException

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

class DataHandler:
    """
    CLASSE ABSTRAITE -> NE PAS INSTANCIER !!! Utiliser l'héritage puis override les fonctions.
    """

    def __init__(self):
        # ne rien faire
        pass

    #############
    # ADHERENTS #
    #############
    def adherents_get_by_code(self, jsonData:str) -> Adherent:
        raise UndefinedMethodException()
    
    def adherents_insert(self, _adherent:Adherent) -> bool:
        raise UndefinedMethodException()

    ###########
    # AUTEURS #
    ###########
    def auteurs_get_by_id(self, jsonData:str) -> Auteur:
        raise UndefinedMethodException()
    
    def auteurs_insert(self, _auteur:Auteur) -> bool:
        raise UndefinedMethodException()

    ############
    # EDTIEURS #
    ############
    def editeurs_get_by_id(self, jsonData:str) -> Editeur:
        raise UndefinedMethodException()
    
    def editeurs_insert(self, _editeur:Editeur) -> bool:
        raise UndefinedMethodException()

    ###########
    # FORMATS #
    ###########
    def formats_get_by_id(self, jsonData:str) -> Format:
        raise UndefinedMethodException()
    
    def formats_insert(self, _format:Format) -> bool:
        raise UndefinedMethodException()

    ##########
    # LIVRES #
    ##########
    def livres_get_by_isbn(self, jsonData:str) -> Livre:
        raise UndefinedMethodException()
    
    def livres_insert(self, _livre:Livre) -> bool:
        raise UndefinedMethodException()
    
    ################
    # RESERVATIONS #
    ################
    def reservations_get_by_id(self, _id:int) -> bool:
        raise UndefinedMethodException()

    def reservations_insert(self, _reservation:Reservation) -> bool:
        raise UndefinedMethodException()
    
    def reservations_get_all_by_code_adherent(self, ) -> list:
        raise UndefinedMethodException()
    
    def reservations_get_en_cours_by_code_adherent(self, _code_adherent:str) -> list:
        raise UndefinedMethodException()
    
    def reservations_get_retards_by_code_adherent(self, _code_adherent:str) -> list:
        raise UndefinedMethodException()
    
    def reservations_get_retards_all(self) -> list:
        raise UndefinedMethodException()
    
    def reservations_set_rendu(self, _id_reservation:int, _rendu:bool) -> bool:
        raise UndefinedMethodException()