import os, yaml

from src.classes.CDataHandler import DataHandler

from src.classes.CAdherent import Adherent
from src.classes.CAuteur import Auteur
from src.classes.CEditeur import Editeur
from src.classes.CFormat import Format
from src.classes.CLivre import Livre
from src.classes.CReservation import Reservation

class MockHandler(DataHandler):
    """
    Classe héritant de DataHandler.
    Permet d'interagir avec des données de test, configurables à l'aide des fichiers du répertoire 'config/database_filler'.
    """

    def __init__(self):
        super().__init__()

        self.data:list = {} # jdd actif
        self.jdd:list = {} # données des fichiers lus
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
                    self.jdd[nomModele] = data
                    print(f"<DatabaseFiller> Fichier '{nom}' valide et ajouté en tant que fichier de remplissage.")
                else:
                    print(f"<DatabaseFiller> Fichier '{nom}' ignoré : aucune donnée à insérer.")

        print(self.jdd)
        print("<DatabaseFiller> Chargement des fichiers terminé.")



    def adherents_get_by_code(self, code:str) -> Adherent:
        return None

    def auteurs_get_by_id(self, id:int) -> Auteur:
        return None

    def editeurs_get_by_id(self, id:int) -> Editeur:
        return None

    def formats_get_by_id(self, id:int) -> Format:
        return None

    def livres_get_by_isbn(self, code:str) -> Livre:
        return None