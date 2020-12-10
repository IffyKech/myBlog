from flask import Flask, redirect, url_for, render_template, jsonify, request, session, abort, Response
from src import db_scripts
import json
import os
import datetime
import webbrowser

app = Flask(__name__, static_url_path='')  # create instance of Flask server
app.secret_key = b'\x83r\xb6GA:\xa3k"\xf7\x8e\xf3j\xaf{\xfb'  # secret key for user session
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # set cache refresh to every 1 second


@app.route('/')
def login_redirect():
    """
    Automatically redirect to login page when application is started
    If the user has logged in recently and has a session, redirect to the homepage instead
    url_for('*arg*')
    *arg*: the function representing the url you want to redirect to

    :return:
    """
    if 'username' in session:  # if the user has already logged in and started a session
        return redirect(url_for('render_index'))  # redirect them to the home page
    else:  # if the user has not yet logged in
        return redirect(url_for('render_login'))  # redirect them to the login page


@app.route('/static/css/<file>')
def return_css(file):
    return app.send_static_file(file)


@app.route('/login')
def render_login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('username', None)  # destroy the session
    return redirect(url_for('render_login'))  # redirect the user to the login page


# LOGIN USER
@app.route('/login/user', methods=["POST"])
def authenticate_user_login():
    """
    This is the route for when a user fills a form and attempts a login.
    The POST method is used so the ajax call can post the details written in the forms
    The function gets the query string arguments and compares them with rows in the database to find a user match
    :return:
    """
    user_name = request.args["username"]
    password = request.args["password"]

    database = db_scripts.Database("blog.sqlite3")  # initialize database connection
    query = "SELECT userid FROM userInfo WHERE username=? AND userpassword=?"  # search for users with the
    database.cursor.execute(query, (user_name, password))
    results = database.cursor.fetchall()  # stores the results of the query in an array

    if len(results) > 0:  # if there was a match found and returned to the array
        database.close()  # close the database connection
        session["username"] = user_name  # set the username session to the user found
        return redirect(url_for("render_index"))  # redirect to the homepage

    else:
        database.close()
        abort(500)


# CREATE USER
@app.route('/login', methods=["POST"])
def create_new_user():
    user_name = request.args["username"]
    password = request.args["password"]
    database = db_scripts.Database("blog.sqlite3")

    """ Check to see if the username already exists """
    find_username_query = "SELECT username FROM userInfo"
    database.execute_query(find_username_query)
    results = database.cursor.fetchall()  # fetch all the rows into an array

    """ Compare user_name input to usernames in the database. If there's a match, exit. """
    for row in results:  # iterate over each result
        if user_name in row:
            abort(500)  # exit with status code 500

    """ No matches were found. """
    create_query = "INSERT INTO userInfo(username, userpassword) VALUES(?, ?)"
    database.cursor.execute(create_query, (user_name, password))
    database.connection.commit()  # save the database changes
    database.close()

    session['username'] = user_name  # set the session variable to the newly created username
    return redirect(url_for('login_redirect'))  # redirect them to the home page


@app.route('/home', methods=['GET'])
def render_index():
    if 'username' not in session:  # if there hasn't been a session created (no login yet)
        return redirect(url_for('render_login'))  # redirect the user to login
    else:
        database = db_scripts.Database("blog.sqlite3")  # creates a connection to the website's database
        fetch_query = 'SELECT postInfo.postid, title, postdate, userPosts.userid, userInfo.username, tag.tag FROM ' \
                      'postInfo, userPosts, userInfo, tag WHERE userPosts.postid = postInfo.postid AND ' \
                      'userInfo.userid = userPosts.userid AND tag.tagid = postInfo.tagid ORDER BY postdate DESC'  # 
        # variable stores the sql function that needs to be executed 
        fetched_posts = database.cursor.execute(
            fetch_query).fetchall()  # cursor executes the function and gets all results returned by the function
    fetch_query = 'SELECT * FROM tag ORDER BY tagid DESC '
    fetched_tags = database.cursor.execute(fetch_query)

    return render_template("index.html", fetched_posts=fetched_posts, fetched_tags=fetched_tags)


@app.route('/profile')
def render_profile():
    if 'username' not in session:  # if there hasn't been a session created (no login yet)
        return redirect(url_for('render_login'))  # redirect the user to login

    current_username = session["username"]  # get the currently logged in user's username

    return render_template("profile.html", username=current_username)


@app.route('/profile', methods=['POST'])
def change_password():
    username = session["username"]
    current_password = request.args["pwd"]
    new_password = request.args["new_pwd"]

    """Check to see if the username's password is valid"""
    validate_password_query = "SELECT userid from userInfo WHERE username=? AND userpassword=?"
    database = db_scripts.Database("blog.sqlite3")
    database.cursor.execute(validate_password_query, (username, current_password))
    result = database.cursor.fetchall()

    if len(result) > 0:  # if a result was found
        update_password_query = "UPDATE userInfo SET userpassword=? WHERE username=?"
        database.cursor.execute(update_password_query, (new_password, username))
        database.connection.commit()  # save the changes
        database.close()
        return Response("{'a':'b'}", status=200, mimetype='application/json')
    else:
        database.close()
        abort(500)


