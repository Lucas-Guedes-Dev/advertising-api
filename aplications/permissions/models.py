from aplications import db

permissions_users = db.Table(
    'permissions_users',
    db.Column('permission_model_id', db.Integer, db.ForeignKey('permissions_model.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)

    def __repr__(self):
        return f'<Permissions {self.name}>'
