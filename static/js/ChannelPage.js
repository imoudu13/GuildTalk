document.addEventListener('DOMContentLoaded', function() {
    //This is code to reverse the scroll direction of the message board
    const messageContainer = document.querySelector('.message-container');
    messageContainer.scrollTop = messageContainer.scrollHeight;
    //

});

//function to redirect buttons to pages based on url
function redirectToPage(url) {
    window.location.href = url;
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
                newElement.textContent = newChannel.name;
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