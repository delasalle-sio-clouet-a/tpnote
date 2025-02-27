import os, yaml, re

from src.classes.CDataHandler import DataHandler

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

from src.exceptions.DuplicataException import DuplicataException
from src.exceptions.InvalidFormatException import InvalidFormatException
from src.exceptions.InvalidIsbnException import InvalidIsbnException
from src.exceptions.InvalidTypeException import InvalidTypeException
from src.exceptions.MissingDataException import MissingDataException
from src.exceptions.UndefinedMethodException import UndefinedMethodException

class MockHandler(DataHandler):
    """
    Classe héritant de DataHandler.
    Permet d'interagir avec des données de test, configurables à l'aide des fichiers du répertoire 'config/database_filler'.
    """
    def __init__(self):
        super().__init__()

        self.data:dict = {} # jdd actif
        self.dataYaml:dict = {} # données des fichiers lus
        self.repertoireDatabaseFiller = os.path.join(os.path.abspath(f"{os.path.split(__file__)[0]}/../../config"), "database_filler")

        self._lecture_fichiers() # préparation du jeu de données



    def _lecture_fichiers(self):
        """
        METHODE PRIVEE. Récupère les fichiers YAML du répertoire 'config/database_filler' et en extrait les données en lecture.
        """
        print("<DatabaseFiller> Chargement des fichiers...")
        # lister tous les fichiers yaml présents
        lesFichiers = [os.path.join(self.repertoireDatabaseFiller,file) for file in os.listdir(self.repertoireDatabaseFiller) if file.endswith(".yaml")]
        print(f"<DatabaseFiller> Fichiers trouvés : {lesFichiers}")

        # pour chaque fichier :
        # - son nom est un nombre + nom du modèke concerné (le nombre sert à lire les fichiers dans un certain ordre)
        # - l'attribut 'type' définit s'il s'agit d'un remplissage ou d'un jeu de test
        # - l'attribut 'data' est une liste avec les données à ajouter :
        #   - liste de clés-valeurs, avec la clé le nom du champ dans la base de données à affecter
        for unFichier in lesFichiers:
            repertoire, nom = os.path.split(unFichier)
            nomModele = ''.join(c for c in nom.split(".")[0] if not c.isdigit()) # récupérer le nom du modèle concerné
            with open(unFichier, "r", encoding="utf-8") as file:
                config:dict = yaml.load(file, Loader=yaml.FullLoader)
                type:str = config.get("type","remplissage") # type défini à 'remplissage' si la valeur est absente du fichier
                data:list = config.get("data", []) # les données à ajouter

                # conserver les données en mémoire
                if(data != None and len(data) > 0):
                    self.dataYaml[nomModele] = data
                    for uneData in data:
                        instance = globals()[nomModele]()
                        for uneVariable in uneData:
                            instance.__dict__[uneVariable] = uneData[uneVariable]

                        if(nomModele not in self.data):
                            self.data[nomModele] = []
                        self.data[nomModele].append(instance)
                    print(f"<DatabaseFiller> Fichier '{nom}' valide et ajouté en tant que fichier de remplissage.")
                else:
                    print(f"<DatabaseFiller> Fichier '{nom}' ignoré : aucune donnée à insérer.")

        print(self.dataYaml)
        print(self.data)
        print("<DatabaseFiller> Chargement des fichiers terminé.")



    def getData(self, _modele:str) -> list:
        return list(self.data.get(_modele, []))


    #############
    # ADHERENTS #
    #############
    def adherents_get_by_code(self, code:str) -> Adherent:
        lesExistants:list = self.getData("Adherent")
        unExistant:Adherent
        for unExistant in lesExistants:
            if(unExistant.code_adherent == code):
                return unExistant
        return None
    

    def adherents_insert(self, _adherent:Adherent) -> bool:
        lesExistants = self.getData("Adherent")
        unExistant:Adherent

        # controle code adhérent unique
        for unExistant in lesExistants:
            if(unExistant.code_adherent == _adherent.code_adherent):
                raise DuplicataException("Ce code adhérent est déjà utilisé.")
            
        # controle email valide
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if(_adherent.email == None or re.match(regex, str(_adherent.email)) is None):
            raise InvalidFormatException("Format de l'email invalide.")
        
        # contrôle code adhérent (longueur + numérique)
        if(len(_adherent.code_adherent) != 5):
            raise InvalidFormatException("Le code adhérent ne fait pas 5 caractères.")
        if(_adherent.code_adherent.isdigit() == False):
            raise InvalidFormatException("Le code adhérent contient des caractères non numériques.")

        return True # ajout réussi


    ###########
    # AUTEURS #
    ###########
    def auteurs_get_by_id(self, id:int) -> Auteur:
        lesExistants:list = self.getData("Auteur")
        unExistant:Auteur
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def auteurs_insert(self, _auteur:Auteur) -> bool:
        lesExistants = self.getData("Auteur")
        unExistant:Auteur

        # controle id unique
        for unExistant in lesExistants:
            if(unExistant.id == _auteur.id):
                raise DuplicataException("Un auteur possède déjà cet identifiant.")

        return True # ajout réussi


    ############
    # EDITEURS #
    ############
    def editeurs_get_by_id(self, id:int) -> Editeur:
        lesExistants:list = self.getData("Editeur")
        unExistant:Editeur
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def editeurs_insert(self, _editeur:Editeur) -> bool:
        lesExistants = self.getData("Editeur")
        unExistant:Editeur

        # controle id unique
        for unExistant in lesExistants:
            if(unExistant.id == _editeur.id):
                raise DuplicataException("Un éditeur possède déjà cet identifiant.")

        return True # ajout réussi


    ###########
    # FORMATS #
    ###########
    def formats_get_by_id(self, id:int) -> Format:
        lesExistants:list = self.getData("Format")
        unExistant:Format
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def formats_insert(self, _format:Format) -> bool:
        lesExistants = self.getData("Format")
        unExistant:Format

        # controle id unique
        for unExistant in lesExistants:
            if(unExistant.id == _format.id):
                raise DuplicataException("Un format possède déjà cet identifiant.")

        return True # ajout réussi


    ##########
    # LIVRES #
    ##########
    def livres_get_by_isbn(self, _isbn:str) -> Livre:
        lesLivres:list = self.getData("Livre")
        unLivre:Livre
        for unLivre in lesLivres:
            if(unLivre.code_isbn == _isbn):
                return unLivre
        return None
    
    def livres_insert(self, _livre:Livre) -> bool:
        lesExistants = self.getData("Livre")
        unExistant:Livre

        # controle isbn unique
        for unExistant in lesExistants:
            if(unExistant.code_isbn == _livre.code_isbn):
                raise DuplicataException("Un livre possède déjà ce code isbn.")
        
        # transformation de l'isbn s'il contient des tirets
        _livre.code_isbn = _livre.code_isbn.replace("-", "")

        # controle longueur du code isbn
        if(len(_livre.code_isbn) != 10):
            raise InvalidIsbnException("Le code isbn doit faire 10 caractères.")
        
        # controle des caracteres du code isbn (sauf dernier caractere qui accepte le 'X')
        caracteresAutorisesHorsClef = ["0","1","2","3","4","5","6","7","8","9"]
        for index, unCaractere in enumerate(str(_livre.code_isbn)[:-1]):
            if(unCaractere not in caracteresAutorisesHorsClef):
                raise InvalidIsbnException("Le code isbn contient des caractères non autorisés.")
        if(str(_livre.code_isbn)[-1] not in caracteresAutorisesHorsClef+["X"]):
            raise InvalidIsbnException("Le code isbn contient des caractères non autorisés.")
        
        # controle de la clef du code isbn
        poids:int = len(_livre.code_isbn)
        modulo:int = poids + 1
        total:int = 0
        total = sum( [ (poids-index)*int(unCaractere.replace("X","10")) for index, unCaractere in enumerate(_livre.code_isbn) ] )
        if(total%modulo != 0):
            raise InvalidIsbnException("La clé du code isbn est incorrecte.")
        
        # controle auteur existant
        unAuteur = self.auteurs_get_by_id(_livre.id_auteur)
        if(unAuteur == None or isinstance(unAuteur, Auteur) == False):
            raise MissingDataException("L'auteur du livre n'existe pas.")
        
        # controle editeur existant
        unEditeur = self.editeurs_get_by_id(_livre.id_editeur)
        if(unEditeur == None or isinstance(unEditeur, Editeur) == False):
            raise MissingDataException("L'éditeur du livre n'existe pas.")
        
        # controle format existant
        unFormat = self.formats_get_by_id(_livre.id_format)
        if(unFormat == None or isinstance(unFormat, Format) == False):
            raise MissingDataException("Le format du livre n'existe pas.")

        return True # ajout réussi
    

    ################
    # RESERVATIONS #
    ################
    def reservations_get_by_id(self, _id):
        lesExistants:list = self.getData("Reservation")
        unExistant:Reservation
        for unExistant in lesExistants:
            if(unExistant.id == _id):
                return unExistant
        return None
    
    def reservations_insert(self, _reservation:Reservation) -> bool:

        # controle adherent existant
        unAdherent = self.adherents_get_by_code(_reservation.code_adherent)
        if(unAdherent == None or isinstance(unAdherent, Adherent) == False):
            raise MissingDataException("L'adhérent n'existe pas.")
        
        # controle livre existant
        unLivre = self.livres_get_by_isbn(_reservation.code_isbn)
        if(unLivre == None or isinstance(unLivre, Livre) == False):
            raise MissingDataException("Le livre n'existe pas.")

        return True # ajout réussi
    

    def reservations_set_rendu(self, _id_reservation, _rendu) -> bool:

        # controle reservation existante
        uneReservation = self.reservations_get_by_id(_id_reservation)
        if(uneReservation == None or isinstance(uneReservation, Reservation) == False):
            raise MissingDataException("Cette réservation n'existe pas.")

        return True # modification réussie