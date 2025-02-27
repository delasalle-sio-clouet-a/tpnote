from src.classes.CDataHandler import DataHandler

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

class MockHandler(DataHandler):
    """
    Classe héritant de DataHandler.
    Permet d'interagir avec des données de test, configurables à l'aide des fichiers du répertoire 'config/database_filler'.
    """

    def __init__(self):
        
        super().__init__()
        # a faire : charger les données yaml de 'config/database_filler'
        self.data:dict = {}

    def adherents_get_by_code(self, code:str) -> Adherent:
        pass

    def auteurs_get_by_id(self, id:int) -> Auteur:
        pass

    def editeurs_get_by_id(self, id:int) -> Editeur:
        pass

    def formats_get_by_id(self, id:int) -> Format:
        pass

    def livres_get_by_isbn(self, code:str) -> Livre:
        pass