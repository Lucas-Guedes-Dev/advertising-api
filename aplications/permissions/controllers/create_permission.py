from aplications import db
from aplications.permissions.models import PermissionsModel

class CreatePermission():
    def create(self, perm_obj: PermissionsModel):
        new_register = PermissionsModel(name=perm_obj.name)
    
        db.session.add(new_register)
        db.session.commit()