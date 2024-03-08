from flask import Flask, render_template, request
from DatabaseConnections import DatabaseConnect

db = DatabaseConnect()

app = Flask(__name__)


@app.route('/')
@app.route('/Home')
@app.route('/Login')
def login():  # This is the default page. Below we will have other pages
    return render_template("login.html")


@app.route('/Channel')
def channel():  # This is the ChannelPage we will send variables and stuff here to configure
    return render_template("ChannelPage.html")


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
