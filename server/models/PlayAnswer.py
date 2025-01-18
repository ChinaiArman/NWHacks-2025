"""
"""

# IMPORTS
from db_config import db


# PLAY ANSWER DATA CLASS
class PlayAnswer(db.Model):
    __tablename__ = 'play_answers'
    
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text, nullable=False)
    
    # Foreign Keys
    play_id = db.Column(db.Integer, db.ForeignKey('plays.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    play = db.relationship("Play", back_populates="answers")
    student = db.relationship("User", back_populates="play_answers")