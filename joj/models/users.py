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

    privileges=relationship("Privileges")
    informations=relationship("Informations")
    articles=relationship("Articles")

    def __init__(self,dicter):
        self.username=dicter['username']
        self.email=dicter['email']
        self.password=dicter['password']
        self.description=dicter['description']

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
        session.add(self)
        session.commit()

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
        session.add(self)
        session.commit()

    def Ac_rate(self):
        if self.submit_num==0:
            return "No submittion yet."
        return ('%.2f')%(1.0*ac_num/submit_num*100)

    def Update(self,submit_num,ac_num):
        self.submit_num+=submit_num
        self.ac_num+=ac_num
        session.commit()


