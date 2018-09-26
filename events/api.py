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

    @staticmethod
    def get_complete_data(data):
        name = data.get('name')
        date = data.get('event_date')
        event_type = data.get('event_type')
        location = data.get('event_location')

        return name, date, event_type, location

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

        # Insert a new event
        if data.get('type') == "INSERT":
            name, date, event_type, location = self.get_complete_data(data)

            if name is None or date is None or event_type is None or location is None:
                response = "Couldnt perform action: Missing data"
            else:
                response = EVENTS.insert_event(name, date, event_type, location)

        # Delete an event
        elif data.get('type') == "DELETE":
            name = data.get('name')

            if name is None:
                response = "Couldnt perfomr action: Missing data"
            else:
                response = EVENTS.delete_event(name)

        # Get the events
        elif data.get('type') == "READ":
            name, date, event_type, location = self.get_complete_data(data)

            if name is None and date is None and event_type is None and location is None:
                response = EVENTS.read_all()


        # elif data.get('type') == "UPDATE":
        #     name, date, event_type, location = self.get_complete_data(data)
        #
        #     if name is None:
        #         response = "Couldnt perfomr action: Missing data"
        #     else:
        #         #response = EVENTS.update_event(name)
        #         print("hisl")

        return jsonify({
            'events': response
        }), 201
