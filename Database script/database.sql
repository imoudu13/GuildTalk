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
    PRIMARY KEY (username)
);

--Channel Table
CREATE TABLE Channel(
    channelID INTEGER PRIMARY KEY,
    channelName VARCHAR(50),
    creatorUsername VARCHAR(50),
    Foreign Key (creatorUsername) references User(username)
);

-- UserChannel Table (Many-to-Many Relationship)
-- This is used for tracking which users are in which channels
CREATE TABLE UserChannel (
    username VARCHAR(30) REFERENCES User(username),
    ChannelID INTEGER REFERENCES Channel(channelID),
    IsAdmin BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (username, ChannelID)
);

-- Message Table
CREATE TABLE Message (
    messageID INTEGER PRIMARY KEY,
    senderUsername VARCHAR(30) REFERENCES User(username),
    channelID INTEGER REFERENCES Channel(channelID),
    receiverUsername VARCHAR(30) REFERENCES User(username),
    content TEXT,
    timeSent TIMESTAMP  -- the time this message was sent
);

INSERT INTO User(username, password, firstname, lastname) VALUES('imoudu', 'guildtalk24', 'Imoudu', 'Ibrahim');
INSERT INTO User(username, password, firstname, lastname) VALUES('gavin', 'guildtalk24', 'Gavin', 'Ashworth');
INSERT INTO User(username, password, firstname, lastname) VALUES('nick', 'guildtalk24', 'Nicholas', 'Haydu');
INSERT INTO User(username, password, firstname, lastname) VALUES('preston', 'guildtalk24', 'Preston', 'Melvin');

-- Inserting 30 users with common names and diverse email providers
INSERT INTO User(username, password, firstname, lastname, email)
VALUES
('john_doe', 'pass123', 'John', 'Doe', 'john.doe@gmail.com'),
('jane_smith', 'ilovecoding', 'Jane', 'Smith', 'jane.smith@yahoo.com'),
('michael_jones', 'musiclover', 'Michael', 'Jones', 'michael.jones@hotmail.com'),
('emily_brown', 'bookworm', 'Emily', 'Brown', 'emily.brown@gmail.com'),
('ryan_taylor', 'sportsfanatic', 'Ryan', 'Taylor', 'ryan.taylor@yahoo.com'),
('samantha_martin', 'adventuretime', 'Samantha', 'Martin', 'samantha.martin@gmail.com'),
('david_wilson', 'gamingmaster', 'David', 'Wilson', 'david.wilson@hotmail.com'),
('amy_hall', 'artisticmind', 'Amy', 'Hall', 'amy.hall@yahoo.com'),
('brian_miller', 'techie', 'Brian', 'Miller', 'brian.miller@gmail.com'),
('laura_jackson', 'naturelover', 'Laura', 'Jackson', 'laura.jackson@hotmail.com'),
('kevin_white', 'fitnessfreak', 'Kevin', 'White', 'kevin.white@yahoo.com'),
('jessica_adams', 'musiclover', 'Jessica', 'Adams', 'jessica.adams@gmail.com'),
('andrew_morris', 'bookworm', 'Andrew', 'Morris', 'andrew.morris@yahoo.com'),
('olivia_clark', 'artsy', 'Olivia', 'Clark', 'olivia.clark@gmail.com'),
('nathan_wright', 'sciencegeek', 'Nathan', 'Wright', 'nathan.wright@hotmail.com'),
('amanda_cook', 'foodie', 'Amanda', 'Cook', 'amanda.cook@yahoo.com'),
('justin_miller', 'movielover', 'Justin', 'Miller', 'justin.miller@gmail.com'),
('katie_adams', 'animallover', 'Katie', 'Adams', 'katie.adams@yahoo.com'),
('bryan_roberts', 'gamer', 'Bryan', 'Roberts', 'bryan.roberts@hotmail.com'),
('megan_carter', 'traveler', 'Megan', 'Carter', 'megan.carter@gmail.com'),
('eric_nelson', 'musican', 'Eric', 'Nelson', 'eric.nelson@yahoo.com'),
('sarah_hall', 'naturelover', 'Sarah', 'Hall', 'sarah.hall@hotmail.com'),
('jason_turner', 'fitnessfreak', 'Jason', 'Turner', 'jason.turner@gmail.com'),
('lily_thompson', 'artist', 'Lily', 'Thompson', 'lily.thompson@yahoo.com'),
('brent_cook', 'foodie', 'Brent', 'Cook', 'brent.cook@hotmail.com'),
('haley_martin', 'traveler', 'Haley', 'Martin', 'haley.martin@gmail.com'),
('derek_richards', 'techwhiz', 'Derek', 'Richards', 'derek.richards@yahoo.com'),
('emma_cole', 'gamer', 'Emma', 'Cole', 'emma.cole@hotmail.com'),
('ryan_murray', 'movielover', 'Ryan', 'Murray', 'ryan.murray@gmail.com'),
('sophia_riley', 'animallover', 'Sophia', 'Riley', 'sophia.riley@yahoo.com');

