"""
"""

# IMPORTS
from db_config import db
from models.User import User
from models.ClassroomStudents import classroom_students

# CLASSROOM DATA CLASS
class Classroom(db.Model):
    __tablename__ = 'classrooms'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    join_code = db.Column(db.String(50), unique=True, nullable=False)
    
    # Foreign Keys
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    teacher = db.relationship("User", back_populates="classrooms", foreign_keys=[teacher_id])
    students = db.relationship("User", secondary=classroom_students, back_populates="classrooms_as_student")
    lectures = db.relationship("Lecture", back_populates="classroom")
