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
            let xmlhttp = new XMLHttpRequest();  // create the new xml request

            xmlhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) {  // If there was a successful response from the server
                    window.location.href = "http://127.0.0.1:5000/home";  // redirect the user to the homepage
                }

                else if (this.readyState === 4 && this.status === 500) {  // if there was a fail response from the server
                    alert("Username already exists." +
                        "Please Try another username");  // alert the user that the username they inputted already existed
                }
            }


            xmlhttp.open("POST", "http://127.0.0.1:5000/login?username=" +username.toString()+ "&password=" +password.toString());  // create the request with the details
            xmlhttp.send();  // send the request to the server
        }
    }

}

function loginUser() {
    let username = document.getElementById("loginUsername").value;
    let password = document.getElementById("loginPassword").value;

    if ( username.length < 1 || password.length < 1) {  // ensure there is a username and password inputted
        alert("Please enter a value in all fields");
    }

    else {
        let xmlhttp = new XMLHttpRequest();

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) { // if the server returned a successful login code
                window.location.href = "http://127.0.0.1:5000/home";  // redirect the user to the homepage
            }

            else if (this.readyState === 4 && this.status === 500) {  // if the server returned an unsucessful login code
                alert("User Credentials Not Found");  // alert the user of incorrect credentials
            }

        }

        xmlhttp.open("POST", "http://127.0.0.1:5000/login/user?username=" +username.toString()+ "&password=" +password.toString());  // create the request
        xmlhttp.send(); // send the request to the server
    }
}

let createUserButton = document.getElementById("registerButton");
createUserButton.addEventListener("click", function () {createUser()});  // add the create user function to the create user button

let loginUserButton = document.getElementById("loginButton");
loginUserButton.addEventListener("click", function () {loginUser()});  // add the login user function to the login user button
