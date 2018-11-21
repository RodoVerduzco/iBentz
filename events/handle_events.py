""" Handle Events
This program handles the events interactions
"""
from pymongo import MongoClient
from bson.objectid import ObjectId
import config

CLIENT = MongoClient(config.DB_URI,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)
DATABASE = CLIENT.get_default_database()
collection = DATABASE.events


def insert_event(name, image, date, max_part, location, description,
                 info, event_type, status, num_registered, organizer):
    """insert_event
    Calls the DBHelper to insert the event into the database
    categories: MUSICA, DEPORTE, ARTE, CINE, LITERATURA, TEATRO
    Args:
        name           (string):  Name of the event
        image          (string):  Url for the image of the event
        date           (string):  Date of the event
        location       (string):  Where is the event taking place
        description    (string):  Additional information which describes the event
        info           (string):  External info like a url to find more information
        category     (string):  Type of the event (concert, movie, release, etc)
        status         (string):  Event stats (active, inactive)
        num_registered (int):     Number of people attending to the event
        organizer       (string): Organizer of the event

    Returns:
        string: Confirmation Message
    """
    collection.insert({
        "name": name,
        "image": image,
        "date": date,
        "max_participants": max_part,
        "location": location,
        "description": description,
        "ext_info": info,
        "category": event_type,
        "status": status,
        "num_registered": num_registered,
        "organizer": organizer

    })

    return "Event inserted successfully"

def delete_event(event_name):
    """delete_event
    Calls the DBHelper to delete the event into the database

    Args:
        event_name(string): Name of the event

    Returns:
        string: Confirmation Message
    """
    delete_query = {"name": event_name}
    collection.delete_one(delete_query)

    return "Event " + event_name + " was deleted"

def read_all():
    """read_all
    Calls the DBHelper to retrieve the complete list of events

    Returns:
        list: List of events
    """
    retrieved_info = list(DATABASE.events.find())
    print(retrieved_info)
    return get_important_info(retrieved_info)

def search_name(name):
    """search_name
    Search the event by name

    Returns:
        list: List of events
    """
    retrieved_info = collection.find({"name": name})
    if retrieved_info is None:
        return "NOT_FOUND"
    return get_important_info(retrieved_info)

def search_id( event_id):
        element = collection.find_one({'_id': ObjectId(event_id)})
        
        if element is None:
            return "EVENT_NOT_FOUND"
        result ={
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
            "organizer": ""#element['organizer']
        }
        return result

def search_date(date, location, event_type, name):
    """search_date
    Search the event by date, if other filters detected, filter the result
    by them

    Returns:
        list: List of events
    """
    if (location is None) and (event_type is None) and (name is None):
        result = collection.find({"date": date})
    else:
        event_filter = []
        event_filter.append({"date": date})

        if location is not None:
            event_filter.append({"location": location})
        if event_type is not None:
            event_filter.append({"categorie": event_type})
        if name is not None:
            event_filter.append({"name": name})

        query = {"$and": event_filter}
        result = collection.find(query)

    return get_important_info(result)

def search_location(location, event_type, name):
    """search_location
    Search the event by location, if other filters detected, filter the result
    by them

    Returns:
        list: List of events
    """
    if (event_type is None) and (name is None):
        result = collection.find({"location": location})
    else:
        event_filter = []
        event_filter.append({"location": location})

        if event_type is not None:
            event_filter.append({"type": event_type})
        if name is not None:
            event_filter.append({"name": name})

        query = {"$and": event_filter}
        result = collection.find(query)

    return get_important_info(result)

def search_type(event_type):
    """search_type
    Search the event by type

    Returns:
        list: List of events
    """
    result = collection.find({"category": event_type})
    return get_important_info(result)

def search_with_various(event_type, location, name):
    """search_type
    Search the event by type

    Returns:
        list: List of events
    """
    result = collection.find({"$and":[{"category": event_type},{"location":location},{"name":name}, {"status":"ACTIVE"} ]})
    return get_important_info(result)

def search_location_type(event_type, location):
    """search_type
    Search the event by type

    Returns:
        list: List of events
    """
    result = collection.find({"$and":[{"category": event_type},{"location":location}, {"status":"ACTIVE"} ]})
    return get_important_info(result)

def search_location_name(location, name):
    """search_type
    Search the event by type

    Returns:
        list: List of events
    """
    result = collection.find({"$and":[{"name": name},{"location":location}, {"status":"ACTIVE"} ]})
    return get_important_info(result)

def get_important_info(retrieved_info):
    """get_important_info
    Append the important info of the event into a list

    Returns:
        list: List with the important info
    """
    result = []
    for element in retrieved_info:
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
            "organizer":""#element['organizer']
        })

    return result
