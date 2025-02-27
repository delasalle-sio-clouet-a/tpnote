class MissingDataException(Exception):
    """
    Exception levée lorsqu'une donnée n'existe pas ou est manquante (ex: clé étrangère qui ne mène vers rien, livre sans titre, ...)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)