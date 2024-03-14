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

    //These buttons are for the close and submit buttons.
    //These remove the modal from the display.
    let close = document.getElementById("close");

    close.addEventListener('click', function (){
            document.getElementById('myModal').style.display = 'none';
            document.querySelector('.overlay').style.display = 'none';
    });

    let submit = document.getElementById("submit");

    submit.addEventListener('click', function (){
            document.getElementById('myModal').style.display = 'none';
            document.querySelector('.overlay').style.display = 'none';
    });
});
