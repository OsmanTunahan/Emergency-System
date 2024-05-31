class UserModel:
    users = []

    @classmethod
    def find_by_username(cls, username):
        return next((user for user in cls.users if user['username'] == username), None)

    @classmethod
    def find_by_id(cls, user_id):
        return next((user for user in cls.users if user['id'] == user_id), None)

    @classmethod
    def create_user(cls, username, password):
        user = {
            'id': len(cls.users) + 1,
            'username': username,
            'password': password
        }
        cls.users.append(user)
        return user