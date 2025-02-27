from src.classes.CDataHandler import DataHandler

from src.models.Adherents import Adherents
from src.models.Auteurs import Auteurs
from src.models.Editeurs import Editeurs
from src.models.Formats import Formats
from src.models.Livres import Livres
from src.models.Reservations import Reservations

class Database:
    """
    Classe permettant à l'api de communiquer avec un système de stockage de données (sql, mock, ...)
    """
    def __init__(self, _handler:DataHandler):
        self.handler = _handler

    def adherents_get_by_code(self, jsonData:str) -> Adherents:
        return self.handler.adherents_get_by_code(jsonData)

    def auteurs_get_by_id(self, jsonData:str) -> Auteurs:
        return self.handler.auteurs_get_by_id(jsonData)

    def editeurs_get_by_id(self, jsonData:str) -> Editeurs:
        return self.handler.editeurs_get_by_id(jsonData)

    def formats_get_by_id(self, jsonData:str) -> Editeurs:
        return self.handler.formats_get_by_id(jsonData)

    def livres_get_by_isbn(self, jsonData:str) -> Livres:
        return self.handler.livres_get_by_isbn(jsonData)