# Flask and Jinja2<br>
Flask is our micro frame work. It will allow us to send/retrieve data from html pages, as well as render those html pages and add routes to the pages. <br>

Jinja 2 is a template engine that's used for embedding python code into your html document<br> <br>
Jijna 2 should come installed with flask. <br>
### Rendering pages <br>
This is how you add a route and render a page in flask: <br>
```python
from flask import Flask, render_template  #import the necessary functions
@app.route('/')  #this is the route to the page

#now create a function that renders the page
def home():
  return render_template("Home.hmtl")
```

### Sending data from python to html <br>
Fortunately most of this is done in the app.py file. <br>
We'll need to pass some data to files for flask to render them. Here's how: <br>
```python
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


# declare the path to the function, and its action methods, POST or GET or both
@app.route('/process_form', methods=['POST'])
def process_form():
    username = request.form['username']  it will return a dictionary so you can get the data using the keys
    email = request.form['email']

    # Process the data or save it to a database
    # For now, let's just print the values
    print(f"Received data: Username - {username}, Email - {email}")

    # Redirect to a success page or render a new template
    return render_template('success_page.html', username=username, email=email)
```

In the action attribute of the html page you must the same path that you have in the '@app.route' function. That way the form will send the data directly to that function.<br>
#  Database Connection <br>
This class contains some functions for connecting to the sql database and inserting/retrieving data. <br>

Note, all insertion functions will return true if it was inserted with no errors, and false otherwise
```python
# This will allow you to use all the functions in the class 
from DatabaseConnections import DatabaseConnect 


# We create only one instance of the class like so
db = DatabaseConnect()
# anytime we need a function we'll call it like so: db.insert_into_user(data)
```
### User Table

To insert into the User table put the data in a tuple in the form: (username, password, firstname, lastname, email)<br>
Then pass the tuple in the function like so:

```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

username = "user"
password = "pass"
firstname = "first"
lastname = "last"
email = "email@gmail.com"

# put them in a tuple in this order:
information = (username, password, firstname, lastname, email)

# insert into table like so
db.insert_into_user(information)

#if there are no errors it will return true, otherwise it will return false
```

To retrieve from the User table pass the username into the function like so: <br>
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

user_information1  = db.retrieve_from_user("user")

# if the username is valid the function will return a dictionary with keys: 
# "username", "password", "first", "last", and "email"

# access them like so
username = user_information1["username"]
```

### Channel Table

To insert into the channel table put the data in a tuple with the form: (channelName, creatorUsername)
Then pass the tuple into the function:
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

channelName = "name"
creatorUsername = "username"


# put them in a tuple in this order:
information = (channelName, creatorUsername)

# insert into table like so
db.insert_into_channel(information)


```

To retrieve from the channel table pass the channel id into the function like so: <br>
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

channel_information1  = db.retrieve_from_channel(1)


# if the channel id is valid the function will return a dictionary with keys: 
# "id", "name", "creator"

# access them like so
username = channel_information1["id"]
```

### Message Table

To insert into the Message table put the data in a tuple with the form: (senderUsername, channelID, receiverUsername, content, timeSent)
If the message is in a channel then put the receiver username as a blank string
If the message is being sent to a different user then assign the channel id a 0

Then pass the tuple into the function:
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

senderUsername = "sender"
channelID = 1
receiverUsername = ""
content = "Wasup shorty"
timeSent = '2024-03-04 18:00:00'

# put them in a tuple in this order:
information = (senderUsername, channelID, receiverUsername, content, timeSent)

# insert into table like so
db.insert_into_message(information)
```

To retrieve messages that have been sent in a channel use the retrieve message method <br>
```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

# the between_users function will return a dict with the keys "message_id", "content", and "time"

# or this if you're retrieving messages from a channel, pass the channel id into the function
from_channel  = db.retrieve_messages(1)

# if the channel id is valid the function will return a list of dictionaries with keys: 
# "channel_id", "message_id", "sender", "content", "time"
#use address 0 to get the first dict representing a message and then the "content" key to get the
content = from_channel[0]["content"]
```

### User Channel

After creating the channel and inserting it into the Channel table. <br>
Put the data in a tuple like so: (username, ChannelID, IsAdmin)
Insert the channel and the creator into the UserChannel Table.
For the creator of the channel their isAdmin property should be true.
For people who are invited to the channel update add them to the User Channel table as well with their isAdmin property as False
If they are given admin privileges make their isAdmin property True

```python
from DatabaseConnections import DatabaseConnect 

db = DatabaseConnect()

username = "username"
channelID = 1
isAdmin = 'TRUE'

# put them in a tuple in this order:
information = (username, channelID, isAdmin)

