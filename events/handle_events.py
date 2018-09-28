""" Handle Events
This program handles the events interactions
"""
import config
from pymongo import MongoClient

CLIENT = MongoClient(config.DB_URI,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)
DATABASE = CLIENT.get_default_database()
collection = DATABASE.events

def insert_event(name, date, event_type, location):
    """insert_event
    Calls the DBHelper to insert the event into the database

    Args:
        name(string): Name of the event
        date(string): Date of the event
        event_type(string): Type of the event (concert, movie, release, etc)
        location(string): Where is the event taking place

    Returns:
        string: Confirmation Message
    """
    collection.insert({
        "name": name,
        "date": date,
        "type": event_type,
        "location": location
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
    retrieved_info = list(collection.find())
    return get_important_info(retrieved_info)

def search_name(name):
    """search_name
    Search the event by name

    Returns:
        list: List of events
    """
    retrieved_info = collection.find({"name": name})
    return get_important_info(retrieved_info)

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
            event_filter.append({"type": event_type})
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
    result = collection.find({"type": event_type})
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
            "name": element["name"],
            "event_date": element["date"],
            "event_type": element["type"],
            "event_location": element["location"]
        })

    return result
