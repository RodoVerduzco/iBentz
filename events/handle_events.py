""" Handle Events
This program handles the events interactions
"""

import dbhelper.dbhelper_mirror as DBHELPER

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
    db = DBHELPER.DBHelper()
    db.event_insert(name, date, event_type, location)
    return "Event inserted successfully"

def delete_event(event_name):
    """delete_event

    Calls the DBHelper to delete the event into the database

    Args:
        event_name(string): Name of the event

    Returns:
        string: Confirmation Message
    """
    db = DBHELPER.DBHelper()
    db.event_delete(event_name)
    return "Event " + event_name + " was deleted"

def read_all():
    """read_all

    Calls the DBHelper to retrieve the complete list of events

    Returns:
        list: List of events
    """
    db = DBHELPER.DBHelper()
    return db.event_read_all() 
