"""
"""

# IMPORTS

from models.Classroom import Classroom
from models.ClassroomStudents import classroom_students
from models.Lecture import Lecture
from models.Play import Play
from models.Playbook import Playbook
from models.PlayAnswer import PlayAnswer
from models.User import User

from exceptions import InvalidEmailAddress
from exceptions import EmailAddressAlreadyInUse

# DATABASE CLASS
class Database:
    """
    """
    def __init__(self, db):
        """
        """
        self.db = db

    def get_user_by_email(self, email):
        """
        """
        user = self.db.session.query(User).filter(User.email == email).first()
        if not user:
            raise InvalidEmailAddress()
        return user
    
    def create_user(self, username, email, password):
        """
        """
        if self.db.session.query(User).filter(User.email == email).first():
            raise EmailAddressAlreadyInUse()
        # TODO: Implement email verification with one time code + email service.
        user = User(username=username, email=email, password=password, verification_code=None, reset_code=None, is_verified=True)
        self.db.session.add(user)
        self.db.session.commit()
        return user
        