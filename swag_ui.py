from models.Message import MessageSchema
from flasgger import APISpec, Schema, Swagger, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin


def swag_init(app):
    # Create an APISpec
    spec = APISpec(
        title='Messaging App',
        version='1.0',
        openapi_version='2.0',
        plugins=[FlaskPlugin(), MarshmallowPlugin()]
    )

    template = spec.to_flasgger(
        app,
        definitions=[MessageSchema],
    )

    # set the UIVERSION to 3
    app.config['SWAGGER'] = {'uiversion': 3}

    # start Flasgger using a template from apispec
    swag = Swagger(app, template=template)
    return swag
