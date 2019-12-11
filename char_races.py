from enum import Enum
import re, dice

def races_base(race, rolls):
    print("What GENDER are you playing?")
    result = False
    if str(race).isdigit():
        if int(race) in range(0, 7):
            gender = input("M or F?")
            if gender.isalpha():
                if gender.upper() == "M".upper() or gender.upper() == "F".upper():
                    print(gender)
                    if race.upper() == "Dwarf".upper() or "0" == race:
                        race = "Dwarf"
                        result = dwarf(rolls, gender)
                    elif race.upper() == "Elf".upper() or "1" == race:
                        race = "Elf"
                        result = elf(rolls, gender)
                    elif race.upper() == "Gnome".upper() or "2" == race:
                        race = "Gnome"
                        result = gnome(rolls, gender)
                    elif race.upper() == "Half-Elf".upper() or "3" == race:
                        race = "Half-Elf"
                        result = half_elf(rolls, gender)
                    elif race.upper() == "Half-Orc".upper() or "4" == race:
                        race = "Half-Orc"
                        result = half_orc(rolls, gender)
                    elif race.upper() == "Human".upper() or "5" == race:
                        race = "Human"
                        result = human(rolls, gender)
                    elif race.upper() == "Halfling".upper() or "6" == race:
                        race = "Halfling"
                        result = halfling(rolls, gender)
    gender = "M"
    return race, result, gender

def minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma):
    result = False
    if rolls["STR"] < strength:
        print("Insufficient! Minimum Strength of", strength, "required")
        return result
    if rolls["INT"] < intelligence:
        print("Insufficient! Minimum Intelligence of", intelligence, "required")
        return result
    if rolls["WIS"] < wisdom:
        print(wisdom, rolls["WIS"])
        print("Insufficient! Minimum Wisdom of", wisdom, "required")
        return result
    if rolls["DEX"] < dexterity:
        print("Insufficient! Minimum Dexterity of", dexterity, "required")
        return result
    if rolls["CON"] < constitution:
        print("Insufficient! Minimum Constitution of", constitution, "required")
        return result
    if rolls["CHA"] < charisma:
        print("Insufficient! Minimum Charisma of", charisma, "required")
        return result
    result = True
    return result

def dwarf(rolls, gender):
    strength = 8
    if gender == "Female":
        mx_strength = 17
    else:
        mx_strength = 18
    dexterity = 3
    mx_dexterity = 17
    constitution = 12
    mx_constitution = 19
    intelligence = 3
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 16
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Dwarf character rolls.")
        return True
    else:
        return False


def elf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 16
    else:
        mx_strength = 18
    dexterity = 7
    mx_dexterity = 19
    constitution = 8
    mx_constitution = 18
    intelligence = 8
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 8
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Elf character rolls.")
        return True
    else:
        return False


def gnome(rolls, gender):
    strength = 6
    if gender == "Female":
        mx_strength = 15
    else:
        mx_strength = 18
    dexterity = 3
    mx_dexterity = 18
    constitution = 8
    mx_constitution = 18
    intelligence = 7
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Gnome character rolls.")
        return True
    else:
        return False


def half_elf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 17
    else:
        mx_strength = 18
    dexterity = 6
    mx_dexterity = 18
    constitution = 6
    mx_constitution = 18
    intelligence = 4
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Half-Elf character rolls.")
        return True
    else:
        return False


def half_orc(rolls, gender):
    strength = 6
    if gender == "Female":
        mx_strength = 18
    else:
        mx_strength = 18
    dexterity = 8
    mx_dexterity = 17
    constitution = 10
    mx_constitution = 19
    intelligence = 6
    mx_intelligence = 17
    wisdom = 3
    mx_wisdom = 14
    charisma = 3
    mx_charisma = 12
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Half-Orc character rolls.")
        return True
    else:
        return False


def human(rolls, gender):
    strength = 3
    mx_strength = 18
    dexterity = 3
    mx_dexterity = 18
    constitution = 3
    mx_constitution = 18
    intelligence = 3
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Human character rolls.")
        return True
    else:
        return False

def halfling(rolls, gender):
    strength = 6
    if gender == "Female":
        mx_strength = 14
    else:
        mx_strength = 17
    dexterity = 3
    mx_dexterity = 18
    constitution = 3
    mx_constitution = 19
    intelligence = 3
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 17
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Halfling character rolls.")
        return True
    else:
        return False

