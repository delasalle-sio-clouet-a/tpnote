from src.classes.CDataHandler import DataHandler

from src.models.Adherents import Adherents
from src.models.Auteurs import Auteurs
from src.models.Editeurs import Editeurs
from src.models.Formats import Formats
from src.models.Livres import Livres
from src.models.Reservations import Reservations

class MockHandler(DataHandler):
    """
    Classe héritant de DataHandler.
    Permet d'interagir avec des données de test, configurables à l'aide des fichiers du répertoire 'config/database_filler'.
    """

    def __init__(self):
        super().__init__()
        # a faire : charger les données yaml de 'config/database_filler'

    def adherents_get_by_code(self, code:str) -> Adherents:
        pass

    def auteurs_get_by_id(self, id:int) -> Auteurs:
        pass

    def editeurs_get_by_id(self, id:int) -> Editeurs:
        pass

    def formats_get_by_id(self, id:int) -> Editeurs:
        pass

    def livres_get_by_isbn(self, code:str) -> Livres:
        pass