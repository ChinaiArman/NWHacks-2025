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

from exceptions import InvalidEmailAddress, EmailAddressAlreadyInUse, ClassroomNotFound, UserNotFound, Unauthorized

# DATABASE CLASS
class Database:
    """
    """
    def __init__(self, db):
        """
        """
        self.db = db

    # USER METHODS
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
    
    # CLASSROOM METHODS
    def get_student_classrooms(self, student_id):
        """
        """
        classrooms = self.db.session.query(Classroom).join(classroom_students).filter(classroom_students.c.student_id == student_id).all()
        return classrooms
    
    def get_teacher_classrooms(self, teacher_id):
        """
        """
        classrooms = self.db.session.query(Classroom).filter(Classroom.teacher_id == teacher_id).all()
        return classrooms
    
    def create_classroom(self, name, teacher_id, image_url, join_code):
        """
        """
        classroom = Classroom(name=name, image_url=image_url, join_code=join_code, teacher_id=teacher_id)
        self.db.session.add(classroom)
        self.db.session.commit()
        return classroom
    
    def get_classroom_by_join_code(self, join_code):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.join_code == join_code).first()
        if not classroom:
            raise ClassroomNotFound()
        return classroom
    
    def add_student_to_classroom(self, student_id, classroom_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        student = self.db.session.query(User).filter(User.id == student_id).first()
        if not student:
            raise UserNotFound()
        if student in classroom.students or student.id == classroom.teacher_id:
            raise Unauthorized()
        classroom.students.append(student)
        self.db.session.commit()
        return classroom
    
    def get_classroom_by_id(self, classroom_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        return classroom
    
    def delete_classroom(self, classroom_id, teacher_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if classroom.teacher_id != teacher_id:
            raise Unauthorized()
        self.db.session.delete(classroom)
        self.db.session.commit()
        return classroom
    
    def leave_classroom(self, student_id, classroom_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        student = self.db.session.query(User).filter(User.id == student_id).first()
        if not student:
            raise UserNotFound()
        if student not in classroom.students:
            raise Unauthorized()
        classroom.students.remove(student)
        self.db.session.commit()
        return classroom