class UndefinedMethodException(Exception):
    """
    Exception levée lorsqu'une méthode non initialisée à été appellée. (ex: fonctions héritées vides et non redéfinies)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)