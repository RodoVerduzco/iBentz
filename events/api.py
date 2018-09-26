""" EventsAPI """
import logging
from flask.views import MethodView
from flask import jsonify, request
import events.handle_events as EVENTS

class EventsAPI(MethodView):
    """ Main API Body """
    logger = logging.getLogger(__name__)

    #def __init__(self):
    #    if (request.method != 'GET') and not request.json:
    #        abort(400)

    @staticmethod
    def get():
        """ Handle the get request

        Returns:
            json: Return the news then accessed
        """
        return jsonify({'events': 'Events API'}), 200

    def post(self):
        """ Handle the post request

        Call the api when the post request is entered by
        the user

        Returns:
            json: Response from the server with the news
                  result message
        """
        response = "Null"

        data = request.json
        self.logger.info("########## Events API Called")
        self.logger.info(data)

        if data.get('type') == "INSERT":
            name = data.get('name')
            date = data.get('event_date')
            event_type = data.get('event_type')
            location = data.get('event_location')

            print(name + " " + date + " " + event_type + " " + location + " \n\n\n\n")

            if name is None or date is None or event_type is None or location is None:
                response = "Couldnt perfomr action: Missing data"
            else:
                response = EVENTS.insert_event(name, date, event_type, location)

        return jsonify({
            'events': response
        }), 201
