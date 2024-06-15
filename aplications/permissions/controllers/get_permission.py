from aplications import db
from aplications.permissions.models import PermissionsModel
from flask import jsonify

class GetPermissions:
    def __init__(self):
        self.olamundo = "tetadecavalo"
        
    def get_id(self, id):
        
        query_perm = db.session.query(PermissionsModel).filter(PermissionsModel.id==id).all()
        print(query_perm)
        return jsonify({
            "id" : id
        }), 200
        
    def get_all(self):
        return jsonify({
            "teste": 'teste'
        }), 200