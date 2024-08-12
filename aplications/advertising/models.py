from aplications import db


class Advertising(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    image = db.Column(db.LargeBinary)
    video_url = db.Column(db.String(120))
    person_id = db.Column(
        db.Integer, db.ForeignKey('person.id'), nullable=True)
    persons = db.relationship(
        'Person', backref=db.backref('advertisings', lazy=True))
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Advertising {self.username}>'
