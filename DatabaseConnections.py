from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi


# This is the class that directly connects to the database
class DatabaseHandler:
    def __init__(self):
        self.uri = "mongodb+srv://jumbalaya112:cosc310GuildTalk@guildtalk.nktspge.mongodb.net/?retryWrites=true&w=majority&appName=GuildTalk"
        self.client = None
        self.db = None

    def __enter__(self):
        try:
            ssl_options = {'tls': True, 'tlsInsecure': True}
            self.client = MongoClient(self.uri, server_api=ServerApi('1'), **ssl_options)
            self.db = self.client.get_database("GuildTalk")
        except errors.ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.client:
            self.client.close()

    def execute_insert(self, collection_name, document):
        try:
            collection = self.db[collection_name]
            return collection.insert_one(document).inserted_id
        except errors.WriteError as e:
            print(f"Insert failed: {e}")
            return None

    def fetch_one(self, collection_name, parameters):
        collection = self.db[collection_name]
        return collection.find_one(parameters)

    def update_one(self, collection_name, query_params, update_data):
        try:
            collection = self.db[collection_name]
            result = collection.update_one(query_params, update_data)
            return result.modified_count > 0  # Returns True if at least one document is modified
        except Exception as e:
            print(f"Error during update_one: {e}")
            return False


# This is the class that handles the results returned from the database
class DatabaseConnect:
    _instance = None

    # This is to ensure that only one instance of this class exists
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_handler = DatabaseHandler()
        return cls._instance

    def insert_into_user(self, data):
        collection_name = "User"

        data.setdefault("channels", [])

        with self.db_handler as db:

            try:
                return db.execute_insert(collection_name, data)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")
                return False

    def insert_into_channel(self, information):
        collection_name = "Channel"

        # adds the creator to the list of admins and list of users
        # also add an empty list of messages
        information.setdefault("admins", [information["creator"]])
        information.setdefault("users", [])
        information.setdefault("messages", [])
        information.setdefault("isDirectMessageChat", 0)
        with self.db_handler as db:
            try:
                return db.execute_insert(collection_name, information)
            except Exception as e:
                print(f"Error during insert_into_channel: {e}")
                return False

    # The next two functions can be used to insert into any collection in the db provided that you specific the collection name
    # this function is for retrieving a document from a collection
    def retrieve_document(self, doc_id, collection_name):
        with self.db_handler as db:
            try:
                result = db.fetch_one(collection_name, {"_id": doc_id})

                if result is None:
                    return None

                return result
            except Exception as e:
                print(f"Error during retrieve_from_user: {e}")
                return None

    # this function is for updating a documents in a collection, it requires the id for the document,
    # as well as the collection that the document is a part of
    def update(self, documentid, dictionary, collection):
        with self.db_handler as db:
            try:
                db.update_one(collection, {"_id": documentid}, {"$set": dictionary})
                return True
            except Exception as e:
                print(f"Error during update_channel: {e}")
                return False
