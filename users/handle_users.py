""" Handle Events
This program handles the events interactions
"""

import dbhelper.dbhelper as DBHELPER
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
            "events":[]
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

def check_events(usr, event_id):
    user = search_username(usr)
    flag =0
    event_info = db.collection.events.find_one({'_id': ObjectId(event_id)})
    if(user == "USER_NOT_FOUND"):
        return "USER_NOT_FOUND"
    else:
        previous_info = db.collection.users.find_one({"name":user['name']}, {"_id":False})
        for user_event in previous_info['events']:
                if user_event['name'] == event_info['name']:
                    flag =1
    if flag ==0:
        return "NOT_REGISTERED"
    else:
        return "REGISTERED"


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
        if int(event_info['num_registered']) +1 <= int(event_info['max_participants']):
            
            already_added_events = user_info['events']
            for event in user_info['events']:
                if event_info['name'] == event['name']:
                    flag =1
            
            if flag ==0:
                already_added_events.append({"name": event_info['name'], "date":event_info['date'], "sent":"false"})
                db.collection.users.update({"name":user_info['name']},{"$set":{"events":already_added_events}})
                registered = event_info['num_registered'] +1
                db.collection.events.update({"_id":ObjectId(event_id)}, {"$set":{"num_registered":registered}})
                return "EVENT_ADDED"
        return "EVENT_FULL"

