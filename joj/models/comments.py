from joj import BASE,session
from user import User
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class Comments(BASE):
    __tablename__="Comments"
    id=Column(Integer,primary_key=True)
    contents=Column(Text)
    date=Column(String)
    
    user_id=Column(Integer,index=True)
    article_id=Column(Integer,ForeignKey("Articles.id"),index=True)

    def __init__(self,user_id=None,article_id=None,contents=None,date=None):
        self.user_id=user_id
        self.article_id=article_id
        self.contents=contents
        self.date=date

    def __repr__(self):
        talker=session.query(User).filter(id==user_id).first()
        return "<%s from %s:%r>"%(Date,talker.username,contents)

    def Delete(self):
        session.delete(self)
        session.commit()


class Articles(BASE):
    __tablename__="Articles"
    id=Column(Integer,primary_key=True)
    title=Column(Text)
    contents=Column(Text)
    date=Column(String)

    user_id=Column(Integer,ForeignKey("Users.id"),index=True)
    problem_id=Column(Integer,index=True)

    the_comments=relationship("Comments")

    def __init__(self,title=None,contents=None,date=None,user_id=0,problem_id=0):
        self.title=title
        self.contents=contents
        self.date=date
        self.user_id=user_id
        self.problem_id=problem_id

    def __repr__(self):
        return "<title:%r Date:%s>"%(title,date)

    def Delete(self):
        for i in the_comments:
            i.Delete()
        session.delete(self)
        session.commit()




