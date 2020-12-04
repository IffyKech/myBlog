function createUser(){
    let username = document.getElementById("registerUsername").value;
    let password = document.getElementById("registerPassword").value;
    let repeat_password = document.getElementById("registerRepeat").value;

    const requestURL = 'http://127.0.0.1:5000/login?username=' + username.toString() + '&password=' + password.toString() + '&repeat_password=' + repeat_password.toString()
    const request = new XMLHttpRequest();
    request.open('POST', requestURL, true);
    request.setRequestHeader('Content-Type', 'application/json');
    if (request.readyState === 4 && request.status === 200){
        var json = JSON.parse(request.responseText);
    }
    data = JSON.stringify({"username": username, "password": password});
    request.send();
    return false;
}

let createUserButton = document.getElementById("registerButton");
createUserButton.addEventListener("click", function () {createUser()});
