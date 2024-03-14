
let current_channel = ""
document.addEventListener('DOMContentLoaded', function() {
    //This is code to reverse the scroll direction of the message board
    const messageContainer = document.querySelector('.message-container');
    messageContainer.scrollTop = messageContainer.scrollHeight;
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

}
//function to give pop up to user for create channel button
function createChannel(){
    let channelName = prompt("Enter a channel name (1-20 Characters)");
    if(channelName !== null && channelName !== ""){
        if(channelName.length < 20){
        // Allows us to make http requests from client-side js
        var xhr = new XMLHttpRequest();
        //initalizes new request of type POST and sends it to channel python method on server side
        xhr.open("POST", "/channel"); // Send POST request to server-side Python script
        //Indicates that the request body will contain JSON data
        xhr.setRequestHeader("Content-Type", "application/json");
        //function that's called when the request completes successfully
        xhr.onload = function() {
            //status === 200 means that it worked
            if (xhr.status === 200) {
                //parses JSON response from server into js object(newChannel)
                var newChannel = JSON.parse(xhr.responseText);
                // Here we update the html to include the new channel
                var channelContainer = document.querySelector('.select-channel-container');
                var newElement = document.createElement("button");
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
        curr_channel = "test_channel"
        // Do something with the submitted message, for example, log it

        var xhr = new XMLHttpRequest();
        //initalizes new request of type POST and sends it to channel python method on server side
        xhr.open("POST", "/channel"); // Send POST request to server-side Python script
        //Indicates that the request body will contain JSON data
        xhr.setRequestHeader("Content-Type", "application/json");
        //function that's called when the request completes successfully
        xhr.onload = function() {
            //status === 200 means that it worked
            if (xhr.status === 200) {
                //parses JSON response from server into js object(newChannel)
                var newChannel = JSON.parse(xhr.responseText);
                // Here we update the html to include the new channel
                var messageContainer = document.querySelector('.message-container');
                var newElement = document.createElement("div");
                newElement.classList.add('message');
                newElement.textContent = message;
                messageContainer.appendChild(newElement);
            } else {
                // Error handling
                console.error("Failed to create channel.");
            }
        };
        xhr.send(JSON.stringify({text: message, user_name: user_name, time: time, curr_channel:curr_channel }));
        // Clear the textarea after user submission
        document.getElementById("message-input-id").value = "";

    }
}



