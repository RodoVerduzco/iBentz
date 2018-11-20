""" Views form flask framework """
from flask import Blueprint
from assign_events.api import AssignAPI

ASSIGN_APP = Blueprint('assign_app', __name__)
ASSIGN_VIEW = AssignAPI.as_view('assign_api')

ASSIGN_APP.add_url_rule('/assign_events/',
                        view_func=ASSIGN_VIEW,
                        methods=['GET', ])

ASSIGN_APP.add_url_rule('/assign_events/assign',
                        view_func=ASSIGN_VIEW,
                        methods=['POST', ])
