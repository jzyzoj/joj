from flask import Flask
from flask_sqlalchemy import SQLAlchemy

oj=Flask(__name__)
oj.config.from_object("config")
db=SQLAlchemy(oj)

