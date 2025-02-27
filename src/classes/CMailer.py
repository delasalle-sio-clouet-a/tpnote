from src.classes.CAdherent import Adherent
from src.classes.CReservation import Reservation
from src.classes.CDatabase import Database

from src.exceptions.UndefinedMethodException import UndefinedMethodException

class Mailer:
    """
    CLASSE ABSTRAITE -> NE PAS INSTANCIER !!! Utiliser l'héritage puis override les fonctions.
    """
    def __init__(self, _database:Database):
        self.database = _database
        # ne rien faire
        pass

    def envoi_mail_retard(self, adherent:Adherent) -> bool:
        """
        Retourne un tuple (bool, str).
        Retourne True si le mail a bien été envoyé, False sinon, avec le contenu du mail en chaîne de caractères à chaque fois.
        """
        raise UndefinedMethodException()