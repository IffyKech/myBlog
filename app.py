from flask import Flask, redirect, url_for
import sqlite3
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


if __name__ == '__main__':
    app.run()
