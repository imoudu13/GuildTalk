let username = document.currentScript.getAttribute('data-username');
let current_channel = ""
document.addEventListener('DOMContentLoaded', function() {
    //
    // Add an event listener to the textarea for the keypress event
    document.getElementById("message-input-id").addEventListener("keypress", handleKeyPress);

});
//function to redirect buttons to pages based on url
function redirectToPage(url) {
    window.location.href = url;
}
//Function to set current channel and load messages
function setChannel(channel){
    current_channel = channel;
    document.querySelector(".channel-title").innerText = current_channel;
    loadMessages();
}
function loadMessages(){
    let xhr = new XMLHttpRequest();
        //initializes new request of type POST and sends it to channel python method on server side
        xhr.open("POST", "/channel"); // Send POST request to server-side Python script
        //Indicates that the request body will contain JSON data
        xhr.setRequestHeader("Content-Type", "application/json");
        //function that's called when the request completes successfully
        xhr.onload = function() {
            //status === 200 means that it worked
            if (xhr.status === 200) {
                let response = JSON.parse(xhr.responseText);
                let messages = response['messages'];
                let messageContainer = document.querySelector('.message-container');
                messageContainer.innerHTML = ''; // Clear previous messages

                messages.forEach(function(message) {
                    let messageDiv = document.createElement('div');
                    messageDiv.classList.add('message');
                    messageDiv.textContent = message.sender + " || " + message.content;
                    messageContainer.appendChild(messageDiv);
                    //This is code to reverse the scroll direction of the message board
                    const messageContainer1 = document.querySelector('.message-container');
                    messageContainer1.scrollTop = messageContainer1.scrollHeight;
                });

                let userContainer = document.querySelector('.member-container');

                let users = response['users'];

                users.forEach(function (user){
                    let userButton = document.createElement('button');
                    userButton.classList.add('member');
                    let profileContainer = document.createElement("span");
                    profileContainer.className = "profile-container";

                    // Create image element for profile picture
                    let profilePicture = document.createElement("img");
                    profilePicture.src = "../static/images/GuildTalkLogoNoTextClear.png";
                    profilePicture.alt = "Profile Picture";

                    // Create span element for username
                    let usernameSpan = document.createElement("span");
                    usernameSpan.className = "username";
                    usernameSpan.textContent = user; // Assuming users is a variable holding username
                    // Append image and username spans to profile container
                    profileContainer.appendChild(profilePicture);
                    profileContainer.appendChild(usernameSpan);
                    userButton.appendChild(profileContainer);

                    userContainer.appendChild(userButton);
                });

                let adminContainer = document.querySelector('.admin-container');

                let admins = response['admins'];

                admins.forEach(function(admin){
                    let adminButton = document.createElement('button');
                    adminButton.classList.add('member');

                    let adminProfileContainer = document.createElement("span");
                    adminProfileContainer.className = "profile-container";

                    // Create image element for profile picture
                    let profilePicture = document.createElement("img");
                    profilePicture.src = "../static/images/GuildTalkLogoNoTextClear.png";
                    profilePicture.alt = "Profile Picture";

                    // Create span element for username
                    let usernameSpan = document.createElement("span");
                    usernameSpan.className = "username";
                    usernameSpan.textContent = admin; // Assuming users is a variable holding username
                    // Append image and username spans to profile container
                    adminProfileContainer.appendChild(profilePicture);
                    adminProfileContainer.appendChild(usernameSpan);
                    adminButton.appendChild(adminProfileContainer);

                    adminContainer.appendChild(adminButton);
                });
            } else {
                // Error handling
                console.error("Failed");
            }
        };
        xhr.send(JSON.stringify({loadMessage: "true", current_channel: current_channel }));
}
//function to give pop up to user for create channel button
function createChannel(){
    let channelName = prompt("Enter a channel name (1-20 Characters)");
    if(channelName !== null && channelName !== ""){
        if(channelName.length < 20){
        // Allows us to make http requests from client-side js
        let xhr = new XMLHttpRequest();
        //initializes new request of type POST and sends it to channel python method on server side
        xhr.open("POST", "/channel"); // Send POST request to server-side Python script
        //Indicates that the request body will contain JSON data
        xhr.setRequestHeader("Content-Type", "application/json");
        //function that's called when the request completes successfully
        xhr.onload = function() {
            //status === 200 means that it worked
            if (xhr.status === 200) {
                //parses JSON response from server into js object(newChannel)
                let newChannel = JSON.parse(xhr.responseText);
                // Here we update the html to include the new channel
                let channelContainer = document.querySelector('.select-channel-container');
                let newElement = document.createElement("button");
                newElement.classList.add('channel-button');
                newElement.textContent = channelName;
                channelContainer.appendChild(newElement);
            } else {
                // Error handling
                console.error("Failed to create channel.");
            }
        };
        xhr.send(JSON.stringify({channelName: channelName}));
        }
        else{
            alert("Channel name too long");
        }
    }
    else{
        alert("Please insert a channel name");
    }
}

// Function to put a message into html and send it to the controller
function handleKeyPress(event) {
    // Check if Enter key was pressed (keyCode 13)
    if (event.keyCode === 13) {
        event.preventDefault(); // Prevent the default behavior of the Enter key

        // Access the value of the textarea
        const message = document.getElementById("message-input-id").value;
        //Here we will set other values such as username, channel, and time. For now it is dummy data while functionality is being worked on
        user_name = "test_user"
        time = "8:56pm"

        let xhr = new XMLHttpRequest();
        //initializes new request of type POST and sends it to channel python method on server side
        xhr.open("POST", "/channel"); // Send POST request to server-side Python script
        //Indicates that the request body will contain JSON data
        xhr.setRequestHeader("Content-Type", "application/json");
        //function that's called when the request completes successfully
        xhr.onload = function() {
            //status === 200 means that it worked
            if (xhr.status === 200) {
                //parses JSON response from server into js object(newChannel)
                let newChannel = JSON.parse(xhr.responseText);
                // Here we update the html to include the new channel
                let messageContainer = document.querySelector('.message-container');
                let newElement = document.createElement("div");
                newElement.classList.add('message');
                newElement.textContent = username + " || " + message ;
                messageContainer.appendChild(newElement);
            } else {
                // Error handling
                console.error("Failed");
            }
        };
        xhr.send(JSON.stringify({text: message, user_name: user_name, time: time, curr_channel:current_channel }));
        // Clear the textarea after user submission
        document.getElementById("message-input-id").value = "";

    }
}



