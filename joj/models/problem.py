from joj import BASE,session
from sqlalchemy import Column, Integer, String, Text 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table


Hint_ass_Pro = Table('Hint_ass_Pro', BASE.metadata,
    Column('Problem_id', Integer, ForeignKey('problems.id')),
    Column('Hint_id', Integer, ForeignKey('hints.id'))
)

class Problem(BASE):
    __tablename__="problems"


    id = Column(Integer, primary_key=True) 
    Name = Column(String(40))
    Text = Column(Text)
    Examples = Column(String(100))
    Data = Column(String(100))
    Hints = relationship(
            "Hint",
            secondary=Hint_ass_Pro,
            back_populates="Problems"
            )


    Time_limit = Column(Integer)
    Memory_limit = Column(Integer)
    Judge_type = Column(String(50))
	
    ACnum = Column(Integer)
    SUBnum = Column(Integer)

    Articles = relationship("Articles")

    Contest_id = Column(Integer, ForeignKey('contests.id'))

	
    def __repr__(self):
        return '< Pro_id=%d , Pro_Name=%s >' %(self.id, self.Name)

    def save(self):
        session.add(self)
        session.commit()

    def __init__(self, P_data):
        self.Name=P_data['Name']
        self.Text=P_data['Text']
        self.Examples = P_data['Examples']
        self.Data = P_data['Data']
        self.Hint = P_data['Hint']
        self.Time_limit = P_data['Time']
        self.Memory_limit = P_data['Memory']
        self.Judge_type = P_data['Judge']
        self.ACnum = 0
        self.SUBnum= 0
        self.save()


    def update(self, P_data):
        self.Name = P_data['Name']
        self.Text = P_data['Text']
        self.Examples = P_data['Examples']
        self.Data = P_data['Data']
        self.Hint = P_data['Hint']
        self.Time_limit = P_data['Time']
        self.Memory_limit = P_data['Memory']
        self.Judge_type = P_data['Judge']
        self.ACnum = 0 
        self.SUBnum = 0
        self.save()


class Hint(BASE):
    __tablename__='hints'

    id = Column(Integer, primary_key=True)
    Name = Column(String(50))

    Problems = relationship(
            "Problem",
            secondary=Hint_ass_Pro,
            back_populates="Hints"
            )

    def __init__(self, Name):
        self.Name=Name
        self.save()

    def __repr__(self):
        return '< Hint_id=%d , Hint_Name=%s >' %(self.id, self.Name)

    def save(self):
        session.add(self)
        session.commit()


