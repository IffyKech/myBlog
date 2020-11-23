from flask import Flask, redirect, url_for, render_template, jsonify, request
from src import db_scripts
import os
import datetime

app = Flask(__name__)


@app.route('/')
def login_redirect():
    """
    Automatically redirect to login page when application is started
    url_for('*arg*')
    *arg*: the function representing the url you want to redirect to

    :return:
    """
    return redirect(url_for('render_login'))


@app.route('/login')
def render_login():
    return "Login Page!"


@app.route('/index')
def render_index():
    return "Hello World!"


@app.route('/profile')
def render_profile():
    return "Profile Page!"


@app.route('/search')
def render_search():
    return "Search Page"


@app.route('/comments')
def render_post():
    return "Post Page"


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
    app.run()
