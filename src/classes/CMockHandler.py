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
        lesAdherents:list = self.getData("Adherent")
        unAdherent:Adherent
        for unAdherent in lesAdherents:
            if(unAdherent.code_adherent == code):
                return unAdherent
        return None
    

    def adherents_insert(self, _adherent:Adherent) -> bool:
        lesAdherents = self.getData("Adherent")
        unAdherent:Adherent

        # controle code adhérent unique
        for unAdherent in lesAdherents:
            if(unAdherent.code_adherent == _adherent.code_adherent):
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
        lesAuteurs:list = self.getData("Auteur")
        unAuteur:Auteur
        for unAuteur in lesAuteurs:
            if(unAuteur.id == id):
                return unAuteur
        return None
    

    def auteurs_insert(self, _auteur:Auteur) -> bool:
        lesAuteurs = self.getData("Auteur")
        unAuteur:Auteur

        # controle id unique
        for unAuteur in lesAuteurs:
            if(unAuteur.id == _auteur.id):
                raise DuplicataException("Un auteur possède déjà cet identifiant.")

        return True # ajout réussi


    ############
    # EDITEURS #
    ############
    def editeurs_get_by_id(self, id:int) -> Editeur:
        lesEditeurs:list = self.getData("Editeur")
        unEditeur:Editeur
        for unEditeur in lesEditeurs:
            if(unEditeur.id == id):
                return unEditeur
        return None
    

    def editeurs_insert(self, _editeur:Editeur) -> bool:
        lesEditeurs = self.getData("Editeur")
        unEditeur:Editeur

        # controle id unique
        for unEditeur in lesEditeurs:
            if(unEditeur.id == _editeur.id):
                raise DuplicataException("Un éditeur possède déjà cet identifiant.")

        return True # ajout réussi


    ###########
    # FORMATS #
    ###########
    def formats_get_by_id(self, id:int) -> Format:
        lesFormats:list = self.getData("Format")
        unFormat:Format
        for unFormat in lesFormats:
            if(unFormat.id == id):
                return unFormat
        return None


    ##########
    # LIVRES #
    ##########
    def livres_get_by_isbn(self, isbn:str) -> Livre:
        lesLivres:list = self.getData("Livre")
        unLivre:Livre
        for unLivre in lesLivres:
            if(unLivre.code_isbn == id):
                return unLivre
        return None