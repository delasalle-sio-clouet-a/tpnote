from src.classes.CMailer import Mailer

from src.classes.CAdherent import Adherent
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation
from src.classes.CDatabase import Database

class MockMailer(Mailer):
    """
    CLASSE ABSTRAITE -> NE PAS INSTANCIER !!! Utiliser l'héritage puis override les fonctions.
    """
    def __init__(self, _database:Database):
        super().__init__(_database)         # lien avec la db (ex: pour récupérer les retards)

    def envoi_mail_retard(self, adherent:Adherent) -> bool:
        # ici récupérer les retards
        lesRetards:list = []
        lesLivres:list = []
        msg = ""
        if(len(lesRetards) > 0):
            to = adherent.email
            msg += f"{'Monsieur' if adherent.civilite == False else 'Madame'} {adherent.nom}," + "\r\n"
            msg += f"Vous avez {len(lesRetards)} livres à rendre en retard :" + "\r\n"
            unLivre:Livre
            for unLivre in lesLivres:
                msg += f"- {unLivre.titre}" + "\r\n"
            return True, msg
        else:
            return False, msg    # ne pas envoyer de mail si aucun retard n'a été trouvé
