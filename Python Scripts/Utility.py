import sqlite3


def insert_into_User(data):
    try:
        # Attempt to connect to the SQLite database
        connection = sqlite3.connect('../GuildTalkDB')

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


def retrieve_from_user(username):
    try:
        # Attempt to connect to the SQLite database
        connection = sqlite3.connect('../GuildTalkDB')

        cursor = connection.cursor()

        # Insert data into the User table
        insert_query = "SELECT password, firstname, lastname FROM User WHERE username = ?;"
        cursor.execute(insert_query, username)

        result = cursor.fetchone()

        password, firstname, lastname = map(str, result)

        return password, firstname, lastname

    except sqlite3.Error as e:
        print(e)
        return ' '  # returns false meaning there's some problem
