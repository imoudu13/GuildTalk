**Colors** <br>
![img_1.png](DesignImages/ColorPalette.png) <br>
Here are the hex codes from the left to the right: <br>
#020412 Use this as the main background color<br>
#1d0515 Use this for the background of the sidebar<br>
#370617 Use this for the main background of channel messages<br>
#510513 Use these as accents<br>
#6a040f Use these as accents<br>
#ffffff This one is white <br>
<br>
**User requirements** <br>
Authentication: New users can register, returning users can log in. <br>
Channel: Users can create channels and invite others to join them. <br>
Admin: Admins are special users with permissions to manage channels. Initially, the creator of a channel is its admin, they can make other users admins as well. <br>
Admins of channels will be able to manage them, including tasks such as removing members and deleting messages posted by others. <br>
Messaging: All users can send messages, either privately to another user or in a channel that they are a part of. <br>
Users: Users can update their personal information, such as their name, last name, bio, email address, etc. <br>
<br>
**Functional & Non-Functional requirements** <br>
**Functional requirements** <br>
Authentication: Users will be able to enter their personal information, the system will then store the information in the database for later use. <br>
The user can only be registered if their username is unique. That will serve as their key for other processes. <br>
Users will be able to enter their username and password, the system will check if that information matches anything in the database and grant access if so. <br>
<br>
Channel: In the backend the channels that have been created will be stored in the database with a unique key to identify it. The username of the users in the channel will be stored in the database. <br>
<br>
Admin: With the permission of being an admin granted to you, a user will be able to delete certain users and certain messages and promote other users to an admin. <br>
Their username will be stored in the database as an admin. <br>
<br>
Messages: All message history will be stored in the database <br>
<br>
Users: A user's personal information will be stored in the database, there will be code that connects to the database and updates a user's information if they choose to. <br>
The keys of the channels this user is a part of will also be stored in the database. <br>
<br>
**Non-Functional requirements** <br>
**Product requirement:** <br>
-There will be help menus to help users who are lost or new to the system. <br>
-System will be reliable; no crashing or wait times over a second. <br>
-System will be able to cater to users of different skill levels; for experts certain shortcuts will be provided and for novices tools and hints will be available. <br>
External requirement: <br>
-This web app will run on all major browsers on desktop <br>
-We will implement some safety features to protect users personal information in accordance to the levels of privacy expected by regulatory bodies. <br>

**Design** <br>
This is the design for the user profile page, users can view their current information then and make changes if necessary.<br>
![img.png](DesignImages/UserProfilePage.png) <br>
This is the design for the channel page. All functionality is explained in the following annotations which can be better viewed through the following figma link [Figma design](https://www.figma.com/file/4kqgvEGAlwl8flLkyg1dJc/Untitled?type=design&node-id=0%3A1&mode=design&t=niq2g2iKaLOAK5XK-1). <br>
![image](https://github.com/imoudu13/GuildTalk/assets/111312815/fbfbf679-766c-494e-bcab-7a8013cbe986) <br>
![image](https://github.com/imoudu13/GuildTalk/assets/111312815/430fd48e-31c8-4bf3-a8cd-12c7f55ac7a1)

This is the design for the login and registration page where users can either sign into their GuildTalk account, or new users can create a new account.
![image](https://github.com/imoudu13/GuildTalk/blob/main/DesignImages/guildtalk-login.png)
![image](https://github.com/imoudu13/GuildTalk/blob/main/DesignImages/guildtalk-register.png)
