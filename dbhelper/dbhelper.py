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

    