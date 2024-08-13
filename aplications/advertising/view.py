from flask import jsonify, request
from flask.views import MethodView
from aplications.advertising.controllers.advertising import CAdvertising
from flask_jwt_extended import jwt_required


class Advertising(MethodView):
    def __init__(self):
        super().__init__()

        self.controller = CAdvertising()

    @jwt_required()
    def get(self):
        params = request.args.to_dict()

        return self.controller.get_with_filter_advertising(params)

    @jwt_required()
    def post(self):
        data = request.get_json()
        return self.controller.formating_create_advertising(data)