@app.route('/create/post', methods=['POST'])
def create_post():
    database = db_scripts.Database("blog.sqlite3")
    title = request.args["title"]
    content = request.args["content"]
    tag = request.args["tag"]
    post_date = datetime.datetime.today().strftime('%d/%m/%Y')
    
    """Get the current user's userID"""
    author_id_query = "SELECT userid FROM userInfo WHERE username = ?"
    database.cursor.execute(author_id_query, (session['username'],))
    author_id = database.cursor.fetchone()[0]
    
    """Get the tag's id"""
    tag_id_query = 'SELECT tag.tagid FROM tag WHERE tag = ?'
    database.cursor.execute(tag_id_query, (tag,))
    tag_id = database.cursor.fetchone()[0]
    
    """Create the new post with all the values"""
    insert_query = 'INSERT INTO postInfo(title, postcontent, postdate, tagid) VALUES (?,?,?,?)'
    database.cursor.execute(insert_query, (title, content, post_date, tag_id))
    
    """Get the newly created post's postID"""
    post_id_query = 'SELECT postid FROM postInfo WHERE title = (?) ORDER BY postid DESC'
    database.cursor.execute(post_id_query, (title,))
    post_id = database.cursor.fetchone()[0]
    
    """Insert to the post+user link table"""
    insert_link_query = 'INSERT INTO userPosts(userid,postid) VALUES (?,?)'
    database.cursor.execute(insert_link_query, (author_id, post_id))

    database.connection.commit()  # save the changes
    database.close()
    
    return Response("{'a':'b'}", status=200, mimetype='application/json')  # return a valid response


@app.route('/create/comment', methods=['POST'])
def create_comment():
    response = request.get_json()
    comment = response["comment"]
    post_id = response["postid"]
    current_date = datetime.datetime.today().strftime('%d/%m/%Y')
    database = db_scripts.Database("blog.sqlite3")

    """GET THE USER ID OF THE CURRENT USER"""
    user_id_query = "SELECT userid FROM userInfo WHERE username=?"
    database.cursor.execute(user_id_query, (session["username"],))
    user_id = database.cursor.fetchone()[0]

    """CREATE THE NEW COMMENT ROW"""
    create_comment_query = "INSERT INTO commentInfo(commentcontent, commentdate) VALUES(?, ?)"
    database.cursor.execute(create_comment_query, (comment, current_date))

    """GET THE NEWLY CREATED COMMENT'S commentid"""
    comment_id_query = "SELECT commentid FROM commentInfo WHERE commentcontent = (?) ORDER BY commentid DESC"
    database.cursor.execute(comment_id_query, (comment,))
    comment_id = database.cursor.fetchone()[0]

    """CREATE A NEW LINK BETWEEN THE POST AND THE NEWLY MADE COMMENT"""
    comment_link_query = "INSERT INTO comment(commentid, postid, userid) VALUES(?, ?, ?)"
    database.cursor.execute(comment_link_query, (comment_id, post_id, user_id))

    database.connection.commit()  # save the changes
    database.close()

    return Response("{'a':'b'}", status=200, mimetype='application/json')  # return a valid response


@app.route('/search')
def render_search():
    if 'username' not in session:  # if there hasn't been a session created (no login yet)
        return redirect(url_for('render_login'))  # redirect the user to login
    return render_template("search.html")


@app.route('/search', methods=['POST'])
def return_searched_post():
    tag_being_searched_for = request.form['s']  # get the value of the search bar input
    select_posts_query = "select postid, title, postdate, userid, username " \
                         "from postInfo, userInfo " \
                         "where tagid = (SELECT tagid from tag where tag like ?) and postid in (select postid from userPosts where userPosts.userid = userInfo.userid)"  # select all posts that
    # matched the tag being searched for
    database = db_scripts.Database("blog.sqlite3")  # initialize the database connection
    database.cursor.execute(select_posts_query, (f'%{tag_being_searched_for}%',))  # execute the query with the input
    query_results = database.cursor.fetchall()  # get the results in a list of tuples
    database.close()
    return render_template("search.html", json_results=query_results)  # return the page and the results variable to
    # the page


@app.route('/comments')
def render_post():
    if 'username' not in session:  # if there hasn't been a session created (no login yet)
        return redirect(url_for('render_login'))  # redirect the user to login
    post_id = request.args["id"]
    """ Select the post details being searched for (by post_id) and the details of the user who created the post"""
    select_post_query = "SELECT postInfo.postid ,postInfo.tagid, tag.tag, postInfo.postcontent, postInfo.title, " \
                        "postInfo.postdate, userInfo.userid, userInfo.username FROM postInfo, userInfo, " \
                        "tag WHERE postInfo.postid = (SELECT postid from userPosts where postid = ?) AND " \
                        "userInfo.userid = (SELECT userid from userPosts where postid = ?) AND tag.tagid = " \
                        "postInfo.tagid "

    database = db_scripts.Database("blog.sqlite3")
    database.cursor.execute(select_post_query, (post_id, post_id))
    select_post_query_results = database.cursor.fetchall()

    """ Select all the comments and the users who posted the comment for the specific post that's being searched for """
    select_comments_query = "select commentid, commentcontent, commentdate from commentInfo" \
                            " where commentid IN (select commentid from comment where postid=?)"
    database.cursor.execute(select_comments_query, (post_id))
    select_comments_query_results = database.cursor.fetchall()
    database.close()

    # return the page and the results variable to the page
    return render_template("post.html", post_results=select_post_query_results,
                           comment_results=select_comments_query_results)


def does_file_exist(file_to_find):
    """
    Searches for a file in the current directory
    :param file_to_find:
    :return: True if the file is in the directory
    :return: False if the file is *not* in the directory
    """
    for file in os.listdir():
        if file_to_find == file:
            return True
    return False


def main():
    if not does_file_exist("blog.sqlite3"):
        db_scripts.create_blog_database()
    webbrowser.open("http://127.0.0.1:5000/")  # open the website page automatically


if __name__ == '__main__':
    main()
    app.run()
