from flask import Blueprint, request, jsonify
from app.emergency.service import EmergencyService
from app.utils.security import token_required

emergency_bp = Blueprint('emergency', __name__)

@emergency_bp.route('/report', methods=['POST'])
@token_required
def report_emergency(current_user):
    data = request.get_json()
    severity = EmergencyService.classify_emergency(data)
    log_entry = EmergencyService.log_emergency(data, severity, current_user['id'])
    return jsonify({'message': 'Emergency reported', 'ip': data['ip'], 'severity': severity, 'log_id': log_entry}), 201

@emergency_bp.route('/logs', methods=['GET'])
@token_required
def get_logs(current_user):
    logs = EmergencyService.get_user_logs(current_user['id'])
    return jsonify(logs), 200