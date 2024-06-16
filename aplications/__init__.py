from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = 'uploads'

    JWTManager(app)
    Swagger(app, template_file='swagger.yaml')

    db.init_app(app)
    migrate.init_app(app, db)

    from aplications.auth.routes import auth_bp
    from aplications.advertising.routes import advertising_bp
    from aplications.person.routes import person_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(advertising_bp, url_prefix='/advertising')
    app.register_blueprint(person_bp, url_prefix='/person')

    # TODO *** não apague isso, é para debugar melhor a aplicalção quando preciso ***
    # with app.app_context():
    #     print_routes(app)

    return app

# TODO *** use esse metodo para debugar as endpoints que estão registrados ***
# def print_routes(app):
#     for rule in app.url_map.iter_rules():
#         methods = ','.join(sorted(rule.methods))
#         print(f'{rule.endpoint}: {rule.rule} [{methods}]')
