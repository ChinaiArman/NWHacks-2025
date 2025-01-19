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

class ClassroomNotFound(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Classroom not found")

class UserNotFound(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("User not found")

class Unauthorized(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Unauthorized")

class PlaybookNotFound(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Playbook not found")

class PlayNotFound(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Play not found")

class LectureNotFound(Exception):
    """
    """
    def __init__(self):
        """
        """
        super().__init__("Lecture not found")