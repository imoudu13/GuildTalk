document.addEventListener('DOMContentLoaded', function() {
    //This is code to reverse the scroll direction of the message board
    const messageContainer = document.querySelector('.message-container');
    messageContainer.scrollTop = messageContainer.scrollHeight;
    //

});

//function to redirect help button to help page. Right now its just google
function redirectToPage() {
    window.location.href = 'https://www.google.com/search?q=google&oq=google+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQIxgnGIAEGIoFMgYIAhBFGDwyBggDEEUYPDIGCAQQRRg8MgYIBRBFGDwyBggGEEUYQTIGCAcQRRhB0gEINjgxOGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8';
}