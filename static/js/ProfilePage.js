document.addEventListener('DOMContentLoaded', function(){

    document.addEventListener('keydown', function(event) {
            // Check if the pressed key is the Escape key (code 27)
            if (event.key === 'Escape' || event.keyCode === 27) {
                // Navigate back to the previous page
                window.history.back();
            }
    });
    //get the button
    let openButton = document.getElementById("edit_profile");

    openButton.addEventListener('click', function (){
        document.getElementById('myModal').style.display = 'block';
        document.querySelector('.overlay').style.display = 'block';
    });

    let closeButton = document.getElementById("close_button");

    closeButton.addEventListener('click', function (){
        document.getElementById('myModal').style.display = 'none';
        document.querySelector('.overlay').style.display = 'none';
    });
});
