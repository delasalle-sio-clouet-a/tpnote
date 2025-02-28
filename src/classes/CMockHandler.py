import os, yaml, re

from src.classes.CDataHandler import DataHandler

from datetime import timedelta, date, datetime

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

                            if("date" in uneVariable):
                                if("heure" in uneVariable):
                                    uneData[uneVariable] = datetime.strptime(uneData[uneVariable], "%Y-%m-%d %H:%M:%S")
                                else:
                                    uneData[uneVariable] = datetime.strptime(uneData[uneVariable], "%Y-%m-%d").date()

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
    def adherents_get_all(self) -> list:
        return self.getData("Adherent")
    

    def adherents_get_by_code(self, code:str) -> Adherent:
        lesExistants:list = self.adherents_get_all()
        unExistant:Adherent
        for unExistant in lesExistants:
            if(unExistant.code_adherent == code):
                return unExistant
        return None
    

    def adherents_insert(self, _adherent:Adherent) -> bool:
        return True # ajout réussi


    ###########
    # AUTEURS #
    ###########
    def auteurs_get_all(self) -> list:
        return self.getData("Auteur")
    
    def auteurs_get_by_id(self, id:int) -> Auteur:
        lesExistants:list = self.auteurs_get_all()
        unExistant:Auteur
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def auteurs_insert(self, _auteur:Auteur) -> bool:
        return True # ajout réussi


    ############
    # EDITEURS #
    ############
    def editeurs_get_all(self) -> list:
        return self.getData("Editeur")
    

    def editeurs_get_by_id(self, id:int) -> Editeur:
        lesExistants:list = self.editeurs_get_all()
        unExistant:Editeur
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def editeurs_insert(self, _editeur:Editeur) -> bool:
        return True # ajout réussi


    ###########
    # FORMATS #
    ###########
    def formats_get_all(self) -> list:
        return self.getData("Format")
    
    def formats_get_by_id(self, id:int) -> Format:
        lesExistants:list = self.formats_get_all()
        unExistant:Format
        for unExistant in lesExistants:
            if(unExistant.id == id):
                return unExistant
        return None
    

    def formats_insert(self, _format:Format) -> bool:
        return True # ajout réussi


    ##########
    # LIVRES #
    ##########
    def livres_get_all(self) -> list:
        return self.getData("Livre")
    

    def livres_get_by_isbn(self, _isbn:str) -> Livre:
        lesLivres:list = self.livres_get_all()
        unLivre:Livre
        for unLivre in lesLivres:
            if(unLivre.code_isbn == _isbn):
                return unLivre
        return None
    
    def livres_insert(self, _livre:Livre) -> bool:
        return True # ajout réussi
    

    ################
    # RESERVATIONS #
    ################
    def reservations_get_all(self) -> list:
        return self.getData("Reservation")
    

    def reservations_get_by_id(self, _id):
        lesExistants:list = self.reservations_get_all()
        unExistant:Reservation
        for unExistant in lesExistants:
            if(unExistant.id == _id):
                return unExistant
        return None
    
    
    def reservations_get_all_by_code_isbn(self, _isbn):
        lesExistants:list = self.reservations_get_all()
        unExistant:Reservation
        reservationsLivre:list = []
        for unExistant in lesExistants:
            if(unExistant.code_isbn == _isbn):
                reservationsLivre.append(unExistant)
        return reservationsLivre
    

    def reservations_get_all_by_code_adherent(self, _code_adherent):
        lesExistants:list = self.reservations_get_all()
        unExistant:Reservation
        reservationsLivre:list = []
        for unExistant in lesExistants:
            if(unExistant.code_adherent == _code_adherent):
                reservationsLivre.append(unExistant)
        return reservationsLivre
    

    def reservations_insert(self, _reservation:Reservation) -> bool:
        return True # ajout réussi
    

    def reservations_set_rendu(self, _id_reservation, _rendu) -> bool:
        return True # modification réussie
    

    def reservations_get_en_cours_by_code_adherent(self, _code_adherent):
        lesReservations:list = self.reservations_get_all_by_code_adherent(_code_adherent)
        lesResEnCours:list = []
        uneReservation:Reservation
        for uneReservation in lesReservations:
            if( (uneReservation.date_heure_fin >= datetime.now() and uneReservation.rendu == True) or uneReservation.rendu == False):
                lesResEnCours.append(uneReservation)
        return lesResEnCours
    

    def reservations_get_retards_by_code_adherent(self, _code_adherent):
        lesReservations:list = self.reservations_get_all_by_code_adherent(_code_adherent)
        lesResEnRetard:list = []
        uneReservation:Reservation
        for uneReservation in lesReservations:
            if(uneReservation.date_heure_fin < datetime.now() and uneReservation.rendu == False):
                lesResEnRetard.append(uneReservation)
        return lesResEnRetard
    

    def reservations_get_retards_all(self):
        lesReservations = self.reservations_get_all()
        lesRetards:list = []
        uneReservation:Reservation
        for uneReservation in lesReservations:
            if(uneReservation.date_heure_fin < datetime.now() and uneReservation.rendu == False):
                lesRetards.append(uneReservation)
        return lesRetards