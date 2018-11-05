""" Handle Events
This program handles the events interactions
"""

import dbhelper.dbhelper as DBHELPER
db = DBHELPER.DBHelper()

def insert_user(username, email, user_type, password, age, first_name, last_name, sex, birthday, location):

    db.collection.users.insert({
        "name": username,
        "email": email,
        "password":password,
        "user_type": user_type,
        "age": age,
        "first_name": first_name,
        "last_name": last_name,
        "sex": sex,
        "birthday": birthday,
        "location": location,
        "preferences": ""
    })
   #db.user_insert(user_name, email, password, age, first_name, last_name, sex, birthday, location)
    return "user inserted successfully"

def delete_email(email):
    """delete_user
    Calls the DBHelper to delete the event into the database
    Args:
        event_name(string): Name of the event
    Returns:
        string: Confirmation Message
    """
    delete_query = {"email": email}
    db.collection.users.delete_one(delete_query)

    return "User " + email + " was deleted"

def validate_user(username, password):

    result =db.collection.users.find_one( {"$or": [{ "$and": [ { "name": username }, { "password": password } ] },
    { "$and": [ { "email": username }, { "password": password } ] } ]}, {"_id":False} )

    print(result)
    if(result is not None):
        return {"user_type":result['user_type']}
    else:
        return {"user_type":"INVALID"}

def delete_user(username):
    """delete_user
    Calls the DBHelper to delete the event into the database
    Args:
        username(string): username of the person
    Returns:
        string: Confirmation Message
    """
    delete_query = {"name": username}
    db.collection.users.delete_one(delete_query)

    return "User " + username + " was deleted"

def read_all():
    """read_all
    Calls the DBHelper to retrieve the complete list of users
    Returns:
        list: List of events
    """
    retrieved_info = list(db.collection.users.find())
    result = []
    for element in retrieved_info:
        result.append({
            "name": element['name'],
            "email": element['email'],
            "password": element['password'],
            "user_type": element['user_type'],
            "age": element['age'],
            "first_name": element['first_name'],
            "last_name": element['last_name'],
            "sex": element['sex'],
            "birthday": element['birthday'],
            "location": element['location'],
            "preferences": element['preferences']
        })
    return result

def search_username(username):
    """search_name
    Search the event by name
    Returns:
        list: List of events
    """
    retrieved_info = db.collection.users.find_one({"$or":[{"name": username},{"email":username}]}, {'_id':False})
    #retrieved_info = db.collection.users.find_one({"name": username}, {'_id':False})
    if retrieved_info is None:
        return "USER_NOT_FOUND"

    return retrieved_info

def search_one_value_param(value, param):
    """search_name
    Search the event by name
    Returns:
        list: List of events
    """
    retrieved_info = db.collection.users.find_one({value:param}, {'_id':False})
    #retrieved_info = db.collection.users.find_one({"name": username}, {'_id':False})
    if retrieved_info is None:
        return "DATA_NOT_FOUND"

    return retrieved_info

def search_many_value_param(value, param):
    """search_name
    Search the event by name
    Returns:
        list: List of events
    """
    retrieved_info = db.collection.users.find({value:param}, {'_id':False})
    #retrieved_info = db.collection.users.find_one({"name": username}, {'_id':False})
    if retrieved_info is None:
        return "DATA_NOT_FOUND"

    return retrieved_info

def search_by_type(type_usr):
    retrieved_info = list(db.collection.users.find({"user_type":type_usr}))
    result = []
    for element in retrieved_info:
        result.append({
            "name": element['name'],
            "email": element['email'],
            "password": element['password'],
            "user_type": element['user_type'],
            "age": element['age'],
            "first_name": element['first_name'],
            "last_name": element['last_name'],
            "sex": element['sex'],
            "birthday": element['birthday'],
            "preferences":element['preferences'],
            "location": element['location']
        })
    return result

def create_preferences(user, preferences):
    user = search_username(user)
    if(user == "USER_NOT_FOUND"):
        return "USER_NOT_FOUND"
    else:
        print(user['name'])
        db.collection.users.update({"name":user['name']},{"$set":{"preferences":preferences}})
        return "PREFERENCES_INSERTED"

def add_new_preference(user, preferences):
    user = search_username(user)
    if(user == "USER_NOT_FOUND"):
        return "USER_NOT_FOUND"
    else:
        previous_info = db.collection.users.find_one({"name":user['name']}, {"_id":False})
        with_added_params = previous_info['preferences']
        for preference in preferences:
            if preference in with_added_params: pass
            with_added_params.append(preference)
        db.collection.users.update({"name":user['name']},{"$set":{"preferences":with_added_params}})
        return "PREFERENCES_ADDED"

def delete_preferences(user, preferences):
    user = search_username(user)
    if(user == "USER_NOT_FOUND"):
        return "USER_NOT_FOUND"
    else:
        previous_info = db.collection.users.find_one({"name":user['name']}, {"_id":False})
        previous = previous_info['preferences']
        new_list = []
        for parameter in previous:
            if parameter not in preferences:
                new_list.append(parameter)
        db.collection.users.update({"name":user['name']},{"$set":{"preferences":new_list}})
        return "PREFERENCES_UPDATED"

def get_parameter(user, param):
    user = search_username(user)
    if(user == "USER_NOT_FOUND"):
        return "USER_NOT_FOUND"
    else:
        previous_info = db.collection.users.find_one({"name":user['name']}, {"_id":False})
        return previous_info[param]

def get_various_parameters(user, parameters):
    user = search_username(user)
    if(user == "USER_NOT_FOUND"):
        return "USER_NOT_FOUND"
    else:
        previous_info = db.collection.users.find_one({"name":user['name']}, {"_id":False})
        desired_info = {}
        for element in previous_info:
            if element in parameters:
                desired_info.update({element:previous_info[element]})

        return desired_info
