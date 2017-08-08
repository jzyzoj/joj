from joj import oj
from flask import redirect,url_for,render_template

from joj.solver import Check_privilege
from joj.config import privilege_table
from .error_handler import Permssion_deny

@oj.route('/status')
def Status():
    
    return render_template("status.html")

@oj.route('/status/<id>')
def Detail(id):

    if Check_privilege(asker,id)==False :
        return Permisson_deny()
    return render_template("status_detail.html")






