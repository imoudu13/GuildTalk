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