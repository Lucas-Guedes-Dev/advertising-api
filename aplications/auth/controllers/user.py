from aplications.auth.instructions.user import IUser
from aplications.auth.models import User

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

    def get_user_with_param(self, id_user, username):
        if id_user and username:
            return jsonify({'message': 'Não é possivel filtrar com username e user_id na mesma requisição'}), 401

        response_list = []
        list_user = []

        if id_user:
            list_user = CUser().get_user_by_id(id_user)

        if username:
            list_user = CUser().get_user_by_username(username)

        if not id_user and not username:
            list_user = CUser().get_all_users()

        for user in list_user:
            response_list.append(user)

        return jsonify(response_list), 200

    def create_object_json(self, person: User):
        return {
            'id_user': person.id,
            'username': person.username,
            'active': person.active
        }
