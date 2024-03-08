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

        }
        else{
            alert("Channel name too long");
        }
    }
    else{
        alert("Please insert a channel name");
    }
}