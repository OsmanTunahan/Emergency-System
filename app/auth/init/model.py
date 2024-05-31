class UserModel:
    users = []

    @classmethod
    def find_by_username(cls, username):
        return next((user for user in cls.users if user['username'] == username), None)

    @classmethod
    def create_user(cls, username, password):
        user = {
            'id': len(cls.users) + 1,
            'username': username,
            'password': password
        }
        cls.users.append(user)
        return user