from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from aplications.person.controllers.person import CPerson


class Person(MethodView):
    def __init__(self):
        super().__init__()

        self.controller_person = CPerson()

    @jwt_required()
    def post(self):
        data = request.get_json()
        print(data)
        create_person = self.controller_person.create_person(data)

        if create_person['success']:
            return jsonify(create_person), 200
        else:
            return jsonify(create_person), 409

    @jwt_required()
    def get(self):
        params = request.args.to_dict()
        person_id = params.get('id')
        person_cpf_cnpj = params.get('cpf_cnpj')

        filter_type = None

        if params.get('is_client'):
            filter_type = 'clients'
        elif params.get('is_employee'):
            filter_type = 'employees'
        elif params.get('is_driver'):
            filter_type = 'drivers'
        else:
            filter_type = 'all'

        person_list = self.controller_person.get_person_by_filter(
            filter_type, person_cpf_cnpj, person_id)

        return jsonify(person_list), 200

    @jwt_required()
    def put(self):
        params = request.args.to_dict()
        person_id = params.get('id')
        data = request.get_json()
        update_person = self.controller_person.update_person_by_id(
            person_id, data)

        if update_person:
            return jsonify({'success': True}), 200
        else:
            return jsonify({'success': False}), 409
