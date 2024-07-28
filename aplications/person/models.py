from aplications import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cpf_cnpj = db.Column(db.String(16), unique=True, nullable=True)
    email = db.Column(db.String(80))
    phone = db.Column(db.String(25))
    road = db.Column(db.String(120))
    state = db.Column(db.String(60))
    city = db.Column(db.String(60))
    number = db.Column(db.String(7))
    neighborhood = db.Column(db.String(60))
    is_employee = db.Column(db.Boolean, default=False)
    is_client = db.Column(db.Boolean, default=False)
    is_driver = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('persons', lazy=True))

    def __repr__(self):
        return f'<Person {self.name}>'
