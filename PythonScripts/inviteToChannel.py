from flask import jsonify
from DatabaseConnections import DatabaseConnect

db = DatabaseConnect()


def addUserToChannel(channel_name, username):
    # Retrieve user from the database
    user = db.retrieve_document(username, 'User')
    # Check if user exists
    if user is None:
        return jsonify({'success': False, 'error': 'User not found'})

    # Retrieve channel information
    channel_information = db.retrieve_document(channel_name, 'Channel')

    # adds user to channel info
    users = channel_information.get("users", [])
    if username not in users:
        users.append(username)
        channel_information["users"] = users
        db.update(channel_name, channel_information, 'Channel')
    else:
        return jsonify({'success': False, 'error': 'User already in channel'})

    # Get list of channels for user, or create an empty list if it doesn't exist
    channels = user.get("channels", [])
    if channel_name not in channels:
        # Add new channel to list
        channels.append(channel_name)
        # Update user with new list of channels
        user["channels"] = channels
        db.update(user['_id'], user, 'User')  # Update user with new list
        return jsonify({'success': True})  # Return a success response
    else:
        return jsonify({'success': False, 'error': 'User already in channel'})
