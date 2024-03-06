from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login(): #This is the default page. Below we will have other pages
    return render_template("login.html")


@app.route('/Channel')
def channel(): #This is the default page. Below we will have other pages
    return render_template("ChannelPage.html")


@app.route('/Profile')
def profile(): #This is the default page. Below we will have other pages
    return render_template("ProfilePage.html")


if __name__ == '__main__':
    app.run(debug=True)
