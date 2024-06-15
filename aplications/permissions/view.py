from flask import jsonify, request
from flask.views import MethodView
from aplications.permissions.models import PermissionsModel
from aplications.permissions.controllers.create_permission import CreatePermission
from aplications.permissions.controllers.get_permission import GetPermissions

class Permissions(MethodView):
    def get(self, id=None):
        if id:
            return GetPermissions().get_id(id)
        else:
            return GetPermissions().get_all()

    def post(self):
        json_obj = request.get_json()
        perm_obj = PermissionsModel()
        perm_obj.name = json_obj['name']

        try:    
            # Exemplo que instacia fora de variavel pois não tem retorno
            CreatePermission().create(perm_obj)
            return jsonify({'message': 'permissão criada com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
        