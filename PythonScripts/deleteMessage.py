from flask import jsonify
import app


def deleteMessage(index, channel):
    selected_channel = app.db.retrieve_from_channel(channel)
    if selected_channel is None:
        return jsonify({'success': False, 'error': 'Channel not found'})

    messages = selected_channel.get("messages", [])
    if index < 0 or index >= len(messages):
        return jsonify({'success': False, 'error': 'Invalid message index'})

    del messages[index]
    selected_channel["messages"] = messages
    app.db.update_channel(channel, selected_channel)
    return jsonify({'success': True})