-- Creating 8 channels with specified creators
INSERT INTO Channel(channelID, channelName, creatorUsername)
VALUES
(1, 'Tech Talk', 'imoudu'),
(2, 'Music Lovers', 'gavin'),
(3, 'Sports Fanatics', 'nick'),
(4, 'Foodie Haven', 'preston');

-- Inserting users into channels
INSERT INTO UserChannel(username, ChannelID, IsAdmin) VALUES
('john_doe', 1, FALSE),
('jane_smith', 1, FALSE),
('michael_jones', 1, FALSE),
('ryan_taylor', 1, FALSE),
('samantha_martin', 2, FALSE),
('david_wilson', 2, TRUE),
('amy_hall', 2, FALSE),
('brian_miller', 2, FALSE),
('laura_jackson', 3, FALSE),
('kevin_white', 3, FALSE),
('jessica_adams', 3, FALSE),
('andrew_morris', 3, FALSE),
('olivia_clark', 4, FALSE),
('nathan_wright', 4, TRUE),
('amanda_cook', 4, FALSE),
('justin_miller', 4, TRUE),
('katie_adams', 1, TRUE),
('bryan_roberts', 2, FALSE),
('megan_carter', 3, FALSE),
('eric_nelson', 4, FALSE),
('sarah_hall', 1, FALSE),
('jason_turner', 2, FALSE),
('lily_thompson', 3, FALSE),
('brent_cook', 4, TRUE),
('haley_martin', 1, FALSE),
('derek_richards', 2, TRUE),
('emma_cole', 3, TRUE),
('ryan_murray', 4, FALSE),
('sophia_riley', 1, TRUE),
('john_doe', 2, FALSE),
('michael_jones', 3, FALSE),
('kevin_white', 4, FALSE);

-- Generate 30 random messages for Channel 1 with specific timestamps
INSERT INTO Message (senderUsername, channelID, receiverUsername, content, timeSent)
VALUES
    ('john_doe', 1, NULL, 'Hey, how is everyone doing?', '2024-03-03 09:15:00'),
    ('jane_smith', 1, NULL, 'I heard there is a new project coming up.', '2024-03-03 10:30:00'),
    ('michael_jones', 1, NULL, 'Any updates on the deadline?', '2024-03-03 11:45:00'),
    ('ryan_taylor', 1, NULL, 'Let me know if you need help with anything.', '2024-03-03 13:00:00'),
    ('john_doe', 1, NULL, 'The weather is great today!', '2024-03-03 14:15:00'),
    ('jane_smith', 1, NULL, 'Has anyone seen the latest movie?', '2024-03-03 15:30:00'),
    ('michael_jones', 1, NULL, 'I just finished reading a good book.', '2024-03-03 16:45:00'),
    ('ryan_taylor', 1, NULL, 'What is for lunch today?', '2024-03-03 18:00:00'),
    ('john_doe', 1, NULL, 'Let us schedule a meeting for next week.', '2024-03-03 19:15:00'),
    ('jane_smith', 1, NULL, 'I am working on the design mockups.', '2024-03-03 20:30:00'),
    ('michael_jones', 1, NULL, 'Do we have the client meeting tomorrow?', '2024-03-03 21:45:00'),
    ('ryan_taylor', 1, NULL, 'I will be out of the office this afternoon.', '2024-03-03 23:00:00'),
    ('john_doe', 1, NULL, 'I need feedback on the latest proposal.', '2024-03-04 09:15:00'),
    ('jane_smith', 1, NULL, 'Happy Friday, everyone!', '2024-03-04 10:30:00'),
    ('michael_jones', 1, NULL, 'The project is progressing well.', '2024-03-04 11:45:00'),
    ('ryan_taylor', 1, NULL, 'Let us aim to finish this by Friday.', '2024-03-04 13:00:00'),
    ('john_doe', 1, NULL, 'I found a bug in the code, looking into it now.', '2024-03-04 14:15:00'),
    ('jane_smith', 1, NULL, 'I will be on vacation next week.', '2024-03-04 15:30:00'),
    ('michael_jones', 1, NULL, 'Great job on the presentation!', '2024-03-04 16:45:00'),
    ('ryan_taylor', 1, NULL, 'Can someone help me with the database query?', '2024-03-04 18:00:00'),
    ('john_doe', 1, NULL, 'Coffee break, anyone?', '2024-03-04 19:15:00'),
    ('jane_smith', 1, NULL, 'Let us organize a team-building event.', '2024-03-04 20:30:00'),
    ('michael_jones', 1, NULL, 'Reminder: Submit your weekly reports.', '2024-03-04 21:45:00'),
    ('ryan_taylor', 1, NULL, 'I will be in the office early tomorrow.', '2024-03-04 23:00:00'),
    ('john_doe', 1, NULL, 'Has anyone tried the new restaurant nearby?', '2024-03-05 09:15:00'),
    ('jane_smith', 1, NULL, 'I am working on resolving the server issue.', '2024-03-05 10:30:00'),
    ('michael_jones', 1, NULL, 'We should plan a project retrospective.', '2024-03-05 11:45:00'),
    ('ryan_taylor', 1, NULL, 'I have a suggestion for the next sprint.', '2024-03-05 13:00:00'),
    ('john_doe', 1, NULL, 'Happy Monday! Let us make it a productive week.', '2024-03-05 14:15:00'),
    ('jane_smith', 1, NULL, 'Do we have any updates from the client?', '2024-03-05 15:30:00');

