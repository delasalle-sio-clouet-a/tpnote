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

    def adherents_get_by_code(self, code:str) -> Adherent:
        raise UndefinedMethodException()

    def auteurs_get_by_id(self, id:int) -> Auteur:
        raise UndefinedMethodException()

    def editeurs_get_by_id(self, id:int) -> Editeur:
        raise UndefinedMethodException()

    def formats_get_by_id(self, id:int) -> Editeur:
        raise UndefinedMethodException()

    def livres_get_by_isbn(self, code:str) -> Livre:
        raise UndefinedMethodException()