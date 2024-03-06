from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Home')
@app.route('/Login')
def login(): #This is the default page. Below we will have other pages
    return render_template("login.html")


@app.route('/Channel')
def channel(): #This is the ChannelPage we will send variabls and stuff here to configure
    return render_template("ChannelPage.html")


@app.route('/Profile')
def profile(): #This is the profile page we will send variables and stuff here to configure
    return render_template("ProfilePage.html")


if __name__ == '__main__':
    app.run(debug=True)