-- Generate 30 random messages for Channel 2 with specific timestamps
INSERT INTO Message (senderUsername, channelID, receiverUsername, content, timeSent)
VALUES
    ('samantha_martin', 2, NULL, 'Any plans for the weekend?', '2024-03-03 09:15:00'),
    ('david_wilson', 2, NULL, 'I am reviewing the latest code changes.', '2024-03-03 10:30:00'),
    ('amy_hall', 2, NULL, 'Do we have a status update on the client meeting?', '2024-03-03 11:45:00'),
    ('brian_miller', 2, NULL, 'I will be away for the next two days.', '2024-03-03 13:00:00'),
    ('samantha_martin', 2, NULL, 'Working on the marketing presentation.', '2024-03-03 14:15:00'),
    ('david_wilson', 2, NULL, 'Discussing the project timeline in the next meeting.', '2024-03-03 15:30:00'),
    ('amy_hall', 2, NULL, 'Who is responsible for the upcoming release?', '2024-03-03 16:45:00'),
    ('brian_miller', 2, NULL, 'I will handle the server maintenance this weekend.', '2024-03-03 18:00:00'),
    ('samantha_martin', 2, NULL, 'Feedback on the new design concepts?', '2024-03-03 19:15:00'),
    ('david_wilson', 2, NULL, 'Can we schedule a quick sync tomorrow morning?', '2024-03-03 20:30:00'),
    ('amy_hall', 2, NULL, 'Planning the agenda for the team meeting.', '2024-03-03 21:45:00'),
    ('brian_miller', 2, NULL, 'I have updated the project documentation.', '2024-03-03 23:00:00'),
    ('samantha_martin', 2, NULL, 'Reviewing the user feedback from the latest release.', '2024-03-04 09:15:00'),
    ('david_wilson', 2, NULL, 'Let us discuss the budget allocation for the next quarter.', '2024-03-04 10:30:00'),
    ('amy_hall', 2, NULL, 'Has anyone tested the new feature on the staging server?', '2024-03-04 11:45:00'),
    ('brian_miller', 2, NULL, 'I am working on the technical documentation.', '2024-03-04 13:00:00'),
    ('samantha_martin', 2, NULL, 'Preparing for the client demo this afternoon.', '2024-03-04 14:15:00'),
    ('david_wilson', 2, NULL, 'I will be on a business trip next week.', '2024-03-04 15:30:00'),
    ('amy_hall', 2, NULL, 'I need input on the project timeline from the team.', '2024-03-04 16:45:00'),
    ('brian_miller', 2, NULL, 'Is everyone up to date on the latest project updates?', '2024-03-04 18:00:00'),
    ('samantha_martin', 2, NULL, 'Reminder: Submit your time sheets by Friday.', '2024-03-04 19:15:00'),
    ('david_wilson', 2, NULL, 'How are we handling the server downtime this weekend?', '2024-03-04 20:30:00'),
    ('amy_hall', 2, NULL, 'I will be in a training session most of tomorrow.', '2024-03-04 21:45:00'),
    ('brian_miller', 2, NULL, 'Do we have an update on the project budget?', '2024-03-04 23:00:00'),
    ('samantha_martin', 2, NULL, 'Let us plan a team-building activity for next month.', '2024-03-05 09:15:00'),
    ('david_wilson', 2, NULL, 'Reviewing the feedback from the client meeting.', '2024-03-05 10:30:00'),
    ('amy_hall', 2, NULL, 'Any issues with the latest software release?', '2024-03-05 11:45:00'),
    ('brian_miller', 2, NULL, 'I will be available for support during the weekend.', '2024-03-05 13:00:00'),
    ('samantha_martin', 2, NULL, 'I am working on the presentation for the investor meeting.', '2024-03-05 14:15:00'),
    ('david_wilson', 2, NULL, 'Reminder: Complete the mandatory security training.', '2024-03-05 15:30:00');

