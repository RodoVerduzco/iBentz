""" Application.py """
import logging
from flask import Flask
from flask_cors import CORS

def create_app(config, debug=False, testing=False, config_overrides=None):
    """
    Create all the API configurations, this handle the database connection, the routes
    initialization, the SSL certificate and all the error handlers

    Arguments
        name: config,
        type: module,
        summary: This file is in charge of the database connections and credentials

        name: debug,
        type: boolean,
        summary: It set the environment as development phase or not

        name: testing,
        type: boolean,
        summary: It set the environment as testing

        name: config_overrides,
        type: boolean,
        summary: This will say if the initial config is other rather the initial one

    Call
        create_app('module', True, False, False)

    Response
        None
    """

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config)

    # Initialize enviroment
    app.debug = debug
    app.testing = testing

    # Apply configurations overrides
    if config_overrides:
        app.config.update(config_overrides)

    # Initialize logs
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    from users.views import USERS_APP

    app.register_blueprint(USERS_APP, url_prefix='/api/v1')

    return app
