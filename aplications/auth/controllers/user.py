from aplications.auth.instructions.user import IUser
from flask import jsonify


class CUser(IUser):
    def __init__(self):
        super().__init__()

    def formating_create_user(self, user_dict):
        create = self.create_user(user_dict)

        if create['success']:
            return jsonify(create), 200
        else:
            return jsonify(create), 409
