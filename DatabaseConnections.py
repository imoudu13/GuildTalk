import sqlite3


# This is the class that directly connects to the database
class DatabaseHandler:
    # This is the initialization function
    # upon creation of a DatabaseHandler class it creates 3 variables, a connection, cursor, and a database name
    # In java you'd declare variables that the class would use then instantiate them in the constructor
    # in python you do it in the init method
    def __init__(self, database_name='GuildTalkDB'):
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    # The enter method is called when you use the with statement, you'll see it later
    # It establishes a connection to the db and creates the cursor
    def __enter__(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        return self

    # The exit method is called when the code leaves the with statement, you'll see it later
    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    # This function accepts a sql statement and executes it
    def execute_query(self, query, parameters=None):
        try:
            self.cursor.execute(query, parameters)
            return True
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False

    # This is for fetching the single result
    def fetch_one(self, query, parameters=None):
        self.execute_query(query, parameters)
        return self.cursor.fetchone()

    # This gets all tuples returned by the statement
    def fetch_all(self, query, parameters=None):
        self.execute_query(query, parameters)

        return self.cursor.fetchall()


# This is the class that handles the results returned from the database
class DatabaseConnect:
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def insert_into_user(self, data):
        query = "INSERT INTO User (username, password, firstname, lastname, email) VALUES (?, ?, ?, ?, ?);"
        with self.db_handler as db:  # This calls the enter function in the DatabaseHandler class, it's responsible for opening the connection
            try:
                return db.execute_query(query, data)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")
                return False
        # When the code leaves the with block the exit function is called, closing the connection

    def retrieve_from_user(self, username):
        query = "SELECT password, firstname, lastname, email FROM User WHERE username = ?;"
        # This function retrieves a tuple matching the username form the User table
        # If the username isn't in the db it returns None
        # Otherwise it puts the information in a dictionary
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
        # This function retrieves a tuple matching the channel id form the Channel table
        # If the channel id isn't in the db it returns None
        # Otherwise it puts the information in a dictionary
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
        # This function accept a tuple with some information
        # It uses that information to fill out the binds in the insertion statement.
        # It's sent to the execution function, if there are no errors, it returns true, otherwise false
        with self.db_handler as db:
            try:
                return db.execute_query(query, information)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")

    def retrieve_messages(self, channel_id):
        query = "SELECT messageID, senderUsername, content, timeSent FROM Message WHERE channelID = ?;"
        # This function retrieves a table of messages matching the channel id form the Message table
        # If the channel id isn't in the db it returns None
        # Otherwise it puts the information for each message in a dictionary
        # Then adds all the dictionaries to a list and return the list of dictionaries
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

    def insert_into_user_channel(self, information):
        with self.db_handler as db:
            try:
                query = "INSERT INTO UserChannel (username, ChannelID, IsAdmin) VALUES (?, ?, ?);"
                return db.execute_query(query, information)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")

    def update_user(self, information):
        with self.db_handler as db:
            try:
                query = "UPDATE User SET username = ?, firstname = ?, lastname = ?, email = ?, password = ? WHERE username  = ?"
                return db.execute_query(query, information)
            except Exception as e:
                print(f"Error during insert_into_user: {e}")
