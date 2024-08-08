from flask import Blueprint
from aplications.advertising.view import Advertising

advertising_bp = Blueprint('advertising', __name__)

advertising_view = Advertising.as_view('advertising_api')
advertising_bp.add_url_rule(
    '/create', view_func=advertising_view, methods=['POST'])
advertising_bp.add_url_rule(
    '/list', view_func=advertising_view, methods=['GET'])
