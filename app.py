from flask import Flask, render_template, request, jsonify, redirect
from DatabaseConnections import DatabaseConnect
from PythonScripts.createChannel import get_channels, add_channel

# singleton instantiation of the database
db = DatabaseConnect()

app = Flask(__name__)


@app.route('/')
@app.route('/Home')
@app.route('/login')
def login(): #This is the default page. Below we will have other pages
    return render_template("login.html")


@app.route('/channel', methods=['GET', 'POST'])
def channel(): #This is the ChannelPage we will send variabls and stuff here to configure
    if request.method == 'POST':
        #get the data from the json request
        data = request.get_json()
        #Check if it is channel add request
        if 'channelName' in data:
            channel_name = data['channelName']
            add_channel(channel_name)
            response_data = {'status': 'Channel added successfully'}
            return jsonify(response_data)

            # Check if the request contains data for adding a message
        elif 'message' in data:
            message = data['message']
            # Here we will do something with the messages later
            response_data = {'status': 'Message added successfully'}
            return jsonify(response_data)

            # If the request is invalid/does not match what we expect
        else:
            response_data = {'status': 'Invalid request'}
            return jsonify(response_data)
    else:
        #on page load get the list of channels the user is in and send it to the channel page so we can load them
        channels = get_channels('test_user')
    return render_template("ChannelPage.html", channels=channels)


@app.route('/Profile')
def profile():  # This is the profile page we will send variables and stuff here to configure
    username = 'imoudu'

    user_information = db.retrieve_from_user(username)

    return render_template("ProfilePage.html", userInformation=user_information)


# This function handles
@app.route('/Update', methods=['POST', 'GET'])
def update():
    original = request.form['original_username']

    # get the original information
    user_information = db.retrieve_from_user(original)

    # the html form is formatted in a way such that the default text is the original information
    # So if nothing was changed then all the information will remain the same
    user_information["username"] = request.form['username']
    user_information["first"] = request.form['first']
    user_information["last"] = request.form['last']
    user_information["email"] = request.form['email']
    user_information["password"] = request.form['password']

    # create the tuple for updating
    # "UPDATE User SET username = ?, firstname = ?, lastname = ?, email = ?, password = ? WHERE username  = ?"
    information = (user_information["username"], user_information["first"], user_information["last"], user_information["email"], user_information["password"], original)

    db.update_user(information)

    return render_template("ProfilePage.html", userInformation=user_information)


if __name__ == '__main__':
    app.run(debug=True)
