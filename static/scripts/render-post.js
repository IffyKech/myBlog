var postResults = jsonPostResults;
var commentResults = jsonCommentResults;
console.log(postResults);
console.log(commentResults);

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