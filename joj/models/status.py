from joj import BASE,solver
from sqlalchemy import Boolean,Integer,String,Column,Text
from users import User
from joj.configer import Judge_Status
from sqlalchemy import ForeignKey

class Status(BASE):
    __tablename__="Status"
    id=Column(Integer,primary_key=True)
    date=Column(String(20),nullable=False)

    scores=Column(Integer,nullable=False)
    results=Column(Integer,nullable=False) #Judge Status

    ispublic=Column(Boolean,nullable=False)
    code_location=Column(String(50),nullable=False)

    user_id=Column(Integer,index=True,nullable=False)
    problem_id=Column(Integer,index=True,nullable=False)
    constest_id=Column(
            Integer,
            ForeignKey('contests.id')
            )

    def __init__(self,dicter):
       self.scores=dicter['scores']
       self.results=dicter['results']
       self.user_id=dicter['user_id']
       self.problem_id=dicter['problem_id']
       self.date=solver.Get_Cur_time()
       self.ispublic=dicter['ispublic']
       self.code_location=dicter['codeloc']

    def __repr__(self):
        strr=Judge_Status[self.results]
        return "<Pro:%d User:%d Status:%s Scores:%d/100 Date:%s>"%(self.problem_id,self.user_id,strr,self.scores,self.date)

    def Save(self):
        solver.Add(self)

    def Delete(self):
        solver.Delete(self)
        
    def View_status(self,ispublic):
        if self.ispublic==ispublic:
            return 
        self.ispublic=ispublic
        solver.Update()

