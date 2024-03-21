from flask import jsonify
import app


def deleteMessage(index, channel):
    selected_channel = app.db.retrieve_from_channel(channel)
    if selected_channel is None:
        return []
    messages = selected_channel["messages"]
    messages.remove(index)
    selected_channel["messages"] = messages
    app.db.update_channel(channel, selected_channel)
    return jsonify({'success': False, 'error': 'User not found'})
