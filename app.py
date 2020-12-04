from flask import Flask, redirect, url_for, render_template, jsonify, request, session
from src import db_scripts
import os
import datetime

app = Flask(__name__, static_url_path='')  # create instance of Flask server
app.secret_key = b'\x83r\xb6GA:\xa3k"\xf7\x8e\xf3j\xaf{\xfb'  # secret key for user session


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
    else:
        return redirect(url_for('render_login'))


@app.route('/static/css/<file>')
def return_css(file):
    return app.send_static_file(file)


@app.route('/login')
def render_login():
    return render_template("login.html")


# LOGIN USER
@app.route('/login', methods=["POST"])
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
    query = """SELECT userid FROM userInfo WHERE username=? AND userpassword=?""", (user_name, password)  # search for users with the
    database.execute_query(query)
    results = database.cursor.fetchall()  # stores the results of the query in an array

    if len(results > 0):  # if there was a match found and returned to the array
        print(results)
        database.close()  # close the database connection

    else:
        return "<p>No records Found</p>"

# CREATE USER
@app.route('/login', methods=["POST"])
def create_new_user():
    user_name = request.args["username"]
    password = request.args["password"]
    repeat_password = request.args["repeat_password"]

    if len(user_name < 1 or len(password) < 1 or len(repeat_password) < 1):  # if any of the fields are empty
        return "200 Please enter both a username and password"

    else:
        if repeat_password == password:  # if the user entered the same password correctly
            database = db_scripts.Database("blog.sqlite3")
            """ Check to see if the username already exists """
            username_exists = False
            find_username_query = "SELECT username FROM userInfo"
            database.execute_query(find_username_query)
            results = database.cursor.fetchall()  # fetch all the rows into an array
            """ Compare user_name input to usernames in the database. If there's a match, exit. """
            for row in results:  # iterate over each result
                if user_name in row:
                    return "200 User Already exists"  # exit
            """ No matches were found. """
            create_query = "INSERT INTO userInfo"


@app.route('/index')
def render_index():
    return render_template("index.html")


@app.route('/profile')
def render_profile():
    return render_template("profile.html")


@app.route('/search')
def render_search():
    return render_template("search.html")


@app.route('/comments')
def render_post():
    return render_template("post.html")


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


if __name__ == '__main__':
    main()
    app.run(debug=True)
