from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import copy
from Monster import *
from NPC import *

def open_db():
    engine = create_engine('sqlite:///monsters.db', echo=True)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def load_npc(session):
    # load bestiary
    with open(r"NPCS.csv", encoding='utf-8') as csvfile:
        spam_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"' )
        creature_list = []
        npc_list = []
        for row in spam_reader:
            # Create new entries
            new_npc = NPC(row)
            session.add(new_npc)
            #creature_list.append(new_npc.creature)
            session.add(new_npc.creature)
            #npc_list.append(new_npc)
        session.commit()
        # max_entries = 5
        # num_creatures = max_entries
        # for creature in creature_list:
        #     num_creatures -= 1
        #     if num_creatures <= 0:
        #         break
        # session.commit()
        #
        # num_npcs = max_entries
        # for npc in npc_list:
        #     session.add(npc)
        #     num_npcs -= 1
        #     if num_npcs <= 0:
        #         break
        # session.commit()

    print("num creatures: " + str(session.query(
          func.count(Creature.Id)).scalar()))

def load_monsters(session):
    with open(r"Bestiary_full.csv") as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=';')
        for row in spamreader:
            # Create new entries
            new_monster = Monster(row)
            session.add(new_monster)
    session.commit()


def load_csv():
    engine = create_engine('sqlite:///monsters.db', echo=True)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    load_npc(session)
    return session