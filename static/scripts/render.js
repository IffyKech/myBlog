function createUser() {
    let username = document.getElementById("registerUsername").value;
    let password = document.getElementById("registerPassword").value;
    let repeat_password = document.getElementById("registerRepeat").value;

    if (username.length < 1 || password.length < 1 || repeat_password.length < 1) { // if a value has not been entered in every field
        alert("Please Enter a value in all fields"); // inform the user
    }

    else { // if a value has been entered in every field
        if (repeat_password !== password) { // if the user did not re-enter the correct password
            alert("Both Passwords did not match.<br>Please Try again.");
        }

        else { // if the user re-entered the correct password
            let xmlhttp = new XMLHttpRequest();

            xmlhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) {
                    alert("Account Created");
                }
            }

            xmlhttp.open("POST", "http://127.0.0.1:5000/login?username=" +username.toString()+ "&password=" +password.toString());
            xmlhttp.send();
        }
    }

}

let createUserButton = document.getElementById("registerButton");
createUserButton.addEventListener("click", function () {createUser()});
