var postResults = jsonPostResults;
var commentResults = jsonCommentResults;
var amountOfComments = commentResults.length;

var postID = postResults[0][0];
var tagID = postResults[0][1];
var tagName = postResults[0][2];
var postContent = postResults[0][3];
var postTitle = postResults[0][4];
var postDate = postResults[0][5];
var creatorID = postResults[0][6];
var creatorName = postResults[0][7];

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
postContentEle.style.fontSize = "30px";
postContentEle.innerHTML = postContent;

var linksParagraphEle = document.createElement("p");
linksParagraphEle.className = "links";
linksParagraphEle.innerHTML = `Tag: ${tagName}`;

contentDiv.appendChild(postDivEle);

postDivEle.appendChild(postTitleEle);
postDivEle.appendChild(postDateEle);
postDivEle.appendChild(whitespaceDivEle);
postDivEle.appendChild(entryDivEle);
entryDivEle.appendChild(postContentEle);
entryDivEle.appendChild(linksParagraphEle);

if (amountOfComments > 0) { // if there were comments found
    for (let repeat = 0; repeat < amountOfComments; repeat++) {

        var commentID = commentResults[repeat][0];
        var commentContent = commentResults[repeat][1];
        var commentDate = commentResults[repeat][2];
        var commentCreatorID = commentResults[repeat][3];
        var commentCreatorName = commentResults[repeat][4];

        var commentPostDivEle = document.createElement("div");
        commentPostDivEle.className = "post";

        var commentDateEle = document.createElement("p");
        commentDateEle.className = "meta";
        commentDateEle.innerHTML = `<span class="date">${commentDate}</span><span class="posted">Comment posted by: ${commentCreatorName}</span>`

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

else {
    var errorMessage = document.createElement("h1");
    errorMessage.style.color = "red";
    errorMessage.innerHTML = "No Comments";
    contentDiv.appendChild(errorMessage);
}