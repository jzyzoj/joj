from joj import BASE,session
from sqlalchemy import Column,Integer,String


class Comments(BASE):
    __tablename__="Comments"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("Users.id"),index=True)
    problem_id=Column(Integer,ForeignKey("Problems.id"))
    


