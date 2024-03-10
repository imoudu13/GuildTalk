from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi


# This is the class that directly connects to the database
class DatabaseHandler:
    def __init__(self):
        self.uri = "mongodb+srv://GuildTalk:cosc310guildtalk@guildtalk.nmclwfs.mongodb.net/?retryWrites=true&w=majority&appName=GuildTalk"
        self.client = None
        self.db = None

    def __enter__(self):
        try:
            self.client = MongoClient(self.uri, server_api=ServerApi('1'))
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

    def fetch_all(self, collection_name, parameters):
        collection = self.db[collection_name]
        return list(collection.find(parameters))

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
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def insert_into_user(self, data):
        collection_name = "User"
        with self.db_handler as db:

            try:
                return db.execute_insert(collection_name, data)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")
                return False

    def retrieve_from_user(self, username):
        collection_name = "User"
        with self.db_handler as db:
            try:
                result = db.fetch_one(collection_name, {"_id": username})

                if result is None:
                    return None

                return {
                    "_id": result["_id"],
                    "password": result["password"],
                    "first": result["firstname"],
                    "last": result["lastname"],
                    "email": result["email"]
                }
            except Exception as e:
                print(f"Error during retrieve_from_user: {e}")
                return None

    # Add similar modifications for other functions...

    def update_user(self, information):
        collection_name = "User"
        with self.db_handler as db:
            try:
                query_params = {"username": information[0]}
                update_data = {
                    "$set": {
                        "firstname": information[1],
                        "lastname": information[2],
                        "email": information[3],
                        "password": information[4]
                    }
                }
                return db.update_one(collection_name, query_params, update_data)
            except Exception as e:
                print(f"Error during update_user: {e}")
                return False

    def retrieve_from_channel(self, channel_id):
        collection_name = "Channel"
        with self.db_handler as db:
            try:
                result = db.fetch_one(collection_name, {"channelID": channel_id})

                if result is None:
                    return None

                return {
                    "id": result["channelID"],
                    "name": result["channelName"],
                    "creator": result["creatorUsername"]
                }
            except Exception as e:
                print(f"Error during retrieve_from_channel: {e}")
                return None

    def insert_into_channel(self, information):
        collection_name = "Channel"
        with self.db_handler as db:
            try:
                return db.execute_insert(collection_name, information)
            except Exception as e:
                print(f"Error during insert_into_channel: {e}")
                return False

    def retrieve_messages(self, channel_id):
        collection_name = "Message"
        with self.db_handler as db:
            try:
                result = db.fetch_all(collection_name, {"channelID": channel_id})

                if not result:
                    return None

                result_list = []

                for message in result:
                    record = {
                            "channel_id": message["channelID"],
                            "message_id": message["messageID"],
                            "sender": message["senderUsername"],
                            "content": message["content"],
                            'time': message["timeSent"]
                        }

                    result_list.append(record)

                return result_list
            except Exception as e:
                print(f"Error during retrieve_messages: {e}")
                return None

    def insert_into_message(self, information):
        collection_name = "Message"
        with self.db_handler as db:
            try:
                return db.execute_insert(collection_name, information)
            except Exception as e:
                print(f"Error during insert_into_message: {e}")
                return False

    def insert_into_user_channel(self, information):
        collection_name = "UserChannel"

        with self.db_handler as db:
            try:
                return db.execute_insert(collection_name, information)
            except Exception as e:
                print(f"Error during insert_into_user_channel: {e}")
                return False
