from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from aplications.person.controllers.person import CPerson


class Person(MethodView):
    @jwt_required()
    def post(self):
        data = request.get_json()
        create_person = CPerson().create_person(data)

        if create_person['success']:
            return jsonify(create_person), 200
        else:
            return jsonify(create_person), 409
