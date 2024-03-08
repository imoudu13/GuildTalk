from flask import Flask, render_template, request, jsonify, redirect
from DatabaseConnections import DatabaseConnect
from PythonScripts.createChannel import get_channels, add_channel

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
        # Extracting the data from the post request
        data = request.get_json()
        #channel name that we will add to db
        channel_name = data.get('channelName')


        # For simplicity, let's assume we just want to return the channel name as JSON data
        response_data = {'name': channel_name}

        # Return a JSON response with the new channel data
        return jsonify(response_data)
    else:
        #on page load get the list of channels the user is in and send it to the channel page so we can load them
        channels = get_channels('john_doe')
    return render_template("ChannelPage.html", channels=channels)


@app.route('/profile')
def profile(): #This is the profile page we will send variables and stuff here to configure
    return render_template("ProfilePage.html")


if __name__ == '__main__':
    app.run(debug=True)
