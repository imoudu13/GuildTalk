let username = document.currentScript.getAttribute('data-username');
let current_channel = ""
let users = null;
let admins = null;

document.addEventListener('DOMContentLoaded', function () {
    //
    // Add an event listener to the textarea for the keypress event
    document.getElementById("message-input-id").addEventListener("keypress", handleKeyPress);
    document.querySelector('.promote-button').addEventListener("click", promote);
    document.querySelector('.remove-button').addEventListener("click", handleKeyPress);
});

//function to redirect buttons to pages based on url
function redirectToPage(url) {
    window.location.href = url;
}

//Function to set current channel and load messages
function setChannel(channel) {
    current_channel = channel;
    document.querySelector(".channel-title").innerText = current_channel;
    loadMessagesAndMembers();
}

function loadMessagesAndMembers() {
    let xhr = new XMLHttpRequest();
    //initializes new request of type POST and sends it to channel python method on server side
    xhr.open("POST", "/channel"); // Send POST request to server-side Python script
    //Indicates that the request body will contain JSON data
    xhr.setRequestHeader("Content-Type", "application/json");
    //function that's called when the request completes successfully
    xhr.onload = function () {
        //status === 200 means that it worked
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText);
            let messages = response['messages'];
            let messageContainer = document.querySelector('.message-container');
            messageContainer.innerHTML = ''; // Clear previous messages

            messages.forEach(function (message) {
                let messageDiv = document.createElement('div');
                messageDiv.classList.add('message');
                messageDiv.textContent = message.sender + " || " + message.content;
                messageContainer.appendChild(messageDiv);
                //This is code to reverse the scroll direction of the message board
                const messageContainer1 = document.querySelector('.message-container');
                messageContainer1.scrollTop = messageContainer1.scrollHeight;
            });

            let userContainer = document.querySelector('.member-container');
            userContainer.innerHTML = ''; //Clear previous members
            users = response['users'];

            users.forEach(function (user) {
                displayInUserOrAdmin(user, userContainer);
            });

            let adminContainer = document.querySelector('.admin-container');
            adminContainer.innerHTML = '';
            admins = response['admins'];

            admins.forEach(function (admin) {
                displayInUserOrAdmin(admin, adminContainer);
            });
        } else {
            // Error handling
            console.error("Failed");
        }
    };
    xhr.send(JSON.stringify({loadMessage: "true", current_channel: current_channel}));
}
function promote(){
    if(current_channel === ""){
        alert("Please select a channel first.");
    }else if(!admins.includes(username)){
        alert("You are not an admin, you do cannot promote a user.");
    }else{
        let userToPromote = window.prompt("Please enter the username for the user that you want to promote.");

        if (userToPromote) {
            fetch('/channel', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    promote: true,
                    newAdmin: userToPromote,
                    channelName: current_channel  // assuming current_channel is available
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data); // Log the response from the server
                // Handle the response as needed
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle errors
            });
        } else {
            // If the user canceled the prompt or entered an empty string, handle it here.
            console.log("No username entered or prompt canceled.");
        }
    }
}
function displayInUserOrAdmin(username, container) {
    let button = document.createElement('button');
    button.classList.add('member');

    let profileContainer = document.createElement("span");
    profileContainer.className = "profile-container";

    // Create image element for profile picture
    let profilePicture = document.createElement("img");
    profilePicture.src = "../static/images/GuildTalkLogoNoTextClear.png";
    profilePicture.alt = "Profile Picture";

    // Create span element for username
    let usernameSpan = document.createElement("span");
    usernameSpan.className = "username";
    usernameSpan.textContent = username;
    // Append image and username spans to profile container
    profileContainer.appendChild(profilePicture);
    profileContainer.appendChild(usernameSpan);
    button.appendChild(profileContainer);
    container.appendChild(button);
}

//function to give pop up to user for create channel button
function createChannel() {
    let channelName = prompt("Enter a channel name (1-20 Characters)");
    if (channelName !== null && channelName !== "") {
        if (channelName.length < 20) {
            // Allows us to make http requests from client-side js
            let xhr = new XMLHttpRequest();
            //initializes new request of type POST and sends it to channel python method on server side
            xhr.open("POST", "/channel"); // Send POST request to server-side Python script
            //Indicates that the request body will contain JSON data
            xhr.setRequestHeader("Content-Type", "application/json");
            //function that's called when the request completes successfully
            xhr.onload = function () {
                //status === 200 means that it worked
                if (xhr.status === 200) {
                    //parses JSON response from server into js object(newChannel)
                    let newChannel = JSON.parse(xhr.responseText);
                    // Here we update the html to include the new channel
                    let channelContainer = document.querySelector('.select-channel-container');
                    let newElement = document.createElement("button");
                    newElement.classList.add('channel-button');
                    newElement.textContent = channelName;
                    newElement.onclick = function () {
                        setChannel(channelName);
                    };
                    channelContainer.appendChild(newElement);
                } else {
                    // Error handling
                    console.error("Failed to create channel.");
                }
            };
            xhr.send(JSON.stringify({channelName: channelName}));
        } else {
            alert("Channel name too long");
        }
    } else {
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
        xhr.onload = function () {
            //status === 200 means that it worked
            if (xhr.status === 200) {
                //parses JSON response from server into js object(newChannel)
                let newChannel = JSON.parse(xhr.responseText);
                // Here we update the html to include the new channel
                let messageContainer = document.querySelector('.message-container');
                let newElement = document.createElement("div");
                newElement.classList.add('message');
                newElement.textContent = username + " || " + message;
                messageContainer.appendChild(newElement);
            } else {
                // Error handling
                console.error("Failed");
            }
        };
        xhr.send(JSON.stringify({text: message, user_name: user_name, time: time, curr_channel: current_channel}));
        // Clear the textarea after user submission
        document.getElementById("message-input-id").value = "";

    }
}



