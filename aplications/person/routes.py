from flask import Blueprint
from aplications.person.view import Person

person_bp = Blueprint('person', __name__)

person_view = Person.as_view('person_api')
person_bp.add_url_rule('/create', view_func=person_view, methods=['POST'])
person_bp.add_url_rule('/list', view_func=person_view, methods=['GET'])
person_bp.add_url_rule('/update',
                       view_func=person_view, methods=['PUT'])
