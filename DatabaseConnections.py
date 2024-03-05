import sqlite3


def insertIntoUser(data):
    try:
        # Attempt to connect to the SQLite database
        connection = sqlite3.connect('GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        insert_query = "INSERT INTO User (username, password, firstname, lastname, email) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(insert_query, data)

        # If no exception occurred, commit the changes (if any)
        connection.commit()

        return True  # returns true meaning there were no errors
    except sqlite3.Error as e:
        print(f"Error in insert_into_User: {e}")
        return False  # returns false meaning there's some problem


def retrieveFromUser(username):
    try:
        connection = sqlite3.connect('GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        select_query = f"SELECT password, firstname, lastname, email FROM User WHERE username = '{username}';"
        cursor.execute(select_query)

        result = cursor.fetchone()

        if result is None:
            return None

        password, firstname, lastname, email = map(str, result)

        return {"username": username, "password": password, "first": firstname, "last": lastname, "email": email}

    except sqlite3.Error as e:
        print(e)


def retrieveFromChannel(channelID):
    try:
        connection = sqlite3.connect('GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        select_query = f"SELECT channelName, creatorUsername FROM Channel WHERE channelID = {channelID};"
        cursor.execute(select_query)

        result = cursor.fetchone()

        if result is None:
            return None

        channelName, creatorUsername = map(str, result)

        return {"id": channelID, "name": channelName, "creator": creatorUsername}

    except sqlite3.Error as e:
        print(e)


def insertIntoChannel(information):
    try:
        connection = sqlite3.connect('GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        select_query = "INSERT INTO Channel (channelName, creatorUsername) VALUES (?, ?);"
        cursor.execute(select_query, information)

        # If no exception occurred, commit the changes (if any)
        connection.commit()

        return True

    except sqlite3.Error as e:
        print(e)
        return False


def retrieveMessage(username):
    try:
        connection = sqlite3.connect('GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        select_query = f"SELECT messageID, senderUsername, channelID, content, timeSent FROM Message WHERE senderUsername = '{username}';"
        cursor.execute(select_query)

        result = cursor.fetchall()

        if not result:
            return None

        result_list = []

        for row in result:
            messageID, senderUsername, channelID, content, timeSent = map(str, row)

            record = {"channel_id": int(channelID),
                      "message_id": int(messageID),
                      "sender": senderUsername,
                      "content": content,
                      'time': timeSent}

            result_list.append(record)

        return result_list

    except sqlite3.Error as e:
        print(e)


def insertIntoMessage(information):
    try:
        connection = sqlite3.connect('GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        select_query = "INSERT INTO Message (senderUsername, channelID, receiverUsername, content, timeSent) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(select_query, information)

        # If no exception occurred, commit the changes (if any)
        connection.commit()

        return True

    except sqlite3.Error as e:
        print(e)
        return False


def insertIntoUserChannel(information):
    try:
        connection = sqlite3.connect('GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        select_query = "INSERT INTO UserChannel (username, ChannelID, IsAdmin) VALUES (?, ?, ?);"
        cursor.execute(select_query, information)

        # If no exception occurred, commit the changes (if any)
        connection.commit()

        return True
    except sqlite3.Error as e:
        print(e)
        return False
