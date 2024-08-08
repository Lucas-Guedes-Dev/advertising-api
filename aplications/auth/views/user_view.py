from flask import jsonify, request
from flask.views import MethodView
from aplications.auth.controllers.user import CUser


class UserView(MethodView):
    def __init__(self):
        super().__init__()

    def post(self):
        data = request.get_json()
        return CUser().formating_create_user(data)

    def get(self):
        params = request.args.to_dict()
        return CUser().get_user_with_param(params.get('id_user'), params.get('username'))
