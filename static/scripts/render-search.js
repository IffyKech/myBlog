var results = json_results;
var amountOfResults = results.length;
var contentDiv = document.getElementById("content");
if (amountOfResults > 1) {  // if the query returned results
    /*
Repeat the process of creating html for the posts, for as many posts as there are
 */
    for (let repeat = 0; repeat < amountOfResults; repeat++) {
        /* Get the Post details iteratively for each post */
        let resultPostID = results[repeat][0];
        let resultPostTitle = results[repeat][1];
        let resultPostDate = results[repeat][2];
        let resultUserID = results[repeat][3];
        let resultUsername = results[repeat][4];

        /* Create the new HTML elements for the posts */
        /* POST TITLE */
        var postDiv = document.createElement("div");
        postDiv.className = "post";

        var postTitle = document.createElement("h2");
        postTitle.className = "title";
        postTitle.innerHTML = `<a href="http://127.0.0.1:5000/comments?id=${resultPostID}">${resultPostTitle}</a>`;

        /* POST DATE */
        var postDate = document.createElement("p");
        postDate.className = "meta";
        postDate.innerHTML = `<span class="date">${resultPostDate}</span><span class="posted">Posted by: ${resultUsername}</a>`;

        /* WHITESPACE DIV */
        var whitespaceDiv = document.createElement("div");
        whitespaceDiv.style.clear = "both";

        /* READ MORE ENTRY */
        var entryDiv = document.createElement("div");
        entryDiv.className = "entry";

        var linksParagraph = document.createElement("p");
        linksParagraph.className = "links";
        linksParagraph.innerHTML = "<a href='http://127.0.0.1:5000/comments?id=${resultPostID}'>Read More</a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;<a href='http://127.0.0.1:5000/comments?id=${resultPostID}'>Comments</a>";

        /* append parent nodes to create html structure */
        contentDiv.appendChild(postDiv);

        // POST TITLE STRUCTURE
        postDiv.appendChild(postTitle);

        // POST DATE STRUCTURE
        postDiv.appendChild(postDate);

        // WHITESPACE DIV STRUCTURE
        postDiv.appendChild(whitespaceDiv);

        // READ MORE ENTRY STRUCTURE
        postDiv.appendChild(entryDiv);
        entryDiv.appendChild(linksParagraph);

    }
}

else {  // if the query didn't return any results
    var errorMessage = document.createElement("h1");
    errorMessage.style.color = "red";
    errorMessage.innerHTML = "No Posts Found";
    contentDiv.appendChild(errorMessage);
}
