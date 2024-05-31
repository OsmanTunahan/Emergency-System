import jwt
from functools import wraps
from flask import request, jsonify
from app.config import Config
from app.auth.init.model import UserModel

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
            current_user = UserModel.find_by_id(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid or expired'}), 403

        return f(current_user, *args, **kwargs)
    
    return decorated