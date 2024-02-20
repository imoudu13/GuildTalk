--User Table
CREATE TABLE User (
    username            VARCHAR(30),
    password            VARCHAR(30),
    firstname           VARCHAR(50),
    lastname            VARCHAR(50),
    email               VARCHAR(50),
    address             VARCHAR(50),
    city                VARCHAR(40),
    state               VARCHAR(20),
    postalCode          VARCHAR(20),
    country             VARCHAR(40),
    PRIMARY KEY (username)
);

--Channel Table
CREATE TABLE Channel(
    channelID PRIMARY KEY IDENTITY,
    channelName,
    creatorUsername (Foreign Key references User.username)
);

-- UserChannel Table (Many-to-Many Relationship)
-- This is used for tracking which users are in which channels
CREATE TABLE UserChannel (
    UserID INT REFERENCES User(username),
    ChannelID INT REFERENCES Channel(channelID),
    IsAdmin BOOLEAN,
    PRIMARY KEY (username, ChannelID) 
);

-- Message Table
CREATE TABLE Message (
    messageID INT PRIMARY KEY,
    senderUsername INT REFERENCES User(username),
    channelID INT REFERENCES Channel(channelID),
    receiverUsername INT REFERENCES User(username),
    content TEXT,
    timeSent TIMESTAMP  -- the time this message was sent
);