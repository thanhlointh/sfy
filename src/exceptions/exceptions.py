class DataExceptions(Exception):
    """
    Exception raised for error in database
    """
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

