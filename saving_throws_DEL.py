def class_saves(char_class):
    global saves
    if char_class == "asn":
        saves = assasin()
    elif char_class == "clr":
        saves = cleric()
    elif char_class == "dru":
        saves = druid()
    elif char_class == "ftr":
        saves = fighter()
    elif char_class == "ran":
        saves = ranger()
    elif char_class == "pal":
        saves = paladin()
    elif char_class == "mag":
        saves = magic_user()
    elif char_class == "ill":
        saves = illusionist()
    elif char_class == "thi":
        saves = thief()
    return saves

def assasin():
    saves = {"Rods, Staves, Wands:": 14,
             "Breath Weapon:": 16,
             "Poison": 13,
             "Death Magic:": 13,
             "Petrification, Polymorph:": 12,
             "Spells:": 15}
    return saves

def thief():
    saves = {"Rods, Staves, Wands:": 14,
             "Breath Weapon:": 16,
             "Poison": 13,
             "Death Magic:": 13,
             "Petrification, Polymorph:": 12,
             "Spells:": 15}
    return saves

def cleric():
    saves = {"Rods, Staves, Wands:": 14,
             "Breath Weapon:": 16,
             "Poison": 10,
             "Death Magic:": 10,
             "Petrification, Polymorph:": 13,
             "Spells:": 15}
    return saves

def druid():
    saves = {"Rods, Staves, Wands:": 14,
             "Breath Weapon:": 16,
             "Poison": 10,
             "Death Magic:": 10,
             "Petrification, Polymorph:": 13,
             "Spells:":15}
    return saves

def fighter():
    saves = {"Rods, Staves, Wands:": 16,
             "Breath Weapon:": 17,
             "Poison": 14,
             "Death Magic:": 14,
             "Petrification, Polymorph:": 15,
             "Spells:": 17}
    return saves

def paladin():
    saves = {"Rods, Staves, Wands:": 16,
             "Breath Weapon:": 17,
             "Poison": 14,
             "Death Magic:": 14,
             "Petrification, Polymorph:": 15,
             "Spells:": 17}
    return saves
def ranger():
    saves = {"Rods, Staves, Wands:": 16,
             "Breath Weapon:": 27,
             "Poison:": 14,
             "Death Magic:": 14,
             "Petrification, Polymorph:": 15,
             "Spells:": 17}
    return saves

def illusionist():
    saves = {"Rods, Staves, Wands:": 11,
             "Breath Weapon:": 15,
             "Poison:": 14,
             "Death Magic:": 14,
             "Petrification, Polymorph:": 13,
             "Spells:": 12}
    return saves

def magic_user():
    saves = {"Rods, Staves, Wands:": 11,
             "Breath Weapon:": 15,
             "Poison:": 14,
             "Death Magic:": 14,
             "Petrification, Polymorph:": 13,
             "Spells:": 12}
    return saves




#5-8 12 15 12 11 13
#9-12 10 14 11 10 11
#13-15 8 13 10 9 9