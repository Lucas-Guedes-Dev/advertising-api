from flask import Blueprint
from aplications.auth.view import Auth

auth_bp = Blueprint('auth', __name__)

auth_view = Auth.as_view('auth_api')
auth_bp.add_url_rule('/login', view_func=auth_view, methods=['POST'])