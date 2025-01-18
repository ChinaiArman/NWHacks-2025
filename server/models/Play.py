"""
"""

# IMPORTS
from db_config import db


# PLAY DATA CLASS
class Play(db.Model):
    __tablename__ = 'plays'
    
    id = db.Column(db.Integer, primary_key=True)
    play_type = db.Column(db.String(100), nullable=False)
    play_prompt = db.Column(db.Text, nullable=False)
    play_answer = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    
    # Foreign Keys
    playbook_id = db.Column(db.Integer, db.ForeignKey('playbooks.id'), nullable=False)
    
    # Relationships
    playbook = db.relationship("Playbook", back_populates="plays")
    answers = db.relationship("PlayAnswer", back_populates="play", cascade="all, delete-orphan")