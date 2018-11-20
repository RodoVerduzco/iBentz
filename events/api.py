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
        """ get
        Handle the get request

        Returns:
            json: Return the news then accessed
        """
        return jsonify({'events': 'Events API'}), 200

    @staticmethod
    def get_complete_data(data):
        """ get_complete_data
        Retrieve the complete data from the json
        categories: MUSICA, DEPORTE, ARTE, CINE, LITERATURA, TEATRO
        """
        name = data.get('name')
        image = data.get('image')
        date = data.get('event_date')
        max_part = data.get('max_participants')
        location = data.get('event_location')
        description = data.get('description')
        info = data.get('info')
        event_type = data.get('category')
        status = data.get('status')
        num_registered = 0

        return name, image, date, max_part, location, description, \
               info, event_type, status, num_registered

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

            # Retrieve all the data
            name, image, date, max_part, location, description, \
            info, event_type, status, num_registered = self.get_complete_data(data)

            if name is None or date is None or event_type is None or location is None:
                response = "Couldnt perform action: Missing data"
            else:
                response = EVENTS.insert_event(name, image, date, max_part, location, description,
                                               info, event_type, status, num_registered)

        # Delete an event
        elif data.get('type') == "DELETE":
            name = data.get('name')

            if name is None:
                response = "Couldnt perfomr action: Missing data"
            else:
                response = EVENTS.delete_event(name)

        # Get the events
        elif data.get('type') == "READ":

            # Retrieve all the data
            name, image, date, max_part, location, description, \
            info, event_type, status, num_registered = self.get_complete_data(data)

            if ((name is None) and (date is None) and (event_type is None) and (location is None)):
                response = EVENTS.read_all()
            elif date is not None:
                response = EVENTS.search_date(date, location, event_type, name)
            elif location is not None:
                response = EVENTS.search_location(location, event_type, name)
            elif event_type is not None:
                response = EVENTS.search_type(event_type)
            elif name is not None:
                response = EVENTS.search_name(name)


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
