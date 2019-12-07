from enum import Enum
import re

def races_base(race, rolls):
    print("What GENDER are you playing?")
    result = False
    while not result:
        gender = input("M or F?")
        if gender.upper() == "M".upper() or gender.upper() == "F".upper():
            result = True
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
    else:
        print("Invalid race choice")
        result = False
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
        print("Insufficient! Minimum Wisdom of", wisdom, "required")
        return result
    if rolls["DEX"] < dexterity:
        print("Insufficient! Minimum Dexterity of", dexterity, "required")
        return result
    if rolls["CON"] < constitution:
        print("Insufficient! Minimum Wisdom of", constitution, "required")
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

class race_class_choices(Enum):
    Cleric = 909
    Druid = 919
    Fighter = 929
    Thief = 939
    Assassin = 949
    Ranger = 959
    Illusionist = 969
    ClericFighter = 979
    ClericFighterMagicUser = 989
    ClericRanger = 999
    ClericThief = 9109
    ClericAssassin = 9119
    FighterMagicUser = 9129
    FighterIllusionist = 9139
    FighterThief = 9149
    FighterAssassin = 9159
    FighterMagicUserThief = 9169
    IllusionistThief = 9179



def race_classes(rolls, race, race_class_choices):
    if race == "Elf":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter", "Cleric/Fighter/Magic-User", "Cleric/Ranger (UA)", "Cleric/Magic-User (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Magic-User", "Fighter/Illusionist (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)"]
    elif race == "Dwarf":
        class_choices = ["Cleric (UA)", "Fighter", "Thief", "Assassin", "Cleric/Fighter (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)"]
    elif race == "Half-Orc":
        class_choices = ["Cleric", "Fighter", "Thief", "Assassin", "Cleric/Fighter",
                         "Cleric/Thief", "Cleric/Assassin", "Fighter/Thief", "Fighter/Assassin"]
    elif race == "Halfling":
        class_choices = ["Cleric (UA)", "Druid (UA)", "Fighter", "Thief",  "Cleric/Fighter",
                         "Cleric/Thief (UA)", "Fighter/Thief"]
    elif race == "Gnome":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter", "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Illusionist",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Illusionist/Thief"]
    elif race == "Half-Elf":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter", "Cleric/Fighter/Magic-User", "Cleric/Ranger (UA)", "Cleric/Magic-User (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Magic-User", "Fighter/Illusionist (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)"]
    elif race == "Human":
        class_choices = ["Fighter", "Ranger", "Paladin", "Cleric", "Druid", "Thief", "Assassin", "Magic-User", "Illusionist"]

    result = False
    while not result:
        for c in class_choices:
            class_ch = re.sub(r' \(UA\)|/|-', '', str(c))
            for rc in race_class_choices:
                print(rc.value, c)

        choices = input("Choose a Class NUMBER:")

        for rc in race_class_choices:
            if choices == rc.value:
                choices = str(rc.name)

        stop = False
        remember_choice = choices
        while len(choices) > 0 and not stop:
            if "Cleric" in choices:
                if rolls["WIS"] < 9:
                    print("Not enough WIS!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
            elif "Druid" in choices:
                if rolls["WIS"] < 12:
                    print("Not enough WIS!")
                if rolls["CHA"] < 15:
                    print("Not enough CHA!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
            elif "Fighter" in choices:
                if rolls["STR"] < 9:
                    print("Not enough STR!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
            elif "Paladin" in choices:
                if rolls["STR"] < 12:
                    print("Not enough STR!")
                if rolls["INT"] < 9:
                    print("Not enough INT!")
                if rolls["WIS"] < 13:
                    print("Not enough WIS!")
                if rolls["CON"] < 9:
                    print("Not enough CON!")
                if rolls["CHA"] < 17:
                    print("Not enough CHA!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
            elif "Ranger" in choices:
                if rolls["STR"] < 13:
                    print("Not enough STR!")
                if rolls["INT"] < 13:
                    print("Not enough INT!")
                if rolls["WIS"] < 14:
                    print("Not enough WIS!")
                if rolls["CON"] < 14:
                    print("Not enough CON!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
            elif "Magic-User" in choices:
                if rolls["INT"] < 9:
                    print("Not enough INT!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
            elif "Illusionist" in choices:
                if rolls["INT"] < 15:
                    print("Not enough INT!")
                elif rolls["DEX"] < 16:
                    print("Not enough DEX!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
            elif "Thief" in choices:
                if rolls["STR"] < 12:
                    print("Not enough STR!")
                if rolls["DEX"] < 12:
                    print("Not enough DEX!")
                if rolls["INT"] < 11:
                    print("Not enough INT!")
                    stop = True
                else:
                    choices = choices.replace(str(choices), "")
        if len(choices) > 1:
            print("This choice isn't valid, try again.")
        else:
            result = input("Agreed? Y/N")
            if "y".upper() == result.upper():
                result = True



def base_bonuses(rolls, race, saves, race_abilities):
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
        saves["Rods, Staves, Wands:"] -= int(str(round(rolls["CON"] / 3.5))[0])
        saves["Poison:"] -= int(str(round(rolls["CON"] / 3.5))[0])
        saves["Spells:"] -= int(str(round(rolls["CON"] / 3.5))[0])
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
        saves["Poison:"] -= int(str(round(rolls["CON"] / 3.5))[0])
        saves["Spells:"] -= int(str(round(rolls["CON"] / 3.5))[0])
        saves["Rods, Staves, Wands:"] -= int(str(round(rolls["CON"] / 3.5))[0])
        race_abilities["Infravision"] = "30' (Or 60' if Stoutish)"
        race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Dwarven", "Orcish",
                                              "Common", "+{} more".format(rolls["INT"]-16)]
        race_abilities["Halfling Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        race_abilities["Detect Grade Underground"] = "d4, score 1-3"
        race_abilities["Determine Direction Underground"] = "d10, score 1-5"
    elif race == "Gnome":
        saves["Rods, Staves, Wands:"] -= int(str(round(rolls["CON"] / 3.5))[0])
        saves["Spells:"] -= int(str(round(rolls["CON"] / 3.5))[0])
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