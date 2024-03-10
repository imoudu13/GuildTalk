#  Database Connection <br>
This class contains some functions for connecting to the MongoDB and inserting/retrieving/updating data. <br>

Note, all insertion functions will return true if it was inserted with no errors, and false otherwise
```python
# This will allow you to use all the functions in the class 
from DatabaseConnections import DatabaseConnect 


# We create only one instance of the class like so
db = DatabaseConnect()
# anytime we need a function we'll call it like so: db.insert_into_user(data)
```
### User Table

To insert into the User table put the data in a dictionary with keys:
"_id", this is the username <br>
"firstname", this is the firstname <br>
"lastname", last name <br>
"email", email <br>
"password", password <br>
<br>
Then pass the dictionary into the function like so:<br>

Data must be passed in that format otherwise it will cause errors later. <br>

In addition, that function adds an empty list that will hold the channels that user is a part of.

The "_id" is vital, it will be used to retrieve that users information later. <br>
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

user_data = {
            "_id": "test_user",
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        }

# insert into table like so
db.insert_into_user(user_data)

#if there are no errors it will return true, otherwise it will return false
```
Here is what a document in the User Collection looks like on Mongo: <br>
![image](/DesignImages/UserCollection.png) <br>
To retrieve from the User table pass the username into the function like so: <br>
If the username is valid the function will return a dictionary with keys: 
"_id" <br>
"firstname" <br>
"lastname" <br>
"email" <br>
"password" <br>
"channels" <br>
The value at "channels" is a list that has the names of all the channels this user is a part of <br>
So if you want to get all the channels for the user, retrieve the user, collect their list then do what you want <br>
The values in that list are the names of the channels.
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

user_information1  = db.retrieve_from_user("user")

# access them like so
username = user_information1["_id"]
```

### Channel Table
The
To insert into the channel table put the data in a dictionary with keys: <br>
"_id", this is the name of the channel
"creator", this is the name of the user who created the Channel

Then pass the dictionary into the function:
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

channel_info = {
            "_id": "test_channel",
            "creator": "test_user"
        }

# insert into table like so
db.insert_into_channel(channel_info)
```
That function will also add a list of users, a list of admins. For both of those lists it will put the creator in them <br>
Lastly, it creates a list of messages that are empty to start. <br>

Here is what a document in the Channel Collection looks like on Mongo: <br>

![image](/DesignImages/ChannelCollection.png) <br>

So anytime a message is sent, user is added, need to check if someone is a admin, retrieve from the Channel Collection. <br>
To retrieve from the channel table pass the channel id into the function like so: <br>
These are the keys when the dictionary is returned:<br>
"_id", the name of the channel <br>
"admins", list of admins <br>
"users", list of users <br>
"messages", list of message dictionaries<br>
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

channel_information1  = db.retrieve_from_channel("test_channel")


# if the channel id is valid the function will return a dictionary with keys: 
# "id", "name", "creator"

# access them like so
channel_admins = channel_information1["admins"]
```

If you want to insert a message, add a new user or admin, retrieve from the channel using its id, then do one of these <br>

```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

channel_information1  = db.retrieve_from_channel("test_channel")


# if the channel id is valid the function will return a dictionary with keys: 
# "id", "name", "creator"

# You don't need to get all of these lists of you only want to add to one
# Just doing this for example
messages = channel_information1["messages"]
admins = channel_information1["admins"]
users = channel_information1["users"]
name_channel = channel_information1["_id"]
# Do this for creating a message
message = {
    "sender": "user",
    "content": "some_string",
    "timestamp": "time_goes_here"
}

messages.append(message)

# make sure to append new admins to admin list and user list
admins.append("new_admin")
users.append("new_admin")

# Now put those lists back into the channel infromation dictionary
channel_information1["users"] = users
channel_information1["admins"] = admins
channel_information1["messages"] = messages

# Then call the update channel function from the database3 
# You'll need to pass the name of the channel in there as well.
db.update_channel(name_channel, channel_information1)
# Do this for adding a
```

Note if you need to update a user document you'll need to do something along those lines then call the update user function

# Flask and Jinja2<br>
Flask is our micro frame work. It will allow us to send/retrieve data from html pages, as well as render those html pages and add routes to the pages. <br>

Jinja 2 is a template engine that's used for embedding python code into your html document<br> <br>
Jijna 2 should come installed with flask. <br>
### Rendering pages <br>
This is how you add a route and render a page in flask: <br>
```python
from flask import Flask, render_template  #import the necessary functions
app = Flask(__name__)

@app.route('/')  #this is the route to the page

#now create a function that renders the page
def home():
  return render_template("Home.hmtl")
```

### Sending data from python to html <br>
Fortunately most of this is done in the app.py file. <br>
We'll need to pass some data to files for flask to render them. Here's how: <br>
```python
from flask import Flask, render_template  #import the necessary functions
app = Flask(__name__)
def home():
  nameOfList = "Favorite fruits"
  fruitList = ["Apple", "Pineapple", "Pear", "Banana", "Watermelon"]

  #send it to whatever page you want to render like so
  return render_template("RandomPage.html", name = nameOfList, fruits = fruitList)
```
### Embedding using Jinja 2 <br>
That will send the string and the list to the html page, in the html page the names for those variables will be name and fruits <br>
Go to that page and display the data like so: <br>
```html
<!-- This creates an ordered list and displays each item in the list -->
<h1> {{ name }} </h1> <!-- Use double parentheses for variables, put them in between html tags -->
<ol>
  <!-- Put for loops inside parentheses with percentages like so -->
  {% for fruit in fruits %}
      <li> {{ fruit }} </li>  
  {% endfor %}  <!-- end for loops like so -->
</ol>
```

All of that is the same thing as this: <br>
```html
<h1>Favorite fruits</h1>

    <ol>
        <li>Apple</li>
        <li>Pineapple</li>
        <li>Pear</li>
        <li>Banana</li>
        <li>Watermelon</li>
    </ol>
```

### Sending data to a python file <br>

This is how you send data to a python file: <br>

```html
<h1>Registration Form</h1>

    <form method="POST" action="/process_form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <input type="submit" value="Submit">
    </form>
```
```python
from flask import Flask, render_template, request  #first import the request function
app = Flask(__name__)

# declare the path to the function, and its action methods, POST or GET or both
@app.route('/process_form', methods=['POST'])
def process_form():
    username = request.form['username']  # it will return a dictionary so you can get the data using the keys
    email = request.form['email']

    # Process the data or save it to a database
    # For now, let's just print the values
    print(f"Received data: Username - {username}, Email - {email}")

    # Redirect to a success page or render a new template
    return render_template('success_page.html', username=username, email=email)
```

In the action attribute of the html page you must the same path that you have in the '@app.route' function. That way the form will send the data directly to that function.<br>
