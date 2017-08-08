from joj import oj
from flask import render_template



@oj.route('/')
def index():
    return render_template("index.html")


@oj.route('/error')
def error():
    return render_template("error.html")

    
@oj.route('/help')
def help():
    return render_template("help.html")
