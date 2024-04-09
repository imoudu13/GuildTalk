let username = document.currentScript.getAttribute("data-username");
let current_channel = "";
let users = null;
let admins = null;
let selectedUser = null;

document.addEventListener("DOMContentLoaded", function () {
    // these event listener are to hide the userModal
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            hideModal();
        }
    });
    // event listeners for remove/promote user
    document.getElementById('removeUser').addEventListener('click', function () {
        remove();
        hideModal();
    });
    document.getElementById('promoteUser').addEventListener('click', function () {
        promote();
        hideModal();
    });

    // Add an event listener to the textarea for the keypress event
    document
        .getElementById("message-input-id")
        .addEventListener("keypress", handleKeyPress);
    // document.querySelector(".promote-button").addEventListener("click", promote);
    // document.querySelector(".remove-button").addEventListener("click", remove);

    // Add an event listener to the search bar
    document
        .getElementById("message-search-bar")
        .addEventListener("input", searchMessages);
    //hide invite button when not in channel
    document.querySelector('.invite-button').classList.add('hide');

    //event listener for joke button
    const fetchJokeBtn = document.getElementById('joke-button-id');
    const messageInput = document.getElementById('message-input-id');

    fetchJokeBtn.addEventListener('click', async () => {
        try {
            const response = await fetch('https://icanhazdadjoke.com/', {
                headers: {
                    'Accept': 'application/json'
                }
            });

            const data = await response.json();

            // Populate the input with the joke
            messageInput.value = data.joke;

        } catch (error) {
            console.error('Error fetching joke:', error);
            alert('Failed to fetch joke. Please try again.');
        }
    });

    //set username
    document.querySelector('.username').innerHTML= username;
});

function searchMessages() {
    // Get the search query from the search bar
    const searchQuery = document
        .getElementById("message-search-bar")
        .value.toLowerCase();

    // Get all message elements
    const messageElements = document.querySelectorAll(".message");

    // Iterate over each message element
    messageElements.forEach(function (messageElement) {
        // Get the text content of the message
        const messageText = messageElement.textContent.toLowerCase();

        // Check if the search query is found in the message text
        if (messageText.includes(searchQuery)) {
            // If the search query is found, display the message
            messageElement.style.display = "block";
        } else {
            // If the search query is not found, hide the message
            messageElement.style.display = "none";
        }
    });
}

//function to redirect buttons to pages based on url
function redirectToPage(url) {
    window.location.href = url;
}

//Function to set current channel and load messages
function setChannel(channel, isDirectMessage) {
    let isHidden = document.querySelector('.invite-button').classList.contains('hide');
    if (isDirectMessage === 1 && !isHidden){
        document.querySelector('.invite-button').classList.add('hide');
    }
    else if (isDirectMessage !== 1 && isHidden){
        document.querySelector('.invite-button').classList.remove('hide');
    }
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
            let messages = response["messages"];
            let messageContainer = document.querySelector(".message-container");
            messageContainer.innerHTML = ""; // Clear previous messages

            messages.forEach(function (message) {
                makeMessage(message, messageContainer, 0);
            });

            let userContainer = document.querySelector(".member-container");
            userContainer.innerHTML = ""; //Clear previous members
            users = response["users"];

            users.forEach(function (user) {
                displayInUserOrAdmin(user, userContainer);
            });

            let adminContainer = document.querySelector(".admin-container");
            adminContainer.innerHTML = "";
            admins = response["admins"];

            admins.forEach(function (admin) {
                displayInUserOrAdmin(admin, adminContainer);
            });
        } else {
            // Error handling
            console.error("Failed");
        }
    };
    xhr.send(
        JSON.stringify({loadMessage: "true", current_channel: current_channel})
    );
}

function promote() {
    if (selectedUser) {
        fetch("/channel", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                promote: true,
                newAdmin: selectedUser,
                channelName: current_channel, // assuming current_channel is available
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data); // Log the response from the server
                // Handle the response as needed
            })
            .catch((error) => {
                console.error("Error:", error);
                // Handle errors
            });
    } else {
        // If the user canceled the prompt or entered an empty string, handle it here.
        console.log("No username entered or prompt canceled.");
    }
}

