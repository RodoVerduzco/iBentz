""" Views form flask framework """
from flask import Blueprint
from events.api import EventsAPI

EVENTS_APP = Blueprint('users_app', __name__)
EVENTS_VIEW = EventsAPI.as_view('events_api')

EVENTS_APP.add_url_rule('/events/',
                        view_func=EVENTS_VIEW,
                        methods=['GET', ])

EVENTS_APP.add_url_rule('/events/search_events',
                        view_func=EVENTS_VIEW,
                        methods=['POST', ])
