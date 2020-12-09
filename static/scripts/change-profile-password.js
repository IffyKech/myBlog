function changePassword() {
    var currentPasswordInput = document.getElementById("currentPassword").value;
    var newPasswordInput = document.getElementById("newPassword").value;

    if (currentPasswordInput.length < 1 || newPasswordInput.length < 1) {
        alert("Please enter a value in all fields");
    }

    else {
        xmlhttp = new XMLHttpRequest();

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                alert("Password Changed Successfully");
            }

            else if (this.readyState === 4 && this.status === 500) {
                alert("Current Password is incorrect. " +
                    "Please Try again");
                window.location.href = "http://127.0.0.1:5000/profile";
            }

        }

        xmlhttp.open("POST", "http://127.0.0.1:5000/profile?pwd=" +currentPasswordInput.toString()+ "&new_pwd=" +newPasswordInput.toString(), true);
        xmlhttp.send();
    }

}

var changePasswordButton = document.getElementById("changePasswordButton");
changePasswordButton.addEventListener("click", function () {changePassword()});