document.addEventListener("DOMContentLoaded", function () {
  document.addEventListener("keydown", function (event) {
    // Check if the pressed key is the Escape key (code 27)
    if (event.key === "Escape" || event.keyCode === 27) {
      // Navigate back to the previous page
      window.history.back();
    }
  });
  //get the edit profile button
  let openButton = document.getElementById("edit_profile");

  openButton.addEventListener("click", function () {
    document.getElementById("myModal").style.display = "block";
    document.querySelector(".overlay").style.display = "block";
  });

  // Get the logout button
  let logoutButton = document.getElementById("log_out");

  // Add event listener to logout button
  logoutButton.addEventListener("click", function () {
    // Display confirmation dialog
    let confirmLogout = confirm("Are you sure you want to logout?");

    // If user confirms logout, redirect to login page
    if (confirmLogout) {
      window.location.href = "/"; // Change "/login" to the actual URL of your login page
    }
  });

  //These buttons are for the close and submit buttons.
  //These remove the modal from the display.
  let close = document.getElementById("close");

  close.addEventListener("click", function () {
    document.getElementById("myModal").style.display = "none";
    document.querySelector(".overlay").style.display = "none";
  });

  let submit = document.getElementById("submit");

  submit.addEventListener("click", function () {
    document.getElementById("myModal").style.display = "none";
    document.querySelector(".overlay").style.display = "none";
  });
});
