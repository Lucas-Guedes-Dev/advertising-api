from aplications import db
from aplications.advertising.models import Advertising
from sqlalchemy.exc import IntegrityError


class IAdvertising:
    def __init__(self):
        super().__init__()

    def get_advertising_by_id(self, id):
        return Advertising.query.filter_by(id=id).first()

    def get_all_advertising(self):
        return Advertising.query.all()

    def create_advertising(self, advertising_dict):
        try:
            new_advertising = Advertising(
                name=advertising_dict.get('name'),
                description=advertising_dict.get('description'),
                image=advertising_dict.get('image'),
                video_url=advertising_dict.get('video_url'),
                person_id=advertising_dict.get('person_id'),
                active=advertising_dict.get('active')
            )

            db.session.add(new_advertising)
            db.session.commit()

            return {'success': True}
        except IntegrityError as e:
            return {'success': False, 'error': str(e)}
