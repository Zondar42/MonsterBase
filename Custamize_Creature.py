
from Creature import *

def Change_Stat(Creature, stat, value):
    #Update derived stats
    if stat == "str":
        Creature = Change_STR(Creature, value)
    elif stat == "dex":
        Creature = Change_DEX(Creature, value)
    elif stat == "con":
        Creature = Change_CON(Creature, value)
    elif stat == "int":
        Creature = Change_INT(Creature, value)
    elif stat == "wis":
        Creature = Change_WIS(Creature, value)
    elif stat == "cha":
        Creature = Change_CHA(Creature, value)
    #Update skills
    return Creature

def Change_STR(Creature, new_str):
    return Creature

def Change_DEX(Creature, new_dex):
    return Creature

def Change_CON(Creature, new_con):
    return Creature

def Change_INT(Creature, new_int):
    return Creature

def Change_WIS(Creature, new_wis):
    return Creature

def Change_CHA(Creature, new_cha):
    return Creature