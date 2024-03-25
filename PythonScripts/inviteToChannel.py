from flask import jsonify
import app


def addUserToChannel(channel_name, username):
    # Retrieve user from the database
    user = app.db.retrieve_from_user(username)
    channel_information = app.db.retrieve_from_channel(channel_name)
    
    #adds user to channel info
    if channel_information:
        
        users = channel_information.get("users",[])
        users.append(username)
        channel_information["users"] = users
        
        app.db.update_channel(channel_name,channel_information)
    
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
