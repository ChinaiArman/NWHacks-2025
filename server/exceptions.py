"""
"""

class IncorrectPassword(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Incorrect password")

class InvalidOneTimeCode(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Invalid one-time code")