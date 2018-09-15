""" EventsAPI """
import logging
from flask.views import MethodView
from flask import jsonify, request

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

        data = request.json
        self.logger.info("########## Events API Called")
        self.logger.info(data)

        return jsonify({
            'events': "Events"
        }), 201
