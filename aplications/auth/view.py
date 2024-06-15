from flask import jsonify, request
from flask.views import MethodView

class Auth(MethodView):    
    def post(self):
        data = request.get_json()
        return jsonify({'message': 'POST request received', 'data': data}), 201
