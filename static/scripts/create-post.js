function createPost() {
    let title = document.getElementById("create-title").value; // gets the value of what the user types into element with ID "create-title"
    let content = document.getElementById("create-content").value;  // gets the value of what the user types into element with ID "create-content"
    let tag = document.getElementById("tag").value; // gets the value of the tag selected by the user

    if (title.length < 1 || content.length < 1 ) { // if a value has not been entered in every field
        alert("Please Enter a value in all fields"); // inform the user
    }



    else { // if the user re-entered the correct password
        let xmlhttp = new XMLHttpRequest();

        xmlhttp.onreadystatechange = function () {   // checks if the request is ready to be sent
            if (this.readyState === 4 && this.status === 200) {
                alert("Post Created!\nPlease refresh the page to view the post.");   // lets the user know that their post was made.
            }
        }
        xmlhttp.open("POST", "http://127.0.0.1:5000/create/post?title=" +title.toString()+ "&content=" +content.toString()+ "&tag="+tag.toString(), true);
        xmlhttp.send();   // sends the XML request with the method POST and a url to get the values above
    }
}

let createPostButton = document.getElementById("create-post-button");   // identifies the "Create Post!" button 
createPostButton.addEventListener("click", function () {createPost()});   /*  assign an event listener which checks if the button has been pressed 
                                                                            and a function to execute on press. */


