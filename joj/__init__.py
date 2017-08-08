from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

oj=Flask(__name__)
oj.config.from_object("config")

DB_CON_STR="mysql+mysqldb://root:123@localhost/joj?charset=utf8"
engine=create_engine(DB_CON_STR,convert_unicode=True)

BASE=declarative_base()
Session=sessionmaker(bind=engine)

import models,views,solver


