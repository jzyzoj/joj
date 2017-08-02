from joj import BASE,session
from sqlalchemy import Column,Integer,String,Text,ForeignKey
from sqlalchemy.orm import relationship

class User(BASE):
    __tablename__="User"
    id=Column(Integer,primary_key=True)
    username=Column(String(40),unique=True,index=True)
    email=Column(String(40))
    password=Column(String(40))
    description=Column(Text)

    privilege=relationship("Privilege")
    informations=relationship("Informations")

    def __init__(self,username=None,email=None,password=None,description=None):
        self.username=username
        self.email=email
        self.password=password
        self.description=description

    def __repr__(self):
        return "<Username:%s Password:%s Email:%s>"%(self.username,self.password,self.email)

    def Save(self):
        session.add(self)
        session.commit()

    def Update(self,email=None,password=None,description=None):
        if email!=None:
            self.email=email
        if password!=None:
            self.password=password
        if description!=None:
            self.password=description
        session.commit()


class Privilege(BASE):
    __tablename__="Privilege"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User.id"),index=True)
    value=Column(Integer)
    
    def __init__(self,user_id=None,value=0):
        self.user_id=user_id
        self.value=value

    def __repr__(self):
        ret="<Id:%d Privilege:"%self.user_id
        for i in range(9) :
            if self.value&(1<<i):
                ret+='1'
            else:
                ret+='0'
        ret+='>'
        return ret

    def Query(self,value):
        return (self.value&value)==value

    def Authorize(self,value):
        self.value|=value
        session.commit()

    def Delete(self,value):
        self.value|=value
        self.value^=value
        session.commit()

    def Replace(self,value):
        self.value=value
        session.commit()

    def Show(self):
        return self.value


class Informations(BASE):
    __tablename__="User_Information"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User.id"),index=True)
    submit_num=Column(Integer)
    ac_num=Column(Integer)

    def __init__(self,user_id=None,submit_num=0,ac_num=0):
        self.user_id=user_id
        self.submit_num=submit_num
        self.ac_num=ac_num

    def __repr__(self):
        return "<Id:%d Status:%d/%d>"%(self.user_id,self.ac_num,self.submit_num)

    def Ac_rate(self):
        if self.submit_num==0:
            return "No submittion yet."
        return 1.0*ac_num/submit_num

    def Update(self,submit_num,ac_num):
        self.submit_num+=submit_num
        self.ac_num+=ac_num
        session.commit()


