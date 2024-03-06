# Jinja2 <br>
Jinja 2 is a template engine that's used for embedding python code into you html document<br>

Install it by entering this in your terminal for your ide:
```commandline
pip3 install jinja2
```


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

#insert like so
db.insertIntoUserChannel(information)
```