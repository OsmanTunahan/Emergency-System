from datetime import datetime
from app import db
from app.emergency.init.model import EmergencyLogModel

class EmergencyService:
    logs = []

    @staticmethod
    def classify_emergency(data):
        # TODO: For this, a schema file will be opened and priorities will be defined for all possible emergencies
        if 'violence' in data['description'].lower():
            return 'HIGH'
        elif 'theft' in data['description'].lower():
            return 'MEDIUM'
        else:
            return 'LOW'

    @staticmethod
    def log_emergency(data, severity, user_id):
        log_entry = EmergencyLogModel(user_id=user_id, data=data, severity=severity)
        db.session.add(log_entry)
        db.session.commit()
        return log_entry.id

    @staticmethod
    def get_user_logs(user_id):
        return EmergencyLogModel.query.filter_by(user_id=user_id).all()