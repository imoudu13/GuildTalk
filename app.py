from flask import Flask, render_template, request, jsonify, redirect
from DatabaseConnections import DatabaseConnect

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
        # Extract the channel name from the POST request data
        data = request.get_json()
        channel_name = data.get('name')

        # Perform any necessary actions, such as creating a new channel in the database
        # For simplicity, let's assume we just want to return the channel name as JSON data
        response_data = {'name': channel_name}

        # Return a JSON response with the new channel data
        return jsonify(response_data)
    return render_template("ChannelPage.html")


@app.route('/profile')
def profile(): #This is the profile page we will send variables and stuff here to configure
    return render_template("ProfilePage.html")


if __name__ == '__main__':
    app.run(debug=True)