-- Generate 30 random messages for Channel 3 with specific timestamps
INSERT INTO Message (senderUsername, channelID, receiverUsername, content, timeSent)
VALUES
    ('laura_jackson', 3, NULL, 'Good morning, team! Any updates for today?', '2024-03-03 09:15:00'),
    ('kevin_white', 3, NULL, 'I will be in a client meeting this afternoon.', '2024-03-03 10:30:00'),
    ('jessica_adams', 3, NULL, 'I am working on the project timeline.', '2024-03-03 11:45:00'),
    ('andrew_morris', 3, NULL, 'Has anyone reviewed the latest design mockups?', '2024-03-03 13:00:00'),
    ('laura_jackson', 3, NULL, 'Planning a team lunch for next week.', '2024-03-03 14:15:00'),
    ('kevin_white', 3, NULL, 'Any feedback on the marketing campaign?', '2024-03-03 15:30:00'),
    ('jessica_adams', 3, NULL, 'I need assistance with the client proposal.', '2024-03-03 16:45:00'),
    ('andrew_morris', 3, NULL, 'Working on optimizing the website performance.', '2024-03-03 18:00:00'),
    ('laura_jackson', 3, NULL, 'Let us schedule a project review meeting.', '2024-03-03 19:15:00'),
    ('kevin_white', 3, NULL, 'Discussing the budget for the next quarter.', '2024-03-03 20:30:00'),
    ('jessica_adams', 3, NULL, 'Who is handling the upcoming event coordination?', '2024-03-03 21:45:00'),
    ('andrew_morris', 3, NULL, 'I will be away on vacation next week.', '2024-03-03 23:00:00'),
    ('laura_jackson', 3, NULL, 'Reviewing the progress on the client deliverables.', '2024-03-04 09:15:00'),
    ('kevin_white', 3, NULL, 'Let us plan a team-building activity for next month.', '2024-03-04 10:30:00'),
    ('jessica_adams', 3, NULL, 'Preparing for the team presentation tomorrow.', '2024-03-04 11:45:00'),
    ('andrew_morris', 3, NULL, 'Discussing the latest industry trends in our sector.', '2024-03-04 13:00:00'),
    ('laura_jackson', 3, NULL, 'Reminder: Complete your training modules.', '2024-03-04 14:15:00'),
    ('kevin_white', 3, NULL, 'Any issues with the software updates?', '2024-03-04 15:30:00'),
    ('jessica_adams', 3, NULL, 'Finalizing the project proposal for client approval.', '2024-03-04 16:45:00'),
    ('andrew_morris', 3, NULL, 'I have some new ideas for the upcoming project.', '2024-03-04 18:00:00'),
    ('laura_jackson', 3, NULL, 'Reminder: Submit your weekly reports.', '2024-03-04 19:15:00'),
    ('kevin_white', 3, NULL, 'Let us celebrate the successful project completion!', '2024-03-04 20:30:00'),
    ('jessica_adams', 3, NULL, 'I will be out of the office for a client visit.', '2024-03-04 21:45:00'),
    ('andrew_morris', 3, NULL, 'Discussing potential improvements for our workflow.', '2024-03-04 23:00:00'),
    ('laura_jackson', 3, NULL, 'How are we handling the client feedback?', '2024-03-05 09:15:00'),
    ('kevin_white', 3, NULL, 'Reviewing the project timeline for any adjustments.', '2024-03-05 10:30:00'),
    ('jessica_adams', 3, NULL, 'I will be leading the training session next week.', '2024-03-05 11:45:00'),
    ('andrew_morris', 3, NULL, 'Working on resolving the reported software issues.', '2024-03-05 13:00:00'),
    ('laura_jackson', 3, NULL, 'Let us plan for a knowledge-sharing session.', '2024-03-05 14:15:00'),
    ('kevin_white', 3, NULL, 'Is everyone on track with their assigned tasks?', '2024-03-05 15:30:00');

