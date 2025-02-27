from datetime import datetime

class Reservation():
    def __init__(self, _codeAdherent:str=None, _codeIsbn:str=None, _dateHeureDebut:datetime=None, _dateHeureFin:datetime=None, _rendu:bool=False):
        self.code_adherent:str = _codeAdherent
        self.code_isbn:str = _codeIsbn
        self.date_heure_debut:datetime = _dateHeureDebut
        self.date_heure_fin:datetime = _dateHeureFin
        self.rendu:bool = _rendu                        # booléen pour savoir si le livre a été rendu ou non