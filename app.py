from flask import Flask, render_template, request, jsonify
from DatabaseConnections import DatabaseConnect
from PythonScripts.createChannel import get_channels, add_channel
from PythonScripts.sendMessage import send_message, load_messages

# singleton instantiation of the database
db = DatabaseConnect()

app = Flask(__name__)


@app.route('/')
@app.route('/Home')
@app.route('/login')
def login():  # This is the default page. Below we will have other pages
    return render_template("login.html")


@app.route('/channel', methods=['GET', 'POST'])
def channel():  # This is the ChannelPage we will send variabls and stuff here to configure
    channels = []
    messages = []
    if request.method == 'POST':
        # get the data from the json request
        data = request.get_json()
        # Check if it is channel add request
        if 'channelName' in data:
            channel_name = data['channelName']
            add_channel(channel_name)
            response_data = {'status': 'Channel added successfully'}
            return jsonify(response_data)

            # Check if the request contains data for adding a message
        elif 'text' in data:
            # get the data from the post request
            text = data['text']
            username = "test_user"
            time = "12:01pm"
            curr_channel = data["curr_channel"]
            # Here we call our send message function to put the new message in the database
            send_message(text, username, time, curr_channel)
            response_data = {'status': 'Message added successfully'}
            return jsonify(response_data)

        elif 'loadMessage' in data:
            current_channel = data['current_channel']
            messages = load_messages(current_channel)
            return jsonify(messages=messages)
            # If the request is invalid/does not match what we expect
        else:
            response_data = {'status': 'Invalid request'}
            return jsonify(response_data)
    else:
        # on page load get the list of channels the user is in and send it to the channel page, so we can load them
        channels = get_channels('test_user')
    return render_template("ChannelPage.html", channels=channels, messages=messages)


@app.route('/profile')
def profile():  # This is the profile page we will send variables and stuff here to configure
    username = 'test_user'

    user_information = db.retrieve_from_user(username)

    return render_template("ProfilePage.html", userInformation=user_information)


# This function handles
@app.route('/update', methods=['POST', 'GET'])
def update():
    # Get username of the user from the form
    original_username = request.form["_id"]

    # get the users original information
    user_information = db.retrieve_from_user(original_username)

    # update the dictionary of the original users information with the new information entered by the user
    user_information["first"] = request.form["first"]
    user_information["last"] = request.form["last"]
    user_information["email"] = request.form["email"]
    user_information["password"] = request.form["password"]

    # use the user_information dict to update the database
    db.update_user(user_information)

    # render the page with the new info
    return render_template("ProfilePage.html", userInformation=user_information)


if __name__ == '__main__':
    app.run(debug=True)
