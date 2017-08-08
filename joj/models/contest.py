from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from joj import BASE,solver
from sqlalchemy.schema import Table

Con_ass_Pro = Table('Con_ass_Pro', BASE.metadata,
        Column('Problem_id', Integer, ForeignKey('problems.id')),
        Column('Contest_id', Integer, ForeignKey('contests.id'))
        )

Con_ass_User = Table('Con_ass_User', BASE.metadata,
        Column('Contest_id', Integer, ForeignKey('contests.id')),
        Column('User_id', Integer, ForeignKey('User.id'))
        )

class Contest(BASE):
    __tablename__ = "contests"

    id = Column(Integer, primary_key = True)
    Title = Column(String(40))

    Promblems = relationship(
            "Problem",
            secondary=Con_ass_Pro,
            )

    Announcement = Column(String(400))
    Date = Column(String(10))
    Scores = relationship("Status")
    Players = relationship(
            "User",
            secondary=Con_ass_User,
            back_populates="Contests"
            )

    Condition = Column(String(40))

    def __init__(self,C_data):
        self.Title = C_data['Title']
        self.Announcement = C_data['Ann']
        self.Date = C_data['Date']
        self.Condition = C_data['Con']
        self.save()
    
    def save(self):
        self.Add(self)

