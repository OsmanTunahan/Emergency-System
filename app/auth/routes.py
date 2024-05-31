from flask import Blueprint, request, jsonify
from app.auth.service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = AuthService.login(data['username'], data['password'])
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    success = AuthService.register(data['username'], data['password'])
    if success:
        return jsonify({'message': 'User registered successfully'}), 201
    return jsonify({'message': 'User already exists'}), 409