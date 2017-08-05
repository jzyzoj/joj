from joj import BASE,session
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
        self.date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        talker=session.query(User).filter(id==user_id).first()
        return "<%s from %s:%r>"%(date,talker.username,contents)

    def Save(self):
        session.save(self)
        session.commit()

    def Delete(self):
        session.delete(self)
        session.commit()


class Articles(BASE):
    __tablename__="Articles"
    id=Column(Integer,primary_key=True)
    title=Column(Text)
    contents=Column(Text)
    date=Column(String(20))
 
    user_id=Column(Integer,ForeignKey("User.id"),index=True)
    problem_id=Column(Integer,index=True)

    the_comments=relationship("Comments")

    def __init__(self,dicter):
        self.title=dicter['title']
        self.contents=dicter['contents']
        self.date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user_id=dicter['user_id']
        self.problem_id=dicter['problem_id']

    def __repr__(self):
        return "<title:%r Date:%s>"%(self.title,self.date)

    def Save(self):
        session.add(self)
        session.commit()

    def Delete(self):
        for i in the_comments:
            i.Delete()
        session.delete(self)
        session.commit()