function remove() {
    if (selectedUser) {
        fetch("/channel", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                remove: true,
                removedUser: selectedUser,
                channelName: current_channel, // assuming current_channel is available
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data); // Log the response from the server
                // Handle the response as needed
            })
            .catch((error) => {
                console.error("Error:", error);
                // Handle errors
            });
    } else {
        // If the user canceled the prompt or entered an empty string, handle it here.
        console.log("No username entered or prompt canceled.");
    }
}

function displayInUserOrAdmin(username, container) {
    let button = document.createElement("button");
    button.classList.add("member");

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

    // This listener it displays the remove/promote modal on a click
    button.addEventListener('click', function () {
        selectedUser = username;
        console.log(selectedUser);
        displayModal();
    });

    // add event listener for regular member
    container.appendChild(button);
}

function displayModal() {
    // this function displays the modal that allows the admin to remove/promote a user
    // the modal only displays id the user is an admin
    if (!admins.includes(username)) return;

    document.getElementById('user-modal-question').innerText = `What would you like to do with ${selectedUser}?`;
    document.getElementById('user-modal-question').style.color = 'black';
    document.getElementById("userModal").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

function hideModal() {
    // this function hides a modal
    document.getElementById("userModal").style.display = "none";
    document.getElementById("overlay").style.display = "none";
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
                    let channelContainer = document.querySelector(
                        ".select-channel-container"
                    );
                    let newElement = document.createElement("button");
                    newElement.classList.add("channel-button");
                    newElement.textContent = channelName;
                    newElement.onclick = function () {
                        setChannel(channelName,0);
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
function directMessage() {
    let userToMessage = prompt("Enter the username of who you want to create a chat with");
    if (userToMessage === username){
        alert("You cannot create a direct message chat with yourself :( Please find a friend");
        return;
    }
    if (userToMessage !== null && userToMessage !== "") {
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
                    let response = JSON.parse(xhr.responseText);
                    // Check the success field
                    if (response.success) {
                        // Here we update the html to include the user
                       let channelContainer = document.querySelector(
                        ".select-channel-container"
                    );
                    let newElement = document.createElement("button");
                    newElement.classList.add("channel-button");
                    newElement.textContent = userToMessage + " + " + username;
                    newElement.onclick = function () {
                        setChannel(userToMessage + " + " + username, 1);
                    };
                    channelContainer.appendChild(newElement);
                    } else {
                        // Display error message
                        console.error("User does not exist", response.error);
                        alert(response.error);
                    }
                    // Here we update the html to include the new channel
                } else {
                    // Error handling
                    console.error("Failed to make direct message chat.");
                }
            };
            xhr.send(JSON.stringify({directMessage: userToMessage}));
    } else {
        alert("Please insert a username to message");
    }
}

// Function to put a message into html and send it to the controller
function handleKeyPress(event) {
    // Check if Enter key was pressed (keyCode 13)
    let user_name;
    if (event.keyCode === 13) {
        event.preventDefault(); // Prevent the default behavior of the Enter key
        //if not in a channel alert user
        if (current_channel === '') {
            alert("Please select a channel to send a message");
        }
        // Access the value of the textarea
        const message = document.getElementById("message-input-id").value;
        //Here we will set other values such as username, channel, and time. For now it is dummy data while functionality is being worked on
        //if message is empty dont send it
        if (message === '') {
            return
        }
        user_name = username;
        time = "8:56pm";

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
                let messageContainer = document.querySelector(".message-container");
                makeMessage(message, messageContainer, 1);
            } else {
                // Error handling
                console.error("Failed");
            }
        };
        xhr.send(
            JSON.stringify({
                text: message,
                user_name: user_name,
                time: time,
                curr_channel: current_channel,
            })
        );
        // Clear the textarea after user submission
        document.getElementById("message-input-id").value = "";
    }
}

//Function to invite other users to channel
function inviteToChannel() {
    let inviteUser = prompt("Enter a username");
    if (inviteUser !== null && inviteUser !== "") {
        if (inviteUser.length < 20) {
            // Allows us to make http requests from client-side js
            var xhr = new XMLHttpRequest();
            //initalizes new request of type POST and sends it to channel python method on server side
            xhr.open("POST", "/channel"); // Send POST request to server-side Python script
            //Indicates that the request body will contain JSON data
            xhr.setRequestHeader("Content-Type", "application/json");
            //function that's called when the request completes successfully
            xhr.onload = function () {
                //status === 200 means that it worked
                if (xhr.status === 200) {
                    //parse the json response and act accordingly
                    let response = JSON.parse(xhr.responseText);
                    // Check the success field
                    if (response.success) {
                        // Here we update the html to include the user
                        let userContainer = document.querySelector(".member-container");
                        displayInUserOrAdmin(inviteUser, userContainer);
                    } else {
                        // Display error message
                        console.error("Failed to add user:", response.error);
                        alert(response.error);
                    }
                } else {
                    // Error handling
                    console.error("Failed to add user");
                }
            };
            xhr.send(JSON.stringify({invite: inviteUser, current_channel: current_channel}));
        } else {
            alert("username too long");
        }
    } else {
        alert("Please insert a username");
    }
}

