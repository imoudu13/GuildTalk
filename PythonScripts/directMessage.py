from flask import jsonify
from DatabaseConnections import DatabaseConnect

db = DatabaseConnect()


def add_channelDirectMessage(userToMessage, username):
    # Set data (for now we will use boilerplate name. Later it will be logged in user)
    userWeAreMessaging = db.retrieve_document(userToMessage, "User")
    if userWeAreMessaging is None:
        return jsonify({'success': False, 'error': 'User not found'})
    channel_info = {
        "_id": userToMessage + " + " + username,
        "creator": username,
        "users": [userToMessage]
    }
    # Add a new channel to the database
    db.insert_into_channel(channel_info)

    # Retrieve user from the database
    user = db.retrieve_document(username, "User")
    if userWeAreMessaging:
        # Get list of channels for user, or create an empty list if it doesn't exist
        channels = userWeAreMessaging.get("channels", [])
        # Add new channel to list
        channels.append(userToMessage + " + " + username)
        # Update user with new list of channels
        userWeAreMessaging["channels"] = channels
        db.update(userWeAreMessaging['_id'], userWeAreMessaging, "User")  # Update user with new list

        if user:
            # Get list of channels for user, or create an empty list if it doesn't exist
            channels = user.get("channels", [])
            # Add new channel to list
            channels.append(userToMessage + " + " + username)
            # Update user with new list of channels
            user["channels"] = channels
            db.update(user['_id'], user, "User")  # Update user with new list
            return jsonify({'success': True})  # Return a success response
        else:
            return jsonify({'success': False, 'error': 'User not found'})

    else:
        return jsonify({'success': False, 'error': 'User not found'})


