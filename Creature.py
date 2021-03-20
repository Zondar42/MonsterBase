from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import re


engine = create_engine('sqlite:///monsters.db')
Base = declarative_base()
Creature_Curr_Id = 1

########################################################################
class Creature(Base):
    """"""
    __tablename__ = "Creature"

    Id = Column(Integer, primary_key=True, autoincrement=False)
    Name = Column(String(50), nullable=False)
    CR = Column(Float)
    XP = Column(Integer, nullable=False)
    # TODO: should be enum
    Alignment = Column(String(2), nullable=False)
    Size = Column(String(20), nullable=False)
    Type = Column(String(30), nullable=False)
    HP = Column(Integer, nullable=False)
    AC = Column(Integer, nullable=False)
    AC_mods = Column(String(100))
    # TODO: HD, CMB, CMD, F/R/W need to grab the first number
    # leaving the raw value as a seperate value
    HD = Column(String(20))
    CMB = Column(String, nullable=False)
    CMD = Column(String, nullable=False)
    Fort = Column(String, nullable=False)
    Ref = Column(String, nullable=False)
    Will = Column(String, nullable=False)

    Melee = Column(String(100))
    Ranged = Column(String(100))
    Reach = Column(Integer, nullable=False)
    Feats = Column(String(100))
    Skills = Column(String)
    Environment = Column(String(100))
    Source = Column(String(25))
    Description = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, data):
        """"""
        first_whole_number = r"([0-9+]).*"
        try:
            global Creature_Curr_Id
            self.Id = Creature_Curr_Id
            Creature_Curr_Id += 1
            self.Name = data["Name"]
            if data["CR"] == "-":
                self.CR = -1.0
            else:
                fract_match = re.findall(r"([0-9+])\/([0-9+])", data["CR"])
                if fract_match:
                    self.CR = float(fract_match[0][0])/float(fract_match[0][1])
                else:
                    self.CR = float(data["CR"])
            raw_xp_string = data["XP"]
            # xp strings are stored as "9,600"
            xp_string = re.sub(r"[^0-9]", "", raw_xp_string)
            if xp_string:
                self.XP = int(xp_string)
            else:
                self.XP = 0
            self.Class = data["Class"]
            self.Alignment = data["Alignment"]
            self.Size = data["Size"]
            self.Type = data["Type"]
            self.AC = data["AC"]
            self.AC_mods = data["AC_Mods"]
            try:
                self.HP = int(data["HP"])
            except ValueError:
                whole_number_match = re.findall(first_whole_number, data["CR"])

                if whole_number_match:
                    self.HP = int(whole_number_match[0][0])
                else:
                    #Debug
                    print("AC mods: " + data["AC_Mods"])
                    print("HP: " + data["HP"])
                    raise
            self.HD = data["HD"]
            self.CMB = data["CMB"]
            self.CMD = data["CMD"]
            self.Fort = data["Fort"]
            self.Ref = data["Ref"]
            self.Will = data["Will"]
            self.Melee = data["Melee"]
            self.Ranged = data["Ranged"]
            self.Reach = data["Reach"]
            self.Feats = data["Feats"]
            self.Skills = data["Skills"]
            self.Environment = data ["Environment"]
            self.Source = data["Source"]
            self.Description = data["Description_Visual"]
        except ValueError:
            print(data["Name"])
            raise


# create tables
Base.metadata.create_all(engine)