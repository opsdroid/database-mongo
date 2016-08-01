import logging
from pymongo import MongoClient


class DatabaseMongo:
    """A module for opsdroid to allow memory to persist in a mongo database."""

    def __init__(self, config):
        """Start the database connection."""
        logging.debug("Loaded mongo database connector")
        self.name = "mongo"
        self.config = config
        self.client = None
        self.db = None

    def connect(self):
        """Connect to the database."""
        host = self.config["host"] if "host" in self.config else "localhost"
        port = self.config["port"] if "port" in self.config else "27017"
        database = self.config["database"] \
            if "database" in self.config else "opsdroid"
        path = "mongodb://" + host + ":" + port
        self.client = MongoClient(path)
        self.db = self.client[database]

    def put(self, key, data):
        """Insert or replace an object into the database for a given key."""
        # TODO: Clean this up, inserting one and deleting the rest is
        #       definitely a sledgehammer approach
        result = self.db[key].insert_one(data)
        newid = result.inserted_id
        result = self.db[key].delete_many({"_id": {"$ne": newid}})

    def get(self, key):
        """Get a document from the database for a given key."""
        cursor = self.db[key].find(
                        {"$query": {}, "$orderby": {"$natural" : -1}}
                        ).limit(1)
        for document in cursor:
            return document
