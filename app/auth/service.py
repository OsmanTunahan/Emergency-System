import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.config import Config
from app.auth.init.model import UserModel

class AuthService:
    @staticmethod
    def login(username, password):
        user = UserModel.find_by_username(username)
        if user and check_password_hash(user.password, password):
            token = jwt.encode({
                'user_id': user['id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)
            }, Config.JWT_SECRET_KEY, algorithm='HS256')
            return token
        return None

    @staticmethod
    def register(username, password):
        if UserModel.find_by_username(username):
            return False
        hashed_password = generate_password_hash(password)
        UserModel.create_user(username, hashed_password)
        return True
