from flask import jsonify
from DatabaseConnections import DatabaseConnect
import app

db = DatabaseConnect()


def get_channels(username):
    # Fetch channels from the database
    user = db.retrieve_document(username, "User")
    if user is None:
        return []

    channels = user["channels"]
    if channels is None:
        return []
    return channels


def add_channel(channel_name, username):
    # Set data (for now we will use boilerplate name. Later it will be logged in user)
    channel_info = {
        "_id": channel_name,
        "creator": username
    }
    # Add a new channel to the database
    db.insert_into_channel(channel_info)

    # Retrieve user from the database
    user = db.retrieve_document(username, "User")
    if user:
        # Get list of channels for user, or create an empty list if it doesn't exist
        channels = user.get("channels", [])
        # Add new channel to list
        channels.append(channel_name)
        # Update user with new list of channels
        user["channels"] = channels
        db.update(user['_id'], user, "User")  # Update user with new list
        return jsonify({'success': True})  # Return a success response
    else:
        print("No channel found")
        return jsonify({'success': False, 'error': 'User not found'})
