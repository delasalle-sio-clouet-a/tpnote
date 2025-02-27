from src.exceptions.UndefinedMethodException import UndefinedMethodException

from src.models.Adherents import Adherents
from src.models.Auteurs import Auteurs
from src.models.Editeurs import Editeurs
from src.models.Formats import Formats
from src.models.Livres import Livres
from src.models.Reservations import Reservations

class DataHandler:
    """
    CLASSE ABSTRAITE -> NE PAS INSTANCIER !!! Utiliser l'héritage puis override les fonctions.
    """

    def __init__(self):
        # ne rien faire
        pass

    def adherents_get_by_code(self, code:str) -> Adherents:
        raise UndefinedMethodException()

    def auteurs_get_by_id(self, id:int) -> Auteurs:
        raise UndefinedMethodException()

    def editeurs_get_by_id(self, id:int) -> Editeurs:
        raise UndefinedMethodException()

    def formats_get_by_id(self, id:int) -> Editeurs:
        raise UndefinedMethodException()

    def livres_get_by_isbn(self, code:str) -> Livres:
        raise UndefinedMethodException()