def get_org_event(user,stat):
    user_info = search_username(user)
    if user_info == "USER_NOT_FOUND":
        return "USER_NOT_FOUND"
    else:
        events = db.collection.events.find({"$and":[{'organizer': user}, {"status":stat}]})
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
    print("sending email")
    print(">>>>>>>>>")
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
                    html = '<!doctype html><html><head><meta name="viewport" content="width=device-width" />\
                            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><title>Simple Transactional Email</title>\
                            <style>img { border: none; -ms-interpolation-mode: bicubic; max-width: 100%;} body {background-color: #f6f6f6;\
                            font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0;\
                            padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;} table { border-collapse: separate;\
                            mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; } table td {font-family: sans-serif; font-size: 14px;\
                            vertical-align: top; } .body {background-color: #f6f6f6; width: 100%; } .container { display: block; Margin: 0 auto !important;\
                            max-width: 580px; padding: 10px; width: 580px; } .content { box-sizing: border-box;display: block;Margin: 0 auto;max-width: 580px;padding: 10px;}\
                            .main { background: #ffffff;border-radius: 3px;width: 100%;} .wrapper {box-sizing: border-box;padding: 20px;}\
                            .content-block { padding-bottom: 10px;   padding-top: 10px; } .footer {   clear: both;   Margin-top: 10px;   text-align: center;   width: 100%;  }   .footer td,   .footer p,   .footer span,   .footer a {\
                            color: #999999;font-size: 12px;text-align: center;  } h1, h2, h3, h4 {   color: #000000;   font-family: sans-serif;   font-weight: 400;   line-height: 1.4;   margin: 0;   margin-bottom: 30px;  } h1 {   font-size: 35px;   font-weight: 300;   text-align: center;   text-transform: capitalize;  } p, ul, ol {   font-family: sans-serif;   font-size: 14px;   font-weight: normal;   margin: 0;   margin-bottom: 15px;  }   p li,   ul li,   ol li {\
                            list-style-position: inside; margin-left: 5px;  } a {   color: #3498db;   text-decoration: underline;  } .btn {   box-sizing: border-box;   width: 100%; }   .btn > tbody > tr > td {\
                            padding-bottom: 15px; }   .btn table { width: auto;  }   .btn table td {background-color: #ffffff;border-radius: 5px;text-align: center;  }   .btn a { background-color: #ffffff;\
                            border: solid 1px #3498db;border-radius: 5px;box-sizing: border-box;color: #3498db;cursor: pointer;display: inline-block;font-size: 14px;font-weight: bold;margin: 0;\
                            padding: 12px 25px;text-decoration: none; text-transform: capitalize;  } .btn-primary table td {   background-color: #3498db;  } .btn-primary a {   background-color: #3498db;   border-color: #3498db;   color: #ffffff;  } .last {   margin-bottom: 0;  } .first {   margin-top: 0;  } .align-center {   text-align: center;  } .align-right {   text-align: right;  } .align-left {   text-align: left;  } .clear {   clear: both;  } .mt0 {   margin-top: 0;  } .mb0 { margin-bottom: 0;  } .preheader {   color: transparent;   display: none;   height: 0;   max-height: 0;   max-width: 0;   opacity: 0;   overflow: hidden;   mso-hide: all;   visibility: hidden;   width: 0;  } .powered-by a {   text-decoration: none;  } hr {   border: 0;   border-bottom: 1px solid #f6f6f6;   Margin: 20px 0;  }\
                            @media only screen and (max-width: 620px) { table[class=body] h1 { font-size: 28px !important; margin-bottom: 10px !important; } table[class=body] p, table[class=body] ul, table[class=body] ol, table[class=body] td, table[class=body] span, table[class=body] a { font-size: 16px !important; } table[class=body] .wrapper,\
                            table[class=body] .article { padding: 10px !important; } table[class=body] .content { padding: 0 !important; } table[class=body] .container { padding: 0 !important; width: 100% !important; } table[class=body] .main { border-left-width: 0 !important; border-radius: 0 !important; border-right-width: 0 !important; } table[class=body] .btn table { width: 100% !important; } table[class=body] .btn a { width: 100% !important; } table[class=body] .img-responsive { height: auto !important;\
                            max-width: 100% !important; width: auto !important; } } @media all { ExternalClass {  width: 100%; }.ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div {  line-height: 100%; }.apple-link a {  color: inherit !important;  font-family: inherit !important;  font-size: inherit !important;  font-weight: inherit !important;  line-height: inherit !important;  text-decoration: none !important; }.btn-primary table td:hover {  background-color: #34495e !important; }.btn-primary a:hover {  background-color: #34495e !important;  border-color: #34495e !important; }   }</style>  </head>\
                            <body class=""><table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body"><tr><td>&nbsp;</td><td class="container"><div class="content"><!-- START CENTERED WHITE CONTAINER --><span class="preheader">iBentz</span><table role="presentation" class="main">\
                            <!-- START MAIN CONTENT AREA --><tr><td class="wrapper"><table role="presentation" border="0" cellpadding="0" cellspacing="0">\
                            <tr><td><p>Hi there,'+user['name']+'</p><p>Your event '+event['name']+'is coming up on '+event['date']+'</p><p>Make sure to check the weather forecast and pick up your tickets on time! </td></tr></table></td></tr><!-- END MAIN CONTENT AREA --></table>\
                            <!-- START FOOTER --><div class="footer"><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="content-block"><span class="apple-link">Company Inc, 3 Abbey Road, San Francisco CA 94102</span></td></tr><tr><td class="content-block powered-by">Powered by <a href="http://htmlemail.io">HTMLemail</a>.</td></tr></table></div><!-- END FOOTER --><!-- END CENTERED WHITE CONTAINER --></div></td><td>&nbsp;</td></tr></table></body></html>'
                    event['sent'] = "true"
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(gmail_user, gmail_pwd)
                    msg = MIMEMultipart('alternative')
                    recipient = "gabo-fly@hotmail.com"
                    msg['Subject'] = "iBentz- Your event "+event['name']+" is coming up!"
                    msg['From'] = gmail_user
                    msg['To'] = recipient
                    part2 = MIMEText(html, 'html')
                    msg.attach(part2)
                    server.sendmail(gmail_user, recipient, msg.as_string())
                    print("Email Sent")
                    print(">>>>>")
                events_t.append(event)
            db.collection.users.update({"name":user['name']},{"$set":{"events":events_t}})


            

    