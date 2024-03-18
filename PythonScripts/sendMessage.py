from flask import jsonify
import app


def send_message(text, username, time, curr_channel):
    username = username
    time = "12:01pm"
    # Add a new channel to the database
    channel_information1 = app.db.retrieve_from_channel(curr_channel)

    # Check if channel information is retrieved successfully
    if channel_information1 is None:
        # Channel does not exist, create a new one
        channel_information1 = {"messages": []}

    # You don't need to get all of these lists if you only want to add to one
    messages = channel_information1.get("messages", [])

    # Do this for creating a message
    message = {
        "sender": username,
        "content": text,
        "timestamp": time
    }

    # Append new message to messages
    messages.append(message)

    # Now put those lists back into the channel information dictionary
    channel_information1["messages"] = messages

    # Then call the update channel function from the database3
    # You'll need to pass the name of the channel in there as well.
    app.db.update_channel(curr_channel, channel_information1)
    return jsonify({'success': True})  # Return a success response


def load_messages(channel):
    # Fetch channels from the database
    selected_channel = app.db.retrieve_from_channel(channel)
    if selected_channel is None:
        return []
    messages = selected_channel["messages"]
    return messages
