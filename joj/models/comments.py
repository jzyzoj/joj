from joj import BASE,solver
from users import User
from sqlalchemy import Column,Text,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class Comments(BASE):
    __tablename__="Comments"
    id=Column(Integer,primary_key=True)
    contents=Column(Text)
    date=Column(String(20))
    
    user_id=Column(Integer,index=True)
    article_id=Column(Integer,ForeignKey("Articles.id"),index=True)

    def __init__(self,dicter):
        self.user_id=dicter['user_id']
        self.article_id=dicter['article_id']
        self.contents=dicter['contents']
        self.date=solver.Get_cur_time()

    def __repr__(self):
        talker=session.query(User).filter(id==user_id).first()
        return "<%s from %s:%r>"%(date,talker.username,contents)

    def Save(self):
        solver.Add(self)

    def Delete(self):
        solver.Delete(self)


class Articles(BASE):
    __tablename__="Articles"
    id=Column(Integer,primary_key=True)
    title=Column(Text)
    contents=Column(Text)
    date=Column(String(20))
 
    user_id=Column(Integer,ForeignKey("User.id"),index=True)
    problem_id=Column(Integer,ForeignKey("problems.id"),index=True)

    the_comments=relationship("Comments")

    def __init__(self,dicter):
        self.title=dicter['title']
        self.contents=dicter['contents']
        self.date=solver.Get_cur_time()
        self.user_id=dicter['user_id']
        self.problem_id=dicter['problem_id']

    def __repr__(self):
        return "<title:%r Date:%s>"%(self.title,self.date)

    def Save(self):
        self.Add(self)

    def Delete(self):
        for i in the_comments:
            i.Delete()
        solver.Delete(self)
    


