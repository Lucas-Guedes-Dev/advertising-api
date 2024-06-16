from flask import jsonify, request
from flask.views import MethodView
from aplications.auth.controllers.login import Login


class Auth(MethodView):
    def __init__(self):
        super().__init__()

        self.controller_login = Login()

    def post(self):
        data = request.get_json()
        access_dict = self.controller_login.make_login(
            data.get('username'), data.get('password'))

        if access_dict['access']:
            return jsonify(access_dict), 200
        else:
            return jsonify(access_dict), 401
