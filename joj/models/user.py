from joj import BASE
from sqlalchemy import Column,Integer,String,Text

class User(BASE):
    __tablename__="User"
    id=Column(Integer,primary_key=True)
    username=Column(String(40),unique=True,index=True)
    email=Column(String(40))
    password=Column(String(40))
    description=Column(Text)
    
    def __init__(self,username=None,email=None,password=None,description=None):
        self.username=username
        self.email=email
        self.password=password
        self.description=description

class Privilege(BASE):
    __tablename__="Privilege"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,index=True)
    value=Column(Integer)
    
    def __init__(self,user_id=None,value=0):
        self.user_id=user_id
        self.value=value

    def Query(self,value):
        return (self.value&value)==value

    def Authorize(self,value):
        self.value|=value
