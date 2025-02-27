from src.classes.CMailer import Mailer

from src.classes.CAdherent import Adherent
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation
from src.classes.CDatabase import Database

from src.exceptions.MissingDataException import MissingDataException

class MockMailer(Mailer):
    """
    CLASSE ABSTRAITE -> NE PAS INSTANCIER !!! Utiliser l'héritage puis override les fonctions.
    """
    def __init__(self, _database:Database):
        super().__init__(_database)         # lien avec la db (ex: pour récupérer les retards)

    def envoi_mail_retard(self, _code_adherent:str) -> bool:
        # récupérer les retards
        unAdherent = self.database.adherents_get_by_code(_code_adherent)
        if(unAdherent == None):
            raise MissingDataException("Cet adhérent n'existe pas.")
        
        lesRetards:list = self.database.reservations_get_retards_by_code_adherent(_code_adherent)

        msg:str = ""
        if(len(lesRetards) > 0):
            # construction du mail
            to:str = unAdherent.email
            subject:str = "Rappel - Livres en retard"
            msg = self._construction_message_retards(unAdherent, lesRetards)
            return True, msg    # mail envoyé (simulé)
        else:
            return False, msg    # ne pas envoyer de mail si aucun retard n'a été trouvé
