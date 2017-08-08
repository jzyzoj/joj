from sqlalchemy import Column,Double,Integer,String,Text,ForeignKey
from sqlalchemy.orm import relationship
from joj.models.contest import Con_ass_User
from joj import BASE,solver
from joj.configer import Online_time
from random import randint


class Session():
    __tablename__="Session"
    id=Column(String(55),primary_key=True)
    user_id=Column(Integer,index=True,ForeignKey("User.id"))
    login_time=Column(Double)

    user=relationship("User")

    def __init__(self,dicter):
        user_id=dicter["user_id"]
        login_time=solver.Get_cur_time(True)
        id=str(randint(1,1e51))
        
    def __repr__(self):
        return "<Session:%d user:%d>"%(self.id,user_id)

    def Delete(self):
        solver.Delete(self)

    def is_valid(self):
        now=solver.Get_cur_time(True)
        if now-login_time>=Online_time:
            solver.Delete(Session,self)
            return False
        return True


class User(BASE):
    __tablename__="User"
    id=Column(Integer,primary_key=True)
    username=Column(String(40),unique=True,index=True)
    email=Column(String(40))
    password=Column(String(40))
    description=Column(Text)

    privileges=relationship("Privileges")
    informations=relationship("Informations")
    articles=relationship("Articles")
    Contests=relationship(
            "Contest",
            secondary=Con_ass_User,
            back_populates="Players"
            )

    def __init__(self,dicter):
        self.username=dicter['username']
        self.email=dicter['email']
        self.password=dicter['password']
        self.description=dicter['description']

    def __repr__(self):
        return "<Username:%s Password:%s Email:%s>"%(self.username,self.password,self.email)

    def Save(self):
        solver.Add(self)

    def Update(self,username=None,email=None,password=None)
        if username:
            self.username=username
        if email:
            self.email=email
        if password:
            self.password=password
        solver.Update()

    def Delete(self)
        self.privileges=0
        solver.Update()

class Privileges(BASE):
    __tablename__="Privileges"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User.id"),index=True)
    value=Column(Integer)
    
    def __init__(self,dicter):
        self.user_id=dicter['user_id']
        self.value=dicter['value']

    def __repr__(self):
        ret="<Id:%d Privileges:"%self.user_id
        for i in range(9) :
            if self.value&(1<<i):
                ret+='1'
            else:
                ret+='0'
        ret+='>'
        return ret

    def Save(self):
        solver.Add(self)

    def Query(self,value):
        return (self.value&value)==value

    def Authorize(self,value):
        self.value|=value
        solver.Update(Privileges,self)

    def Cancel_Privilege(self,value):
        self.value|=value
        self.value^=value
        solver.Update()

    def Replace(self,value):
        self.value=value
        solver.Update()

    def Show(self):
        return self.value

class Informations(BASE):
    __tablename__="User_Informations"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("User.id"),index=True)
    submit_num=Column(Integer)
    ac_num=Column(Integer)

    def __init__(self,dicter):
        self.user_id=dicter['user_id']
        self.submit_num=dicter['submit_num']
        self.ac_num=dicter['ac_num']

    def __repr__(self):
        return "<Id:%d Status:%d/%d>"%(self.user_id,self.ac_num,self.submit_num)

    def Save(self):
        solver.Add(self)

    def Ac_rate(self):
        if self.submit_num==0:
            return "No submittion yet."
        return ('%.2f')%(1.0*ac_num/submit_num*100)

    def Update(self,submit_num,ac_num):
        self.submit_num+=submit_num
        self.ac_num+=ac_num
        solver.Update()


