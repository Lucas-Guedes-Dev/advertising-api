from aplications.auth.instructions.user import IUser

from flask_jwt_extended import create_access_token
from datetime import timedelta
import bcrypt


class Login(IUser):
    def __init__(self):
        super().__init__()

    def make_login(self, username, password):
        user = self.get_user_by_username(username)

        if user and self.check_password(password, user.password):
            access_token = create_access_token(
                identity=user.id, expires_delta=timedelta(minutes=30))
            return {"access": True, "access_token": f"Bearer {access_token}"}
        return {"access": False, "access_token": None}

    def hash_password(self, password):
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def check_password(self, password, hashed_password):
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode('utf-8')

            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

        return False
