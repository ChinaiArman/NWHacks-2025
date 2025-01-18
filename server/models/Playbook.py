"""
"""

# IMPORTS
from db_config import db


# PLAY BOOK DATA CLASS
class PlayBook(db.Model):
    __tablename__ = 'playbooks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    
    # Foreign Keys
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    teacher = db.relationship("User", back_populates="playbooks")
    plays = db.relationship("Play", back_populates="playbook", cascade="all, delete-orphan")
    lectures = db.relationship("Lecture", back_populates="playbook")