""" Views form flask framework """
from flask import Blueprint
from users.api import UsersAPI

USERS_APP = Blueprint('users_app', __name__)
USERS_VIEW = UsersAPI.as_view('users_api')

USERS_APP.add_url_rule('/users/',
                        view_func=USERS_VIEW,
                        methods=['GET', ])

USERS_APP.add_url_rule('/users/search_users',
                        view_func=USERS_VIEW,
                        methods=['POST', ])
