from flask import url_for,redirect

def Show_error(description,nextpage):
    return redirect(url_for("error",info=decription,nextpage=nextpage))

def Unlogin():
    return Show_error("You need to login.","login.html")

def Permission_deny():
    return Show_error("Permission deny.","index.html")



