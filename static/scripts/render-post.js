var postResults = jsonPostResults;  // get the results of posts from the Flask response
var commentResults = jsonCommentResults;  // get the results of comments from the Flask response
var amountOfComments = commentResults.length;  // get the amount of comments

/* RENDER POST */
/* Set all attributes of post details */
var postID = postResults[0][0];
var tagID = postResults[0][1];
var tagName = postResults[0][2];
var postContent = postResults[0][3];
var postTitle = postResults[0][4];
var postDate = postResults[0][5];
var creatorID = postResults[0][6];
var creatorName = postResults[0][7];

/* Start process of rendering the HTML post */
/* These are the necessary elements that are needed in the HTML to render the post */
var contentDiv = document.getElementById("content");

var postDivEle = document.createElement("div");
postDivEle.className = "post";

var postTitleEle = document.createElement("h2");
postTitleEle.className = "title";
postTitleEle.innerHTML = postTitle;

var postDateEle = document.createElement("p");
postDateEle.className = "meta";
postDateEle.innerHTML = `<span class="date">${postDate}</span><span class="posted">Posted by: ${creatorName}</a>`;

var whitespaceDivEle = document.createElement("div");
whitespaceDivEle.style.clear = "both";

var entryDivEle = document.createElement("div");
entryDivEle.className = "entry";

var postContentEle = document.createElement("p");
postContentEle.style.color = "black";
postContentEle.style.fontSize = "15px";
postContentEle.innerHTML = postContent;

var linksParagraphEle = document.createElement("p");
linksParagraphEle.className = "links";
linksParagraphEle.innerHTML = `Tag: ${tagName}`;

/* Once all the HTML elements are created, they need to be sorted in order of parent/child */

contentDiv.appendChild(postDivEle);  // parent element to all the HTML tags for rendering the post

postDivEle.appendChild(postTitleEle);
postDivEle.appendChild(postDateEle);
postDivEle.appendChild(whitespaceDivEle);
postDivEle.appendChild(entryDivEle);
entryDivEle.appendChild(postContentEle);
entryDivEle.appendChild(linksParagraphEle);


/* RENDER COMMENTS */
if (amountOfComments > 0) { // if there were comments found from the Flask response
    /* Create and render the HTML elements for each comment that was found in the Flask response */
    for (let repeat = 0; repeat < amountOfComments; repeat++) {
        /* Retrieve the details of each comment */
        var commentID = commentResults[repeat][0];
        var commentContent = commentResults[repeat][1];
        var commentDate = commentResults[repeat][2];
        
        /* Begin rendering the comment with the details above */
        var commentPostDivEle = document.createElement("div");
        commentPostDivEle.className = "post";

        var commentDateEle = document.createElement("p");
        commentDateEle.className = "meta";
        commentDateEle.innerHTML = `<span class="date"></span><span class="posted">Comment posted on: ${commentDate}</span>`

        var commentEntryDiv = document.createElement("div");
        commentEntryDiv.className = "entry";

        var commentContentEle = document.createElement("p");
        commentContentEle.style.color = "black";
        commentContentEle.style.fontSize = "15px";
        commentContentEle.innerHTML = commentContent;

        contentDiv.appendChild(commentPostDivEle);
        commentPostDivEle.appendChild(commentDateEle);
        commentPostDivEle.appendChild(commentEntryDiv);
        commentEntryDiv.appendChild(commentContentEle);

    }
}

else {  // if there were no comments found from the FLask response
    /* Display a red text message to indicate no comments */
    var errorMessage = document.createElement("h1");
    errorMessage.style.color = "red";
    errorMessage.innerHTML = "No Comments";
    contentDiv.appendChild(errorMessage);
}
