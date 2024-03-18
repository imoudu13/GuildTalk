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


def add_channel(channel_name, username):
    # Set data (for now we will use boilerplate name. Later it will be logged in user)
    print(username)
    channel_info = {
        "_id": channel_name,
        "creator": username
    }
    # Add a new channel to the database
    app.db.insert_into_channel(channel_info)

    # Retrieve user from the database
    user = app.db.retrieve_from_user(username)
    if user:
        # Get list of channels for user, or create an empty list if it doesn't exist
        channels = user.get("channels", [])
        # Add new channel to list
        channels.append(channel_name)
        # Update user with new list of channels
        user["channels"] = channels
        app.db.update_user(user)  # Update user with new list
        return jsonify({'success': True})  # Return a success response
    else:
        print("No channel found")
        return jsonify({'success': False, 'error': 'User not found'})
