DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Channel;
DROP TABLE IF EXISTS UserChannel;
DROP TABLE IF EXISTS Message;

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
    channelID PRIMARY KEY UNIQUE,
    channelName VARCHAR(50),
    creatorUsername VARCHAR(50),
    Foreign Key (creatorUsername) references User(username)
);

-- UserChannel Table (Many-to-Many Relationship)
-- This is used for tracking which users are in which channels
CREATE TABLE UserChannel (
    username VARCHAR(30) REFERENCES User(username),
    ChannelID INT REFERENCES Channel(channelID),
    IsAdmin BOOLEAN,
    PRIMARY KEY (username, ChannelID)
);

-- Message Table
CREATE TABLE Message (
    messageID INT PRIMARY KEY UNIQUE,
    senderUsername VARCHAR(30) REFERENCES User(username),
    channelID INT REFERENCES Channel(channelID),
    receiverUsername VARCHAR(30) REFERENCES User(username),
    content TEXT,
    timeSent TIMESTAMP  -- the time this message was sent
);

INSERT INTO User(username, password, firstname, lastname) VALUES('imoudu', 'guildtalk24', 'Imoudu', 'Ibrahim');
INSERT INTO User(username, password, firstname, lastname) VALUES('gavin', 'guildtalk24', 'Gavin', 'Ashworth');
INSERT INTO User(username, password, firstname, lastname) VALUES('nick', 'guildtalk24', 'Nicholas', 'Haydu');
INSERT INTO User(username, password, firstname, lastname) VALUES('preston', 'guildtalk24', 'Preston', 'Melvin');