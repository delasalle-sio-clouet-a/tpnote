from datetime import date

class Adherent():
    def __init__(self, _code_adherent:str=None, _nom:str=None, _prenom:str=None, _date_naissance:date=None, _civilite:bool=None):
        self.code_adherent:str = _code_adherent
        self.nom:str = _nom
        self.prenom:str = _prenom
        self.date_naissance:date = _date_naissance
        self.civilite:bool = _civilite