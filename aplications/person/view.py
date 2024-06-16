from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required


class Person(MethodView):
    @jwt_required()
    def post(self):
        data = request.get_json()

        return jsonify({'message': 'POST request received', 'data': data}), 200
