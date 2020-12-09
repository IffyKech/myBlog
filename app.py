from flask import Flask, redirect, url_for, render_template, jsonify, request, session, abort
from src import db_scripts
import json
import os
import datetime
import webbrowser

app = Flask(__name__, static_url_path='')  # create instance of Flask server
app.secret_key = b'\x83r\xb6GA:\xa3k"\xf7\x8e\xf3j\xaf{\xfb'  # secret key for user session
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # set cache refresh to every 1 second


# TODO: plan out sessions so that each page redirects to login page if session doesn't exist


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
        fetch_query = 'SELECT title, postContent, postDate FROM postInfo ORDER BY postDate DESC '  # variable stores
        # the sql function that needs to be executed
        fetched_posts = database.cursor.execute(fetch_query).fetchall()  # cursor executes the function and gets all
        # results returned by the function
        data_dictionary = {}
        for count in range(len(fetched_posts)):
            data_dictionary[str(count) + '_title'] = fetched_posts[count][0]
            data_dictionary[str(count) + '_contents'] = fetched_posts[count][1]
            data_dictionary[str(count) + '_date'] = fetched_posts[count][2]
    return render_template("index.html", fetched_posts=fetched_posts, data_dictionary=data_dictionary)


@app.route('/profile')
def render_profile():
    if 'username' not in session:  # if there hasn't been a session created (no login yet)
        return redirect(url_for('render_login'))  # redirect the user to login
    return render_template("profile.html")


@app.route('/search')
def render_search():
    if 'username' not in session:  # if there hasn't been a session created (no login yet)
        return redirect(url_for('render_login'))  # redirect the user to login
    return render_template("search.html")


@app.route('/search', methods=['POST'])
def return_searched_post():
    tag_being_searched_for = request.form['s']  # get the value of the search bar input
    select_posts_query = "SELECT postInfo.postid, title, postdate, userPosts.userid, userInfo.username FROM postInfo, "\
                         "userPosts, userInfo WHERE (SELECT tag FROM tag) LIKE ? AND userPosts.postid = " \
                         "postInfo.postid AND userInfo.userid = userPosts.userid"  # select all posts that
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
    query_results = database.cursor.fetchall()
    database.close()

    return render_template("post.html", results=query_results)  # return the page and the results variable to the page


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