def base_bonuses(rolls, race, classlist):
    race_abilities ={}
    race_abilities["Save Bonus"] = {}
    if race == "Elf":
        rolls["DEX"] += 1
        rolls["CON"] -= 1
        race_abilities["Sleep/Charm Resistance"] = "90%"
        race_abilities["Combat Bonus"] = "Short/Long Swords +1 To Hit, Bows +1 To Hit"
        race_abilities["Infravision"] = "60'"
        race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Hobgoblin", "Orcish",
                                              "Gnoll", "Common", "+{} more".format(rolls["INT"]-15)]
        race_abilities["Elven Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)", "Secret: d6, Score 1-2 (Detect: 1-3)"]
    elif race == "Dwarf":
        rolls["CON"] += 1
        rolls["CHA"] -= 1
        race_abilities["Save Bonus"]["Rods, Staves, Wands"] = str('+')+str(int(str(round(rolls["CON"] / 3.5))[0]))
        race_abilities["Save Bonus"]["Poison"] = str('+')+str(int(str(round(rolls["CON"] / 3.5))[0]))
        race_abilities["Save Bonus"]["Spells"] = str('+')+str(int(str(round(rolls["CON"] / 3.5))[0]))
        race_abilities["Detect Grade Underground"] = "d4, score 1-3"
        race_abilities["Detect New Construction Underground"] = "d4, score 1-3"
        race_abilities["Detect Sliding/Shifting Construction Underground"] = "d6, score 1-4"
        race_abilities["Detect Stone Trapwork"] = "d4, score 1-2"
        race_abilities["Detect Depth Underground"] = "d4, score 1-2"
        race_abilities["Infravision"] = "60'"
        race_abilities["Racial Languages"] = ["Dwarven", "Gnome", "Goblin", "Kobold", "Orcish", "Common"]
        race_abilities["Combat Bonus"] = ["+1 To hit: Half-Orc, Goblin, Hobgoblin, Orc",
                                          "-4 Penalty to be hit by Enemy Giants, Titans, Ogres or, Trolls"]
    elif race == "Half-Orc":
        rolls["STR"] += 1
        rolls["CON"] += 1
        rolls["CHA"] -= 2
        race_abilities["Racial Languages"] = ["Orcish", "Common"]
        race_abilities["Infravision"] = "60'"
    elif race == "Halfling":
        rolls["STR"] -= 1
        rolls["DEX"] += 1
        race_abilities["Save Bonus"]["Poison"] = str('+')+str(int(str(round(rolls["CON"] / 3.5))[0]))
        race_abilities["Save Bonus"]["Spells"] = str('+')+str(str(round(rolls["CON"] / 3.5))[0])
        race_abilities["Save Bonus"]["Rods, Staves, Wands"] = str('+')+str(int(str(round(rolls["CON"] / 3.5))[0]))
        race_abilities["Infravision"] = "30' (Or 60' if Stoutish)"
        race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Dwarven", "Orcish",
                                              "Common", "+{} more".format(rolls["INT"]-16)]
        race_abilities["Halfling Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        race_abilities["Detect Grade Underground"] = "d4, score 1-3"
        race_abilities["Determine Direction Underground"] = "d10, score 1-5"
    elif race == "Gnome":
        race_abilities["Save Bonus"]["Rods, Staves, Wands:"] = str('+')+str(int(str(round(rolls["CON"] / 3.5))[0]))
        race_abilities["Save Bonus"]["Spells:"] = str('+')+str(int(str(round(rolls["CON"] / 3.5))[0]))
        race_abilities["Racial Languages"] = ["Dwarven", "Gnome", "Goblin", "Kobold", "Orcish", "Common",
                                              "Burrowing Mammal"]
        race_abilities["Infravision"] = "60'"
        race_abilities["Detect Grade Underground"] = "d10, score 1-8"
        race_abilities["Detect Unsafe Walls/Ceilings/Floors"] = "d10, score 1-7"
        race_abilities["Detect Depth Underground"] = "d10, score 1-6"
        race_abilities["Determine Direction Underground"] = "d10, score 1-5"
        race_abilities["Combat Bonus"] = ["+1 Kobolds, Goblions",
                                          "-4 To Be hit by, Gnolls, Trolls, Giants, Bugbaires, Giants, Titans"]
    elif race == "Half-Elf":
        race_abilities["Sleep/Charm Resistance"] = "30%"
        race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Hobgoblin", "Orcish",
                                              "Gnoll", "Common", "+{} more".format(rolls["INT"] - 16)]
        race_abilities["Infravision"] = "60'"
        race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)",
                                                 "Secret: d6, Score 1-2 (Detect: 1-3)"]
    fighters = ["Fighter", "Barbarian", "Cavalier", "Paladin", "UAPaladin", "Ranger"]
    rolls["EX_STR"] = False
    if rolls["STR"] == 18:
        for c in classlist:
            if str(c) in fighters:
                rolls["EX_STR"] = dice.exceptional_strength()


    return rolls, race_abilities