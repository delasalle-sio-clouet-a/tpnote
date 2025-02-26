import yaml

class Config:
    def __init__(self, emplacementFichierConfig:str):
        # valeurs par défaut en cas d'echec du chargement de la config
        self.logLevel:str = "INFO"

        self.dbServer:str = ""
        self.dbBase:str = ""
        self.dbUser:str = ""
        self.dbPassword:str = ""

        self.tokenDuration:int = 300 # durée des tokens en secondes

        self.urlApi:str = ""

        self.remplissage:bool = False
        self.jeuTest:bool = False

        # lire le fichier de configuration
        
        with open(emplacementFichierConfig, "r") as fichierConfig:
           
            config = yaml.load(fichierConfig, Loader=yaml.FullLoader)

            self.logLevel = config.get("logLevel", "INFO")

            dbConfig:dict = config.get("database", {})
            self.dbDialect = dbConfig.get("dialect", "")
            self.dbServer = dbConfig.get("server", "")
            self.dbBase = dbConfig.get("base", "")
            self.dbUser = dbConfig.get("username", "")
            self.dbPassword = dbConfig.get("password", "")
            
            self.urlApi = config.get("urlApi", "")

            fillerConfig:dict = config.get("database_filler", {})
            self.remplissage = bool(fillerConfig.get("remplissage", False))
            self.jeuTest = bool(fillerConfig.get("jeuTest", False))