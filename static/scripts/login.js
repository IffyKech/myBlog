function createUser() {
    let username = document.getElementById("registerUsername").value;
    let password = document.getElementById("registerPassword").value;
    let repeat_password = document.getElementById("registerRepeat").value;

    if (username.length < 1 || password.length < 1 || repeat_password.length < 1) { // if a value has not been entered in every field
        alert("Please Enter a value in all fields"); // inform the user
    }

    else { // if a value has been entered in every field
        if (repeat_password !== password) { // if the user did not re-enter the correct password
            alert("Both Passwords did not match. Please Try again.");
        }

        else { // if the user re-entered the correct password
            let xmlhttp = new XMLHttpRequest();

            xmlhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) {
                    window.location.href = "http://127.0.0.1:5000/home";
                }

                else if (this.readyState === 4 && this.status === 500) {
                    alert("Username already exists." +
                        "Please Try another username");
                }
            }


            xmlhttp.open("POST", "http://127.0.0.1:5000/login?username=" +username.toString()+ "&password=" +password.toString());
            xmlhttp.send();
        }
    }

}

function loginUser() {
    let username = document.getElementById("loginUsername").value;
    let password = document.getElementById("loginPassword").value;

    if ( username.length < 1 || password.length < 1) {
        alert("Please enter a value in all fields");
    }

    else {
        let xmlhttp = new XMLHttpRequest();

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                window.location.href = "http://127.0.0.1:5000/home";
            }

            else if (this.readyState === 4 && this.status === 500) {
                alert("User Credentials Not Found");
            }

        }

        xmlhttp.open("POST", "http://127.0.0.1:5000/login/user?username=" +username.toString()+ "&password=" +password.toString());
        xmlhttp.send();
    }
}

let createUserButton = document.getElementById("registerButton");
createUserButton.addEventListener("click", function () {createUser()});

let loginUserButton = document.getElementById("loginButton");
loginUserButton.addEventListener("click", function () {loginUser()});
