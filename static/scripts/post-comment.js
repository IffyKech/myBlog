function postComment() {
    var comment = document.getElementById("comment-content").value;
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            alert("Comment Created!\nPlease refresh the page to view this comment");
        }
    }

    xmlhttp.open("POST", "http://127.0.0.1:5000/create/comment", true);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.send(JSON.stringify({"comment": comment, "postid": postID}));

}

var submitCommentButton = document.getElementById("comment-submit");
submitCommentButton.addEventListener("click", function () {postComment()});