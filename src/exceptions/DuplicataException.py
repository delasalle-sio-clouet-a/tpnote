class DuplicataException(Exception):
    """
    Exception pour une donnée ne respectant pas un format attendu (caractères non autorisés, mauvaise longueur, ...)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)