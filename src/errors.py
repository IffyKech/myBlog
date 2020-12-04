from app import app
import db_scripts
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    render_template("404.html"), 404

@app.errorhandler(500)
def database_error(error):
    render_template("500.html"), 500