from src.classes.CAdherent import Adherent
from src.classes.CReservation import Reservation
from src.classes.CDatabase import Database
from src.classes.CLivre import Livre

from src.exceptions.UndefinedMethodException import UndefinedMethodException

class Mailer:
    """
    CLASSE ABSTRAITE -> NE PAS INSTANCIER !!! Utiliser l'héritage puis override les fonctions.
    """
    def __init__(self, _database:Database):
        self.database = _database
        # ne rien faire
        pass

    def envoi_mail_retard(self, _code_adherent:str) -> bool:
        """
        Retourne un tuple (bool, str).
        Retourne True si le mail a bien été envoyé, False sinon, avec le contenu du mail en chaîne de caractères à chaque fois.
        """
        raise UndefinedMethodException()
    
    def _construction_message_retards(self, _adherent:Adherent, _reservationsRetards:list):
        """
        Retourne le message construit en chaîne de caractères.
        """
        msg = f"{'Monsieur' if _adherent.civilite == False else 'Madame'} {_adherent.nom}," + "\r\n"
        msg += f"Vous avez {len(_reservationsRetards)} livres à rendre en retard :" + "\r\n" + "\r\n"
        lesLivres:list = []
        unRetard:Reservation
        for unRetard in _reservationsRetards:
            unLivreEnBase:Livre = self.database.livres_get_by_isbn(unRetard.code_isbn)
            lesLivres.append(unLivreEnBase)

        unLivre:Livre
        for unLivre in lesLivres:
            msg += f"- {unLivre.titre}" + "\r\n"

        return msg