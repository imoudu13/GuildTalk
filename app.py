from flask import Flask, render_template, request, jsonify, redirect, flash, url_for, session
from PythonScripts.registerLogin import RegistrationForm, LoginForm, ResetForm, create_user
from DatabaseConnections import DatabaseConnect
from PythonScripts.createChannel import get_channels, add_channel
from PythonScripts.sendMessage import send_message, load_messages

# singleton instantiation of the database
db = DatabaseConnect()

app = Flask(__name__)

# secret key to prevent cookie modification for login / registration security
app.config['SECRET_KEY'] = '1fe076e0a441ec065328b7506f51d7bb'


@app.route('/')
@app.route('/Home')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = None  # Define user variable here
    if form.validate_on_submit():
        username = form.username.data
        user = db.retrieve_from_user(username)
        if user and user['password'] == form.password.data:
            session['user'] = user
            session['username'] = username
            return redirect(url_for('channel'))
        else:
            flash('Login unsuccessful, please check username and password', 'danger')
    return render_template("login.html", title='Login', form=form, user=user)


@app.route('/register', methods=['GET', 'POST'])  # This is the registration page where users can create new accounts
def register():
    form = RegistrationForm()

    # check if the information meets requirements
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # send info to the create user def    
        create_user(firstname, lastname, username, email, password)

        # message to let the user know they created a new account
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    form = ResetForm()
    if form.validate_on_submit():
        flash(f'Your reset email has been sent', 'success')
        return redirect(url_for('login'))
    return render_template("reset.html", title='Reset', form=form)


@app.route('/channel', methods=['GET', 'POST'])
def channel():  # This is the ChannelPage we will send variabls and stuff here to configure
    username = session.get('username')
    channels = []
    messages = []
    users_in_channel = None

    if request.method == 'POST':
        # get the data from the json request
        data = request.get_json()
        # Check if it is channel add request
        if 'channelName' in data:
            channel_name = data['channelName']
            add_channel(channel_name, username)
            response_data = {'status': 'Channel added successfully'}
            return jsonify(response_data)

            # Check if the request contains data for adding a message
        elif 'text' in data:
            # get the data from the post request
            text = data['text']
            username = username
            time = "12:01pm"
            curr_channel = data["curr_channel"]
            # Here we call our send message function to put the new message in the database
            send_message(text, username, time, curr_channel)
            response_data = {'status': 'Message added successfully'}
            return jsonify(response_data)

        elif 'loadMessage' in data:
            current_channel = data['current_channel']
            messages = load_messages(current_channel)
            channel_info = db.retrieve_from_channel(current_channel)
            return jsonify(messages=messages, users=channel_info['users'], admins=channel_info['admins'])
            # If the request is invalid/does not match what we expect
        else:
            response_data = {'status': 'Invalid request'}
            return jsonify(response_data)
    else:
        # on page load get the list of channels the user is in and send it to the channel page, so we can load them
        channels = get_channels(username)
    return render_template("ChannelPage.html", channels=channels, messages=messages, username=username, users_in_channel=users_in_channel)


@app.route('/profile')
def profile():  # This is the profile page we will send variables and stuff here to configure
    username = session.get('username')

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
