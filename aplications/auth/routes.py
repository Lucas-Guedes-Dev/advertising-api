from flask import Blueprint
from aplications.auth.views.auth_view import Auth
from aplications.auth.views.user_view import UserView

auth_bp = Blueprint('auth', __name__)

auth_view = Auth.as_view('auth_api')
user_view = UserView.as_view('user_api')

auth_bp.add_url_rule('/login', view_func=auth_view, methods=['POST'])
auth_bp.add_url_rule('/user/create', view_func=user_view, methods=['POST'])
auth_bp.add_url_rule('/user/list', view_func=user_view, methods=['GET'])
