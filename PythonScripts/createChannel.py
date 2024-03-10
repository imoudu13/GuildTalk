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
    # Add a new channel to the database
    app.db.add_channel(channel_name)  # Assume add_channel() adds a channel to the database
    return jsonify({'success': True})  # Return a success response
