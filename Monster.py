from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import re
from Creature import *

engine = create_engine('sqlite:///monsters.db')
Base = declarative_base()


########################################################################
class Monster(Base):
    """"""
    __tablename__ = "Monsters"

    Id = Column(Integer, primary_key=True)
    Creature_Id = Column(Integer, ForeignKey(Creature.Id))
    Environment = Column(String(100))
    Source = Column(String(25))
    Description = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, data):
        """"""
        try:
            self.creature = Creature(data)
            self.Creature_Id = self.creature.Id
            self.Environment = data ["Environment"]
            self.Source = data["Source"]
            self.Description = data["Description_Visual"]
        except ValueError:
            print(data["Name"])
            raise


# create tables
Base.metadata.create_all(engine)