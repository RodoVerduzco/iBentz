""" EventsAPI """
import logging
from flask.views import MethodView
from flask import jsonify, request
import users.handle_users as USERS

class UsersAPI(MethodView):
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
        return jsonify({'users': 'Users API'}), 200

    

    def post(self):
        """ Handle the post request

        Call the api when the post request is entered by
        the user

        Returns:
            json: Response from the server with the news
                  result message
        """
        response = "Null"
        USERS.send_mails()
        data = request.json
        self.logger.info("########## Events API Called")
        self.logger.info(data)

        testing_param = data.get('type')

        if testing_param == "READ_ALL": #GET ALL REGISTERED USERS
            response = USERS.read_all()
            USERS.send_mails()
            return jsonify({'users':response})

        elif testing_param == "DELETE_EMAIL": #DELETE AN USER BY EMAIL
            if data.get('email') is None:
                return jsonify({"users": "MISSING_DATA"})
            return jsonify({"users":USERS.delete_user(data.get('email'))})

        elif testing_param == "VALIDATE": #VALIDATION OF A USER
            usr = data.get('username')
            pwd = data.get('password')
            if usr is None or pwd is None:
                return jsonify({"users": "MISSING_DATA"})
            return jsonify({"users": USERS.validate_user(usr,pwd)})

        elif testing_param == "GET_USER_DATA": #GET DATA FROM ONE USER
            usr = data.get('username')
            if usr is None: return jsonify({"user": "MISSING_DATA"})
            return jsonify({"user": USERS.search_username(usr)})

        elif testing_param =="CREATE_PREFERENCES": #ADD INITIAL SPREFERENCES
            usr = data.get('username')
            parameters = data.get('preferences')
            if usr is None or parameters is None:
                return "MISSING_DATA"
            return jsonify({"user":USERS.create_preferences(usr,parameters)})

        elif testing_param == "ADD_PREFERENCES": #ADD PREFS
            usr = data.get('username')
            parameters = data.get('preferences')
            if usr is None or parameters is None:
                return "MISSING_DATA"
            return jsonify({"user": USERS.add_new_preference(usr,parameters)})

        elif testing_param == "UPDATE_PREFERENCES": #ADD PREFS
            usr = data.get('username')
            parameters = data.get('preferences')
            if usr is None or parameters is None:
                return "MISSING_DATA"
            return jsonify({"user": USERS.update_preferences(usr,parameters)})

        elif testing_param == "DELETE_PREFERENCES":
            usr = data.get('username')
            parameters = data.get('preferences')
            if usr is None or parameters is None:
                return "MISSING_DATA"
            return jsonify({"user": USERS.delete_preferences(usr,parameters)})

        elif testing_param == "GET_PARAMETER":
            usr = data.get('username')
            param = data.get('param')
            if usr is None or param is None:
                return "MISSING_DATA"
            response = {"user": USERS.get_parameter(usr,param)}

        elif testing_param == "GET_VARIOUS_PARAMS":
            usr = data.get('username')
            parameters = data.get('param')
            if usr is None or parameters is None:
                return "MISSING_DATA"
            return jsonify({"user": USERS.get_various_parameters(usr,parameters)})

        elif testing_param == "ADD_EVENT":
            usr = data.get('username')
            event_id = data.get('event_id')

            if usr is None and event_id is None:
                response = "MISSING_DATA"
            else:
                response = USERS.add_event(usr, event_id)
        
        elif testing_param == "MODIFY_USER":
            usr = data.get('username')
            email = data.get('email')
            password = data.get('password')
            age = data.get('age')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            sex = data.get('sex')
            birthday = data.get('birthday')
            location = data.get('location')
            if usr and email and password and age and first_name and last_name and sex and birthday and location:
                response = "MISSING_DATA"
            
            response = USERS.modify_user(usr, email, password, age, first_name, last_name, sex, birthday, location)

        elif testing_param == ('SEARCH_TYPE'):
            user_type = data.get('user_type')
            if user_type is None:
                return jsonify({"user":"MISSING_DATA"})
            return jsonify({"user": USERS.search_by_type(user_type)})
        
        elif testing_param == 'GET_ORG_EVENTS':
            usr = data.get('username')
            stat = data.get('status')
            if usr is None or stat is None:
                response = "MISSING_DATA"
            
            response = USERS.get_org_event(usr,stat)
        
        elif testing_param == "GET_USER_RECOMMENDATIONS":
            usr = data.get('username')
            if usr is None:
                response = "MISSING_DATA"
            
            response = USERS.get_user_recommendations(usr)

        elif testing_param == "INSERT_USER":
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            age = data.get('age')
            user_type=data.get('user_type')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            sex = data.get('sex')
            birthday = data.get('birthday')
            location = data.get('location')

            if username is None or email is None or password is None or age is None or first_name is None or last_name is None or sex is None or birthday is None or location is None or user_type is None:
                response = "MISSING_DATA"
            else:
                response = USERS.insert_user(username, email, user_type, password, age, first_name, last_name, sex, birthday, location)

        return jsonify({
            'users': response
        }), 201
