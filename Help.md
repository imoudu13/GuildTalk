# Jinja2 <br>
Jinja 2 is a template engine that's used for embedding python code into you html document<br>

Install it by entering this in your terminal for your ide:
```commandline
pip3 install jinja2
```


#  Database Connection <br>
This file contains some functions for connecting to the sql database and inserting/retrieving data. <br>

Import like so:

```python
# This will allow you to use all the functions in the file 
# You'll have to call them like so: DatabaseConnection.insertIntoUser(information)
import DatabaseConnections 

# if you only want to use a specific function import like so:
from DatabaseConnections import insertIntoUser
```
### User Table

To insert into the User table put the data in a tuple in the form: (username, password, firstname, lastname, email)<br>
Then pass the tuple in the function like so:

```python
import DatabaseConnections
from DatabaseConnections import insertIntoUser

username = "user"
password = "pass"
firstname = "first"
lastname = "last"
email = "email@gmail.com"

# put them in a tuple in this order:
information = (username, password, firstname, lastname, email)

# insert into table like so
DatabaseConnections.insertIntoUser(information)

# or do this if you imported a specific function
insertIntoUser(information)
```

To retrieve from the User table pass the username into the function like so: <br>
```python
import DatabaseConnections
from DatabaseConnections import retrieveFromUser

user_information1  = DatabaseConnections.retrieveFromUser("user")

# do this if you imported a specific function
user_information2 = retrieveFromUser("user")

# if the username is valid the function will return a dictionary with keys: 
# "username", "password", "first", "last", and "email"

# access them like so
username = user_information1["username"]
```

### Channel Table

To insert into the channel table put the data in a tuple with the form: (channelName, creatorUsername)
Then pass the tuple into the function:
```python
import DatabaseConnections 
from DatabaseConnections import insertIntoChannel

channelName = "name"
creatorUsername = "username"


# put them in a tuple in this order:
information = (channelName, creatorUsername)

# insert into table like so
DatabaseConnections.insertIntoChannel(information)

# or do this if you imported the specific function
insertIntoChannel(information)
```

To retrieve from the channel table pass the channel id into the function like so: <br>
```python
import DatabaseConnections
from DatabaseConnections import retrieveFromChannel

channel_information1  = DatabaseConnections.retrieveFromUser(1)

# do this if you imported a specific function
channel_information2 = retrieveFromChannel(1)

# if the channel id is valid the function will return a dictionary with keys: 
# "channel_id", "message_id", "sender", "content", "time"

# access them like so
username = channel_information1["channel_id"]
```

### Message Table

To insert into the Message table put the data in a tuple with the form: (senderUsername, channelID, receiverUsername, content, timeSent)
If the message is in a channel then put the receiver username as a blank string
If the message is being sent to a different user then assign the channel id a 0

Then pass the tuple into the function:
```python
import DatabaseConnections 
from DatabaseConnections import insertIntoMessage

senderUsername = "sender"
channelID = 1
receiverUsername = ""
content = "Wasup shorty"
timeSent = '2024-03-04 18:00:00'

# put them in a tuple in this order:
information = (senderUsername, channelID, receiverUsername, content, timeSent)

# insert into table like so
DatabaseConnections.insertIntoMessage(information)

# or do this if you imported the specific function
insertIntoMessage(information)
```

To retrieve from the Message table <br>
```python
import DatabaseConnections
from DatabaseConnections import retrieveMessagesBetweenUsers

# do this if you're getting messages between users, pass sender username and receiver usernames
between_users = retrieveMessagesBetweenUsers("sender", "receiver")
# the between_users function will return a dict with the keys "message_id", "content", and "time"

# or this if you're retrieving messages from a channel, pass the channel id into the function
from_channel  = DatabaseConnections.retrieveMessage(1)

# if the channel id is valid the function will return a list with dictionaries with keys: 
# "channel_id", "message_id", "sender", "content", "time"

# or the key will be: "message_id", "content", "time" if its between users
# access them like so
content = from_channel["content"]
```

### User Channel

After creating the channel and inserting it into the Channel table. <br>
Put the data in a tuple like so: (username, ChannelID, IsAdmin)
Insert the channel and the creator into the UserChannel Table.
For the creator of the channel their isAdmin property should be true.
For people who are invited to the channel update add them to the User Channel table as well with their isAdmin property as False
If they are given admin privileges make their isAdmin property True

```python
import DatabaseConnections
from DatabaseConnections import insertIntoChannel

username = "username"
channelID = 1
isAdmin = 'TRUE'

# put them in a tuple in this order:
information = (username, channelID, isAdmin)
```