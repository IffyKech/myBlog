function changePassword() {  // 
    var currentPasswordInput = document.getElementById("currentPassword").value;
    var newPasswordInput = document.getElementById("newPassword").value;

    if (currentPasswordInput.length < 1 || newPasswordInput.length < 1) {  // Ensure that a password has been inputted in all both fields
        alert("Please enter a value in all fields");  // Alert the reader if there was no input in all password fields
    }

    else {
        xmlhttp = new XMLHttpRequest();  // create the new request to send data to the Flask server

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {  // If there was a successful response from the Flask Server
                alert("Password Changed Successfully");  // Alert the user that the password was changed successfully
            }

            else if (this.readyState === 4 && this.status === 500) {  // If there was an unsuccessfull response from the Flask Server
                alert("Current Password is incorrect. " +
                    "Please Try again");  // Alert the reader that they inputted the password incorrectly
                window.location.href = "http://127.0.0.1:5000/profile";
            }

        }

        xmlhttp.open("POST", "http://127.0.0.1:5000/profile?pwd=" +currentPasswordInput.toString()+ "&new_pwd=" +newPasswordInput.toString(), true);  // Open the request to change the password
        xmlhttp.send();  // send the request to the server at the URL above
    }

}

var changePasswordButton = document.getElementById("changePasswordButton");
changePasswordButton.addEventListener("click", function () {changePassword()});  // set the changePassword function to the 'Submit Changes' button
