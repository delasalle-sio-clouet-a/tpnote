class Livre():
    def __init__(self, _code_isbn:str=None, _titre:str=None, _id_auteur:int=None, _id_editeur:int=None, _id_format:int=None):
        self.code_isbn:str = _code_isbn
        self.titre:str = _titre
        self.id_auteur:int = _id_auteur
        self.id_editeur:int = _id_editeur
        self.id_format:int = _id_format