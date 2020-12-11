function postComment() {
    var comment = document.getElementById("comment-content").value;
    var xmlhttp = new XMLHttpRequest();
    
    if (comment.length < 1){ // if a value has not been entered in the comment field
        alert("Please enter a value in the comment field.");  // inform the user
    }

    xmlhttp.onreadystatechange = function () {    // checks if the request is ready to send 
        if (this.readyState === 4 && this.status === 200) {
            alert("Comment Created!\nPlease refresh the page to view this comment");    // alerts the user their comment has been made
        }
    }

    xmlhttp.open("POST", "http://127.0.0.1:5000/create/comment", true);      // makes the request an asynchronous POST request and gives it a URL to go to
    xmlhttp.setRequestHeader("Content-Type", "application/json");           // tells the browser what type of data is being sent, which is JSON
    xmlhttp.send(JSON.stringify({"comment": comment, "postid": postID}));   // packs the data that needs to be sent into the request

}

var submitCommentButton = document.getElementById("comment-submit");    // identifies the button with ID "comment-submit"
submitCommentButton.addEventListener("click", function () {postComment()});   /* gives the button an event listener which checks if 
                                                                                    it's been pressed and assigns a function to execute on press */
