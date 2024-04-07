// Mocking the DOM elements
document.body.innerHTML = `
  <button id="edit_profile"></button>
  <div id="myModal"></div>
  <div class="overlay"></div>
  <button id="log_out"></button>
`;

function addEventListenerToEditProfileButton() {
  let openButton = document.getElementById("edit_profile");

  openButton.addEventListener("click", function () {
    document.getElementById("myModal").style.display = "block";
    document.querySelector(".overlay").style.display = "block";
  });
}

function addEventListenerToLogoutButton() {
  let logoutButton = document.getElementById("log_out");

  logoutButton.addEventListener("click", function () {
    let confirmLogout = confirm("Are you sure you want to logout?");
    if (confirmLogout) {
      window.location.href = "/"; // Change "/login" to the actual URL of your login page
    }
  });
}

describe("addEventListenerToEditProfileButton", () => {
  test("it should show modal and overlay on click", () => {
    addEventListenerToEditProfileButton();

    const editProfileButton = document.getElementById("edit_profile");
    const modal = document.getElementById("myModal");
    const overlay = document.querySelector(".overlay");

    editProfileButton.click();

    expect(modal.style.display).toBe("block");
    expect(overlay.style.display).toBe("block");
  });
});

describe("addEventListenerToLogoutButton", () => {
  test("it should show confirmation dialog and redirect on logout", () => {
    // Mocking the confirm method
    const mockConfirm = jest.fn(() => true);
    window.confirm = mockConfirm;

    addEventListenerToLogoutButton();

    const logoutButton = document.getElementById("log_out");

    logoutButton.click();

    expect(mockConfirm).toHaveBeenCalledWith(
      "Are you sure you want to logout?"
    );
    expect(window.location.href.endsWith("/")).toBe(true);
  });

  test("it should not redirect on cancel", () => {
    // Mocking the confirm method
    const mockConfirm = jest.fn(() => false);
    window.confirm = mockConfirm;

    addEventListenerToLogoutButton();

    const logoutButton = document.getElementById("log_out");

    logoutButton.click();

    expect(mockConfirm).toHaveBeenCalledWith(
      "Are you sure you want to logout?"
    );
    expect(window.location.href).not.toBe("/");
  });
});

describe("addEventListenerToLogoutButton", () => {
  test("it should show confirmation dialog and redirect on logout", () => {
    // Mocking the confirm method
    const mockConfirm = jest.fn(() => true);
    window.confirm = mockConfirm;

    addEventListenerToLogoutButton();

    const logoutButton = document.getElementById("log_out");

    logoutButton.click();

    expect(mockConfirm).toHaveBeenCalledWith(
      "Are you sure you want to logout?"
    );
    expect(window.location.href.endsWith("/")).toBe(true);
  });

  test("it should not redirect on cancel", () => {
    // Mocking the confirm method
    const mockConfirm = jest.fn(() => false);
    window.confirm = mockConfirm;

    addEventListenerToLogoutButton();

    const logoutButton = document.getElementById("log_out");

    logoutButton.click();

    expect(mockConfirm).toHaveBeenCalledWith(
      "Are you sure you want to logout?"
    );
    expect(window.location.href).not.toBe("/");
  });
});
