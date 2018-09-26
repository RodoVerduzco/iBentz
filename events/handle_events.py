""" Handle Events
This program handles the events interactions
"""

import dbhelper.dbhelper as DBHELPER

def insert_event(name, date, event_type, location):
    """insert_event

    Calls the DBHelper to insert the event into the database

    Args:
        name(string): Name of the event
        date(string): Date of the event
        event_type(string): Type of the event (concert, movie, release, etc)
        location(string): Where is the event taking place

    Returns:
        string: Confirmation message
    """
    db = DBHELPER.DBHelper()
    db.event_insert(name, date, event_type, location)
    return "Event inserted successfully"
