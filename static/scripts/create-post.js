function createPost() {
    let title = document.getElementById("create-title").value;
    let content = document.getElementById("create-content").value;
    let tag = document.getElementById("tag").value;

    if (title.length < 1 || content.length < 1 ) { // if a value has not been entered in every field
        alert("Please Enter a value in all fields"); // inform the user
    }



    else { // if the user re-entered the correct password
        let xmlhttp = new XMLHttpRequest();

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                alert("Post Created!\nPlease refresh the page to view the post.");
            }
        }
        xmlhttp.open("POST", "http://127.0.0.1:5000/create/post?title=" +title.toString()+ "&content=" +content.toString()+ "&tag="+tag.toString(), true);
        xmlhttp.send();
    }
}

let createPostButton = document.getElementById("create-post-button");
createPostButton.addEventListener("click", function () {createPost()});


