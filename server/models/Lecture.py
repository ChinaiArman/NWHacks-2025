"""
"""

# IMPORTS
from db_config import db

# CLASSROOM DATA CLASS
class Lecture(db.Model):
    __tablename__ = 'lectures'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=False)
    
    # Foreign Keys
    classroom_id = db.Column(db.Integer, db.ForeignKey('classrooms.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    playbook_id = db.Column(db.Integer, db.ForeignKey('playbooks.id'), nullable=True)
    
    # Relationships
    classroom = db.relationship("Classroom", back_populates="lectures")
    teacher = db.relationship("User", back_populates="lectures", foreign_keys=[teacher_id])
    playbook = db.relationship("Playbook", back_populates="lectures")