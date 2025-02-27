class InvalidIsbnException(Exception):
    """
    Exception pour un isbn invalide (clé incorrecte, mauvaise longueur, caractères non autorisés, ...)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)