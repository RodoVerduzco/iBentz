"""DBHelper

This dbhelper is in charge of every interaction to be done with the database in mongo
"""
from pymongo import MongoClient
import config

class DBHelper:
    """ DBHelper Class """

    def __init__(self):
        CLIENT = MongoClient(config.DB_URI,
                             connectTimeoutMS=30000,
                             socketTimeoutMS=None,
                             socketKeepAlive=True)
        DATABASE = CLIENT.get_default_database()
        self.collection = DATABASE

    def event_insert(self, name, date, event_type, location):
        """event_insert

        Insert an event inside the database

        Args:
            self(object): The object created with the DATABASE
            name(string): Name of the event to be inserted
            date(string): Date of the event to be inserted
            event_type(string): Type of the event (concert, movie, release, etc) to be inserted
            location(string): Where is the event taking place to be inserted
        """
        self.collection.events.insert({
            "name": name,
            "date": date,
            "type": event_type,
            "location": location
        })

    def event_delete(self, event_name):
        """event_deletes

        Delete an event from the database

        Args:
            self(object): The object created with the DATABASE
            event_name(string): Name of the event to be inserted
        """

        delete_query = {"name": event_name}
        self.collection.events.delete_one(delete_query)

    def event_read_all(self):
        """event_read_all

        Retrieve a complete list of events, and concatenate the necessary data
        into a new list for the user to see

        Args:
            self(object): The object created with the DATABASE

        Returns:
            list: List containing all the events.
        """
        result = []
        retrieved_info = list(self.collection.events.find())

        for element in retrieved_info:
            result.append({
                "name": element["name"],
                "event_date": element["date"],
                "event_type": element["type"],
                "event_location": element["location"]
            })

        return result
