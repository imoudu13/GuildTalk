from flask import jsonify
from DatabaseConnections import DatabaseConnect
import app

db = DatabaseConnect()


def deleteMessage(index, channel):
    selected_channel = db.retrieve_document(channel, "Channel")

    if selected_channel is None:
        return jsonify({'success': False, 'error': 'Channel not found'})

    messages = selected_channel.get("messages", [])
    if index < 0 or index >= len(messages):
        return jsonify({'success': False, 'error': 'Invalid message index'})

    del messages[index]
    selected_channel["messages"] = messages
    db.update(channel, selected_channel, "Channel")
    return jsonify({'success': True})
