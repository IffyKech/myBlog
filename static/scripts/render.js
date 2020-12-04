function createUser() {
    let username = document.getElementById("registerUsername").value;
    let password = document.getElementById("registerPassword").value;
    let repeat_password = document.getElementById("registerRepeat").value;

    let xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            alert("Account Created");
        }
    }

    xmlhttp.open("POST", "http://127.0.0.1:5000/login?username=" +username.toString()+ "&password=" +password.toString()+
    "&repeat_password=" +repeat_password.toString());
    xmlhttp.send();

}

let createUserButton = document.getElementById("registerButton");
createUserButton.addEventListener("click", function () {createUser()});
