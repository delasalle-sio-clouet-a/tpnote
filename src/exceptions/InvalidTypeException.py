class InvalidTypeException(Exception):
    """
    Exception pour une donnée envoyée dans un type incorrect (ex: string au lieu de int, avec le string ne pouvant pas être transformé en int)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)