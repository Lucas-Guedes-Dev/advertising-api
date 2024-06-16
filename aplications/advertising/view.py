from flask import jsonify, request
from flask.views import MethodView
from aplications.advertising.controllers.advertising import CAdvertising


class Advertising(MethodView):
    def post(self):
        data = request.get_json()

        return CAdvertising().formating_create_advertising(data)
