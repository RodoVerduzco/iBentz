""" AssignAPI """
import logging
from flask.views import MethodView
from flask import jsonify, request
from assign_events.assignation import *

class AssignAPI(MethodView):
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
        return jsonify({'assign': 'Assign API'}), 200


    def post(self):
        """ Handle the post request
        Call the api when the post request is entered by
        the user

        Returns:
            json: Response from the server with the news
                  result message
        """

        data = request.json
        self.logger.info("########## Assign Events API Called")
        self.logger.info(data)

        # Insert a new event
        if data.get('action') == "ASSIGN":
            data.get('user')
            response = "assigned"

        return jsonify({
            'events': response
        }), 201
