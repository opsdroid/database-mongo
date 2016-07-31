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
        port = self.config["port"] if "port" in self.config else "27019"
        database = self.config["database"] \
            if "database" in self.config else "opsdroid"
        path = "mongodb://" + host + ":" + port
        self.client = MongoClient(path)
        self.db = self.client[database]
