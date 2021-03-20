from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Monster import *
from Creature import *
from NPC import *
from Search import *
from re import *
def print_menu():
    print("c> filter by CR ")
    #print("t> filter by type ")
    print("e> filter by environment ")
    #sprint("s> filter by source ")

def manage_cr_query(session):
    qry = session.query(func.max(Monster.CR).label("max_cr"),
                        func.min(Monster.CR).label("min_cr"),
                        )
    res = qry.one()
    desired_CR = input("Input desired CR (" + str(res.max_cr) + " to " + str(res.min_cr) + ")")
    s = select([Monster.Name, Monster.CR]).where(Monster.CR == float(desired_CR))
    result = session.execute(s)
    for row in result:
        print(row.Name)


def manage_env_pattern(session):
    # Get unique CR range
    s = select([Monster.Environment]).distinct()
    result = session.execute(s)
    env_list = list()
    # remove punctuation and seperate out words
    for row in result:
        txt = f"{row.Environment}"
        clean_txt = re.sub('[\,\(\)]', '', txt)
        for clean_word in clean_txt.split(" "):
            #if len(clean_word) == 0:
            #    break
            #if clean_word[-1] == 's':
            #    clean_word = clean_word[:-1]
            if clean_word.lower() not in env_list:
                env_list.append(clean_word.lower())
    filler_words = ["or", "of", "and", "any", "the", "only", "?", "cold", "warm", "temperate", "true", "relatively", \
                    "dry", "wet", "flat", "lands", "terrain"]
    for word in filler_words:
        if word in env_list:
            env_list.remove(word)
    for env in env_list:
        #print(env + "(" + env[-1] + ")")
        print(env)

def search_menu(cmd, session):
    cr_pattern = r"(C|CR)"
    type_pattern = r"(T|TYPE)"
    environment_pattern = r"(E|ENVIRONMENT)"
    source_pattern = r"(S|SOURCE)"

    if re.findall(cr_pattern, cmd, flags=re.IGNORECASE):
        return manage_cr_query(session)
    elif re.findall(environment_pattern, cmd, flags=re.IGNORECASE):
        return manage_env_pattern(session)
    else:
        print_menu()
        cmd = input(" filter option: ")
        return search_menu(cmd, session)

def main_loop(session):
    search_menu("", session)