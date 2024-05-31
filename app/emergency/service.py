from datetime import datetime

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
        log_entry = {
            'id': len(EmergencyService.logs) + 1,
            'user_id': user_id,
            'timestamp': datetime.utcnow(),
            'data': data,
            'severity': severity
        }
        EmergencyService.logs.append(log_entry)
        return log_entry['id']

    @staticmethod
    def get_user_logs(user_id):
        return [log for log in EmergencyService.logs if log['user_id'] == user_id]