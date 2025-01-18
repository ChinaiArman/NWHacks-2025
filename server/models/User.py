"""
"""

# IMPORTS
from db_config import db

# CLASSROOM DATA CLASS
class User(db.Model):
    """
    """
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    verification_code = db.Column(db.String(50))
    reset_code = db.Column(db.String(50))
    
    # Relationships
    classrooms = db.relationship("Classroom", back_populates="teacher", foreign_keys="Classroom.teacher_id")
    lectures = db.relationship("Lecture", back_populates="teacher", foreign_keys="Lecture.teacher_id")
    classrooms_as_student = db.relationship("Classroom", secondary="classroom_students", back_populates="students")
    playbooks = db.relationship("Playbook", back_populates="teacher")
    play_answers = db.relationship("PlayAnswer", back_populates="student")
