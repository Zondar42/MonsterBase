from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from Creature import *

engine = create_engine('sqlite:///monsters.db')
Base = declarative_base()


########################################################################
class NPC(Base):
    """"""
    __tablename__ = "NPC"

    Id = Column(Integer, primary_key=True)
    Creature_Id = Column(Integer, ForeignKey(Creature.Id))
    Race = Column(String(50), nullable=False)
    Class = Column(String(20))
    Class_level = Column(Integer)

    # ----------------------------------------------------------------------
    def __init__(self, data):
        """"""
        try:
            self.Race = data["Race"]
            self.Class = data["Class"]
            self.creature = Creature(data)
            self.Creature_Id = self.creature.Id
        except ValueError:
            print(data["Name"])
            raise

# create tables
Base.metadata.create_all(engine)