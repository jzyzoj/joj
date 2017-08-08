from joj import oj
from flask import url_for,redirect,render_template


@oj.route("/login")
def login():
    return render_template("login.html")


@oj.route("/register")
def register():
    return render_template("register.html")


@oj.route("/logout")
def logout():
    return redirect(url_for("/"))


