from aplications import db
from aplications.auth.models import User
from sqlalchemy.exc import IntegrityError


class IUser():
    def __init__(self):
        super().__init__()

    def get_user_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_all_users(self):
        return User.query.all()

    def create_user(self, user_dict):
        new_user = User(
            username=user_dict.get('username'),
            password=user_dict['password'],
            is_admin=user_dict.get('is_admin'),
            active=user_dict.get('active'),
        )
        if user_dict.get('password'):
            try:
                db.session.add(new_user)
                db.session.commit()
                return {'success': True}
            except IntegrityError as e:
                return {'success': False, 'error': str(e)}

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
