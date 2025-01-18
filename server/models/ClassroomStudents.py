"""
"""

# IMPORTS
from db_config import db


# CLASSROOM STUDENTS DATA CLASS
classroom_students = db.Table(
    'classroom_students',
    db.Column('classroom_id', db.Integer, db.ForeignKey('classrooms.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)