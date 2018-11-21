""" Handle Events
This program handles the events interactions
"""

import dbhelper.dbhelper as DBHELPER
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import smtplib
db = DBHELPER.DBHelper()

def insert_user(username, email, user_type, password, age, first_name, last_name, sex, birthday, location):

    retrieved_info = db.collection.users.find_one({"$or":[{"name": username},{"email":username}]}, {'_id':False})
    if(retrieved_info is None):
    # sex: M, F
    # birthday: %Y-%m-%d
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
            "preferences": [],
            "events":""
        })
        
    #db.user_insert(user_name, email, password, age, first_name, last_name, sex, birthday, location)
        return "user inserted successfully"
    return "User/email already exists"

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

def modify_user(usr, email, password, age, first_name, last_name, sex, birthday, location):

    db.collection.users.update_one({"$or": [{"name": usr}, {"email":usr}]},{"$set": {"email":email, "password":password, "age": age, "first_name":first_name,\
    "last_name":last_name, "sex":sex, "birthday":birthday,"location":location}}, upsert=False)

    return "UPDATED"


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
            "preferences": element['preferences'],
            "events": element['events']
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
            "location": element['location'],
            "events": element['events']
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

def update_preferences(user, preferences):
    user = search_username(user)
    if(user == "USER_NOT_FOUND"):
        return "USER_NOT_FOUND"
    else:
         db.collection.users.update({"name":user['name']},{"$set":{"preferences":preferences}})
    
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

def add_event(user, event_id):
    print("inserted")
    user_info = search_username(user)
    flag =0
    print(user_info)
    if user_info == "USER_NOT_FOUND":
        return "ERROR_EVENT_ALREADY_EXISTED"
    else:
        event_info = db.collection.events.find_one({'_id': ObjectId(event_id)})
        already_added_events = user_info['events']
        for event in user_info['events']:
            if event_info['name'] == event['name']:
                flag =1
        
        if flag ==0:
            already_added_events.append({"name": event_info['name'], "date":event_info['date'], "sent":"false"})
            db.collection.users.update({"name":user_info['name']},{"$set":{"events":already_added_events}})
            return "EVENT ADDED"

def get_org_event(user):
    user_info = search_username(user)
    if user_info == "USER_NOT_FOUND":
        return "USER_NOT_FOUND"
    else:
        events = db.collection.events.find({'organizer': user})
        if events is None:
            return "NO_EVENTS_FOUND"
        
    result = []
    for element in events:
        result.append({
            "id" : str(element.get('_id')),
            "name": element["name"],
            "event_date": element["date"],
            "event_type": element["category"],
            "event_location": element["location"],
            "image":element['image'],
            "max_participants": element['max_participants'],
            "description": element['description'],
            "ext_info": element['ext_info'],
            "category": element['category'],
            "status": element['status'],
            "num_registered": element['num_registered'],
            "organizer":element['organizer']
        })

    return result



def delete_event(user, event_id):
    user_info = search_username(user)
    if user_info == "USER_NOT_FOUND":
        return "ERROR_USER_NOT_FOUND"
    else:
        event_info = db.collection.events.find_one({'_id': ObjectId(event_id)})
        my_events =[]
        for event in user_info['events']:
            if event_info['name'] == event['name']: pass
            my_events.append(event)
        
        db.collection.users.update({"name":user_info['name']},{"$set":{"events":my_events}})
        return "EVENT ADDED"

def get_user_recommendations(usr):

    usr_preferences = get_parameter(usr,"preferences")
    if usr_preferences == "USER_NOT_FOUND":
        return usr_preferences
    print(usr_preferences)
    recommendations =[]
    results = db.collection.events.aggregate([{ "$sample": { "size": 3 } }])
    #results = db.collection.events.find({"$and":[{"category":{"$in":usr_preferences}},{"status":"ACTIVE"}]})
    #print(results)
    for element in results:
        #print(str(element['category']) in usr_preferences)
        if str(element['category']) in usr_preferences and element['status'] =="ACTIVE":
                recommendations.append({"id" : str(element.get('_id')),
                                        "name": element["name"],
                                        "event_date": element["date"],
                                        "event_type": element["category"],
                                        "event_location": element["location"],
                                        "image":element['image'],
                                        "max_participants": element['max_participants'],
                                        "description": element['description'],
                                        "ext_info": element['ext_info'],
                                        "category": element['category'],
                                        "status": element['status'],
                                        "num_registered": element['num_registered'],
                                        "organizer": element['organizer']})
                
    print(recommendations)
    return recommendations

def send_mails():

    gmail_user = "gabo.garces96@gmail.com"
    gmail_pwd = "Ggc#27&25"

    users = read_all()
    events_t = []
    for user in users:
        if user['user_type'] == "USER":
            events_t = []
            for event in user['events']:
                
                if event['sent'] == "false" and (str(datetime.strptime(event['date'], "%Y-%m-%d").date()- timedelta(days=10)) == str(datetime.now().strftime("%Y-%m-%d"))):
                    #print(event['name'])
                    event['sent'] = "true"
                    TO = 'gabo-fly@hotmail.com'
                    SUBJECT = "iBentz- Your event "+event['name']+" is coming up!"
                    TEXT = "testing"
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(gmail_user, gmail_pwd)
                    BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_user,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])
                    server.sendmail(gmail_user, [TO], BODY)
                events_t.append(event)
            db.collection.users.update({"name":user['name']},{"$set":{"events":events_t}})


            

    