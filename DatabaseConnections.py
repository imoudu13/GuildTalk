import sqlite3


class DatabaseHandler:
    def __init__(self, database_name='GuildTalkDB'):
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def execute_query(self, query, parameters=None):
        try:
            self.cursor.execute(query, parameters)
            return True
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False

    def fetch_one(self, query, parameters=None):
        self.execute_query(query, parameters)
        return self.cursor.fetchone()

    def fetch_all(self, query, parameters=None):
        self.execute_query(query, parameters)

        return self.cursor.fetchall()


class DatabaseConnect:
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def insert_into_user(self, data):
        query = "INSERT INTO User (username, password, firstname, lastname, email) VALUES (?, ?, ?, ?, ?);"
        with self.db_handler as db:
            try:
                return db.execute_query(query, data)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")
                return False

    def retrieve_from_user(self, username):
        query = "SELECT password, firstname, lastname, email FROM User WHERE username = ?;"

        with self.db_handler as db:
            try:
                result = db.fetch_one(query, (username,))

                if result is None:
                    return None

                password, firstname, lastname, email = map(str, result)
                return {"username": username, "password": password, "first": firstname, "last": lastname,
                        "email": email}
            except Exception as e:
                print(f"Error during insert_into_user: {e}")

    def retrieve_from_channel(self, channel_id):
        query = "SELECT channelName, creatorUsername FROM Channel WHERE channelID = ?;"

        with self.db_handler as db:
            try:
                result = db.fetch_one(query, (channel_id,))

                if result is None:
                    return None

                channel_name, creator_username = map(str, result)
                return {"id": channel_id, "name": channel_name, "creator": creator_username}
            except Exception as e:
                print(f"Error during insert_into_user: {e}")

    def insert_into_channel(self, information):
        query = "INSERT INTO Channel (channelName, creatorUsername) VALUES (?, ?);"

        with self.db_handler as db:
            try:
                return db.execute_query(query, information)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")

    def retrieve_messages(self, channel_id):
        query = "SELECT messageID, senderUsername, content, timeSent FROM Message WHERE channelID = ?;"

        with self.db_handler as db:
            try:
                result = self.db_handler.fetch_all(query, (channel_id,))

                if not result:
                    return None

                result_list = []

                for row in result:
                    message_id, sender_username, content, time_sent = map(str, row)

                    record = {"channel_id": channel_id,
                              "message_id": int(message_id),
                              "sender": sender_username,
                              "content": content,
                              'time': time_sent}

                    result_list.append(record)

                return result_list
            except Exception as e:
                print(f"Error during insert_into_user: {e}")

    def insert_into_message(self, information):
        with self.db_handler as db:
            try:
                query = "INSERT INTO Message (senderUsername, channelID, receiverUsername, content, timeSent) VALUES (?, ?, ?, ?, ?);"
                return db.execute_query(query, information)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")

    def insertIntoUserChannel(self, information):
        with self.db_handler as db:
            try:
                query = "INSERT INTO UserChannel (username, ChannelID, IsAdmin) VALUES (?, ?, ?);"
                return db.execute_query(query, information)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")
