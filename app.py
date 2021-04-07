from flask import Flask
from API.Message.message_blueprint import *
from API.User.user_blueprint import *
from swag_ui import swag_init
from models.Database import db, ma


def create_app():
    app = Flask(__name__)

    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SQLAlchemy and Marshmallow initiation:
    db.init_app(app)
    ma.init_app(app)
    swag_init(app)

    ##### API #####
    # Blueprints registration
    app.register_blueprint(message_blueprint, url_prefix="/api")
    app.register_blueprint(user_blueprint, url_prefix="/api")

    #######################################
    # from flasgger import APISpec, Schema, Swagger, fields
    # from apispec.ext.marshmallow import MarshmallowPlugin
    # from apispec_webframeworks.flask import FlaskPlugin

    # # Create an APISpec
    # spec = APISpec(
    #     title='Messaging App',
    #     version='1.0',
    #     openapi_version='2.0',
    #     plugins=[FlaskPlugin(), MarshmallowPlugin()]
    # )

    # from models.Message import MessageSchema

    # template = spec.to_flasgger(
    #     app,
    #     definitions=[MessageSchema],
    # )

    # # set the UIVERSION to 3
    # app.config['SWAGGER'] = {'uiversion': 3}

    # # start Flasgger using a template from apispec
    # swag = Swagger(app, template=template)
    #######################################

    return app


##### Main #####
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
