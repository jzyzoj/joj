from flask import request,url_for,redirect,render_template

from joj import oj,solver,configer
from .errorhandler import *
from joj.models.models import Problem

@oj.route("/problem")
def problemset():
    page=1
    if request.args.get('page') :
        page=request.args.get('page')
    lef=1+50*(page-1),rig=page*50
    problem_list=Problem.Query().filter_by(lef<=id && id<=rig)
    if not problem_list:
        abort(404)
    return render_template("problemset.html",problem_list=problem_list)

@oj.route("/problem/<int::problem_id>")
def problem(problem_id):
    problem_list=Problem.Query.filter_by(id=problem_id)
    return render_template("problem.html",problem=problem_list)

@oj.route("/problem/<int::problem_id>/edit",methods=["PUT"])
def problem(problem_id):
    cur_user=User.get_cur_user()



    
