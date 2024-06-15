import bcrypt


class Login():
    def __init__(self):
        pass

    def make_login(self):
        pass

    def hash_password(self, password):
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