// Function to put a message into html and send it to the controller
function makeMessage(message, messageContainer, a) {
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    let messageSender;
    let textContent;
    if (a === 0) {
        messageSender = message.sender;
        textContent = message.content;
    } else if (a === 1) {
        messageSender = username;
        textContent = message;
    }
    //text content
    messageDiv.textContent = messageSender + " || " + textContent;
    //delete button
    let deleteButton = document.createElement("button");
    deleteButton.classList.add("deleteButton");
    deleteButton.classList.add("button");
    deleteButton.textContent = "X";
    //add delete button to message div
    messageDiv.appendChild(deleteButton);
    //On delete button click call deleteMessage()
    deleteButton.onclick = function () {
        deleteMessage(this.parentNode);
    };

    messageContainer.appendChild(messageDiv);
    //This is code to reverse the scroll direction of the message board
    const messageContainer1 = document.querySelector(".message-container");
    messageContainer1.scrollTop = messageContainer1.scrollHeight;
}

function deleteMessage(message) {
    if (isAdmin()) {
        if (confirm("Do you want to delete this message?")) {
            let parentContainer = message.parentNode;
            // Convert the collection of child elements to an array
            let childrenArray = Array.from(parentContainer.children);
            // Find the index of the message within its parent container
            let index = childrenArray.indexOf(message);
            // Delete the message
            message.remove();
            //remove message from database
            let xhr = new XMLHttpRequest();
            //initializes new request of type POST and sends it to channel python method on server side
            xhr.open("POST", "/channel"); // Send POST request to server-side Python script
            //Indicates that the request body will contain JSON data
            xhr.setRequestHeader("Content-Type", "application/json");
            //function that's called when the request completes successfully
            xhr.onload = function () {
                //status === 200 means that it worked
                if (xhr.status === 200) {
                    console.log("Success");
                } else {
                    // Error handling
                    console.error("Failed");
                }
            };
            xhr.send(
                JSON.stringify({
                    deleteMessage: true,
                    messageIndex: index,
                    current_channel: current_channel,
                })
            );
        }
    } else {
        alert("You must be an admin to delete a message");
    }
}

function isAdmin() {
    let admin = false;
    // get admin container
    let adminContainer = document.querySelector(".admin-container");

    // Get all admins
    let memberButtons = adminContainer.querySelectorAll(".member");

    // Iterate over each admin
    memberButtons.forEach(function (memberButton) {
        // Get the username span element within the member button
        let usernameElement = memberButton.querySelector(".username");
        // Get the username text from the username span element
        let usernameAdmin = usernameElement.textContent;
        // Compare the username with logged-in user. If they are an admin they can delete messages now
        if (usernameAdmin === username) {
            admin = true;
        }
    });
    return admin;
}

function testSearchFunctionality() {
    // Simulate user input in the search bar
    const searchInput = "Lorem";

    // Set the value of the search bar to the simulated input
    document.getElementById("message-search-bar").value = searchInput;

    // Trigger the input event on the search bar to simulate user typing
    const event = new Event("input");
    document.getElementById("message-search-bar").dispatchEvent(event);

    // Get all message elements after the search operation
    const messageElements = document.querySelectorAll(".message");

    // Check each message element to ensure correct filtering
    messageElements.forEach(function (messageElement) {
        // Get the text content of the message
        const messageText = messageElement.textContent.toLowerCase();

        // Check if the search query is found in the message text
        const searchResult = messageText.includes(searchInput.toLowerCase());

        // Log test results
        if (searchResult && messageElement.style.display !== "none") {
            console.log("Test passed: Message displayed correctly.");
        } else if (!searchResult && messageElement.style.display === "none") {
            console.log("Test passed: Message hidden correctly.");
        } else {
            console.error("Test failed: Incorrect message display status.");
        }
    });
}

// Call the test function to execute the test
testSearchFunctionality();

