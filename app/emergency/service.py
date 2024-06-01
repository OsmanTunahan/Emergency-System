from datetime import datetime
from app import db
from app.emergency.init.model import EmergencyLogModel
from app.utils.notifications import NotificationService

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
        EmergencyService.notify_emergency(log_entry)
        return log_entry.id

    @staticmethod
    def get_user_logs(user_id):
        return EmergencyLogModel.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def notify_emergency(log_entry):
        message = (
            f"🔴 <b>Acil Durum Bildirimi</b> 🔴\n"
            f"🌐 IP Adresi: {log_entry.data.get('ip_address')}\n"
            f"📍 Konum: {log_entry.data.get('location')}\n"
            f"⚠️ Öncelik: {log_entry.severity}\n"
            f"📝 Açıklama: {log_entry.data.get('description')}\n"
        )

        # Telegram
        NotificationService.send_telegram_message(message)
        
        # Discord Webhook
        NotificationService.send_discord_message(message)