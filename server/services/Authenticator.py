"""
"""

# IMPORTS
import bcrypt
import secrets

from exceptions import IncorrectPassword, InvalidOneTimeCode

# AUTHENTICATOR CLASS
class Authenticator:
    """
    """
    def __init__(self):
        """
        """
        pass

    def encrypt_password(self, password: str) -> str:
        """
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def verify_password(self, password: str, hashed_password: str) -> bool:
        """
        """
        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            raise IncorrectPassword()
        return True
    
    def generate_one_time_code(self) -> str:
        """
        """
        return secrets.token_hex(3)
    
    def verify_code(self, user_code: str, server_code: str) -> bool:
        """
        """
        if user_code != server_code or not user_code:
            raise InvalidOneTimeCode()
        return True