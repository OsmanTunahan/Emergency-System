from datetime import datetime
from app import db

class EmergencyLogModel(db.Model):
    __tablename__ = 'emergency_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    
    user = db.relationship('UserModel', back_populates='logs')