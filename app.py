from flask import Flask, redirect
from API.Message.message_blueprint import *
from API.User.user_blueprint import *
from swag_ui import swag_init
from models.Database import db, ma
from os import environ


def create_app():
    app = Flask(__name__)

    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
        'DATABASE_URL', 'sqlite:///database.sqlite.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # SQLAlchemy and Marshmallow initiation:
    db.init_app(app)
    ma.init_app(app)
    swag_init(app)

    ##### API #####
    # Blueprints registration
    app.register_blueprint(message_blueprint, url_prefix="/api")
    app.register_blueprint(user_blueprint, url_prefix="/api")

    @ app.route("/")
    def index():
        return redirect('/apidocs/')

    return app


##### Main #####
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