-- Generate 30 random messages for Channel 4 with specific timestamps
INSERT INTO Message (senderUsername, channelID, receiverUsername, content, timeSent)
VALUES
    ('olivia_clark', 4, NULL, 'Good morning, team! Any updates for today?', '2024-03-03 09:15:00'),
    ('nathan_wright', 4, NULL, 'I will be in a client meeting this afternoon.', '2024-03-03 10:30:00'),
    ('amanda_cook', 4, NULL, 'I am working on the project timeline.', '2024-03-03 11:45:00'),
    ('justin_miller', 4, NULL, 'Has anyone reviewed the latest design mockups?', '2024-03-03 13:00:00'),
    ('olivia_clark', 4, NULL, 'Planning a team lunch for next week.', '2024-03-03 14:15:00'),
    ('nathan_wright', 4, NULL, 'Any feedback on the marketing campaign?', '2024-03-03 15:30:00'),
    ('amanda_cook', 4, NULL, 'I need assistance with the client proposal.', '2024-03-03 16:45:00'),
    ('justin_miller', 4, NULL, 'Working on optimizing the website performance.', '2024-03-03 18:00:00'),
    ('olivia_clark', 4, NULL, 'Let us schedule a project review meeting.', '2024-03-03 19:15:00'),
    ('nathan_wright', 4, NULL, 'Discussing the budget for the next quarter.', '2024-03-03 20:30:00'),
    ('amanda_cook', 4, NULL, 'Who is handling the upcoming event coordination?', '2024-03-03 21:45:00'),
    ('justin_miller', 4, NULL, 'I will be away on vacation next week.', '2024-03-03 23:00:00'),
    ('olivia_clark', 4, NULL, 'Reviewing the progress on the client deliverables.', '2024-03-04 09:15:00'),
    ('nathan_wright', 4, NULL, 'Let us plan a team-building activity for next month.', '2024-03-04 10:30:00'),
    ('amanda_cook', 4, NULL, 'Preparing for the team presentation tomorrow.', '2024-03-04 11:45:00'),
    ('justin_miller', 4, NULL, 'Discussing the latest industry trends in our sector.', '2024-03-04 13:00:00'),
    ('olivia_clark', 4, NULL, 'Reminder: Complete your training modules.', '2024-03-04 14:15:00'),
    ('nathan_wright', 4, NULL, 'Any issues with the software updates?', '2024-03-04 15:30:00'),
    ('amanda_cook', 4, NULL, 'Finalizing the project proposal for client approval.', '2024-03-04 16:45:00'),
    ('justin_miller', 4, NULL, 'I have some new ideas for the upcoming project.', '2024-03-04 18:00:00'),
    ('olivia_clark', 4, NULL, 'Reminder: Submit your weekly reports.', '2024-03-04 19:15:00'),
    ('nathan_wright', 4, NULL, 'Let us celebrate the successful project completion!', '2024-03-04 20:30:00'),
    ('amanda_cook', 4, NULL, 'I will be out of the office for a client visit.', '2024-03-04 21:45:00'),
    ('justin_miller', 4, NULL, 'Discussing potential improvements for our workflow.', '2024-03-04 23:00:00'),
    ('olivia_clark', 4, NULL, 'How are we handling the client feedback?', '2024-03-05 09:15:00'),
    ('nathan_wright', 4, NULL, 'Reviewing the project timeline for any adjustments.', '2024-03-05 10:30:00'),
    ('amanda_cook', 4, NULL, 'I will be leading the training session next week.', '2024-03-05 11:45:00'),
    ('justin_miller', 4, NULL, 'Working on resolving the reported software issues.', '2024-03-05 13:00:00'),
    ('olivia_clark', 4, NULL, 'Let us plan for a knowledge-sharing session.', '2024-03-05 14:15:00'),
    ('nathan_wright', 4, NULL, 'Is everyone on track with their assigned tasks?', '2024-03-05 15:30:00');