let amountOfResults = results.length;
/*
Repeat the process of creating html for the posts, for as many posts as there are
 */
var content_div = document.getElementById("content");
for (let repeat = 0; repeat < amountOfResults; repeat++) {
    /* Get the Post details iteratively for each post */
    resultPostID = results[repeat][0];
    resultPostTitle = results[repeat][1];
    resultPostDate = results[repeat][2];

    /* Create the new HTML elements for the posts */
    /* POST TITLE */
    var postDiv = document.createElement("div");
    postDiv.className = "post";

    var postTitle = document.createElement("h2");
    postTitle.className = "title";
    postTitle.innerHTML = `<a href="#">${resultPostTitle}</a>`;

    /* POST DATE */
    var postDate = document.createElement("p");
    postDate.className = "meta";
    // TODO: replace the post id with the tag
    postDate.innerHTML = `<span class="date">${resultPostDate}</span><span class="posted">Post ID: ${resultPostID}</a>`;

    /* WHITESPACE DIV */
    var whitespaceDiv = document.createElement("div");
    whitespaceDiv.style.clear = "both";

    /* READ MORE ENTRY */
    var entryDiv = document.createElement("div");
    entryDiv.className = "entry";

    var linksParagraph = document.createElement("p");
    linksParagraph.className = "links";
    linksParagraph.innerHTML = "<a href='#'>Read More</a>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;<a href='#'>Comments</a>";

    /* append parent nodes to create html structure */
    content_div.appendChild(postDiv);

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