from flask import jsonify


def get_channels(username):
    from app import db
    # Fetch channels from the database
    channels = db.retrieve_from_user(username)
    return channels["channels"]


print(get_channels("test_user"))


def add_channel(channel_name):
    from app import db
    # Add a new channel to the database
    db.add_channel(channel_name)  # Assume add_channel() adds a channel to the database
    return jsonify({'success': True})  # Return a success response
