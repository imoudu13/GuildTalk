from flask import jsonify
import app


def get_channels(username):
    # Fetch channels from the database
    user = app.db.retrieve_from_user(username)
    if user is None:
        return []
    print(user)
    channels = user["channels"]
    if channels is None:
        return []
    return channels


def add_channel(channel_name):
    username = "test_user"
    #set data (for now we will use boiler plate name. Later it will be logged in user
    channel_info = {
        "_id": channel_name,
        "creator": username
    }
    # Add a new channel to the database
    app.db.insert_into_channel(channel_info)
    # Add chanel to list of channels for that user
    user = app.db.retrieve_from_user(username) #get user
    channels = user["channels"] #get list of channels for user
    channels.append(channel_name) #add new channel to list
    user["channels"] = channels #add new list to user
    app.db.update_user(user) #update user with new list
    return jsonify({'success': True})  # Return a success response
