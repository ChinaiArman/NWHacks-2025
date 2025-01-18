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

class InvalidEmailAddress(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Invalid email address")

class EmailAddressAlreadyInUse(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Email already exists")

class MissingFields(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Missing fields")