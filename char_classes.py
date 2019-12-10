from enum import Enum
import re, social_class

class race_class_choices(Enum):
    Cleric = 1
    ClericFighter = 2
    ClericMagicUser = 3
    ClericFighterMagicUser = 4
    ClericRanger = 5
    ClericThief = 6
    ClericAssassin = 7
    ClericIllusionist = 8
    ClericMagicUserThief = 9
    ClericFighterThief = 10
    Druid = 11
    DruidRanger = 12
    DruidFighter = 13
    DruidMagicUser = 14
    DruidThief = 15
    Fighter = 16
    FighterMagicUser = 17
    FighterIllusionist = 18
    FighterThief = 19
    FighterAssassin = 20
    FighterMagicUserThief = 21
    Ranger = 22
    RangerMagicUser = 23
    Paladin = 24
    UAPaladin = 35
    Thief = 26
    Assassin = 27
    MagicUser = 28
    MagicUserThief = 29
    MagicUserAssassin = 30
    Illusionist = 31
    IllusionistThief = 32
    IllusionistAssassin = 33
    Monk = 34
    Barbarian = 35
    Cavalier = 36


def race_classes(rolls, race, race_class_choices, soclass_limit):
    print(soclass_limit)
    if race == "Elf":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter (UA)", "Cleric/Fighter/Magic-User", "Cleric/Ranger (UA)", "Cleric/Magic-User (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Magic-User", "Fighter/Illusionist (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)",
                         "Magic-User/Thief", "Ranger/Magic-User (UA)", "Magic-User/Assassin (UA)", "Cleric/Fighter/Thief (UA)",
                         "Cleric/Magic-User/Thief (UA)"]
    elif race == "Dwarf":
        class_choices = ["Cleric (UA)", "Fighter", "Thief", "Assassin", "Cleric/Fighter (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)"]
    elif race == "Half-Orc":
        class_choices = ["Cleric", "Fighter", "Thief", "Assassin", "Cleric/Fighter",
                         "Cleric/Thief", "Cleric/Assassin", "Fighter/Thief", "Fighter/Assassin"]
    elif race == "Halfling":
        class_choices = ["Cleric (UA)", "Druid (UA)", "Fighter", "Thief",  "Cleric/Fighter (UA)",
                         "Cleric/Thief (UA)", "Fighter/Thief"]
    elif race == "Gnome":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter (UA)", "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Illusionist",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Illusionist/Thief", "Cleric/Illusionist (UA)",
                         "Illusionist/Assassin"]
    elif race == "Half-Elf":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter (UA)", "Cleric/Fighter/Magic-User", "Cleric/Ranger (UA)",
                         "Cleric/Magic-User (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Magic-User", "Fighter/Illusionist (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)",
                         "Magic-User/Thief", "Ranger/Magic-User (UA)", "Magic-User/Assassin (UA)",
                         "Cleric/Fighter/Thief (UA)",
                         "Cleric/Magic-User/Thief (UA)"]
    elif race == "Human":
        class_choices = ["Fighter", "Ranger", "Paladin", "Cleric", "Druid", "Thief", "Assassin", "Magic-User", "Illusionist",
                         "Monk", "Barbarian", "UAPaladin  (UA)", "Cavalier (UA)"]

    result = False
    while not result:
        classes = []
        for c in class_choices:
            class_ch = re.sub(r' \(UA\)|/|-', '', str(c))
            for rc in race_class_choices:
                if str(rc.name) == str(class_ch) and str(rc.name):
                    for s in soclass_limit:
                        if s in str(rc.name):
                            if str(rc.name) not in classes:
                                print(rc.value, c)
                                classes.append(str(rc.name))

        choices = input("Choose a Class NUMBER:")
        if choices.isdigit():
            if int(choices) in range(1, 37):
                for rc in race_class_choices:
                    #print(rc.name, rc.value)
                    if str(choices) == str(rc.value):
                        choices = str(rc.name)

                stop = False
                classlist = []
                while len(choices) > 0 and not stop:
                    stop = False
                    for c in classlist:
                        print("Class: ", classlist[-1], "Valid.")
                        break
                    if "Cleric" in choices:
                        if rolls["WIS"] < 9:
                            print("Not enough WIS!")
                            stop = True
                        else:
                            choices = choices.replace("Cleric", "")
                            classlist.append("Cleric")
                    elif "Thief" in choices:
                        if rolls["DEX"] < 9:
                            print("Not enough DEX!")
                            stop = True
                        else:
                            choices = choices.replace("Thief", "")
                            classlist.append("Thief")
                    elif "Druid" in choices:
                        if rolls["WIS"] < 12:
                            print("Not enough WIS!")
                        if rolls["CHA"] < 15:
                            print("Not enough CHA!")
                            stop = True
                        else:
                            choices = choices.replace("Druid", "")
                            classlist.append("Druid")
                    elif "Fighter" in choices:
                        if rolls["STR"] < 9:
                            print("Not enough STR!")
                            stop = True
                        else:
                            choices = choices.replace("Fighter", "")
                            classlist.append("Fighter")
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
                            choices = choices.replace("Paladin", "")
                            classlist.append("Paladin")
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
                            choices = choices.replace("Ranger", "")
                            classlist.append("Ranger")
                    elif "MagicUser" in choices:
                        if rolls["INT"] < 9:
                            print("Not enough INT!")
                            stop = True
                        else:
                            choices = choices.replace("MagicUser", "")
                            classlist.append("MagicUser")
                    elif "Illusionist" in choices:
                        if rolls["INT"] < 15:
                            print("Not enough INT!")
                        elif rolls["DEX"] < 16:
                            print("Not enough DEX!")
                            stop = True
                        else:
                            choices = choices.replace("Illusionist", "")
                            classlist.append("Illusionist")
                    elif "Assassin" in choices:
                        if rolls["STR"] < 12:
                            print("Not enough STR!")
                        if rolls["DEX"] < 12:
                            print("Not enough DEX!")
                        if rolls["INT"] < 11:
                            print("Not enough INT!")
                            stop = True
                        else:
                            choices = choices.replace("Assassin", "")
                            classlist.append("Assassin")
                    elif "Barbarian" in choices:
                        if rolls["STR"] < 15:
                            print("Not enough STR!")
                        if rolls["CON"] < 15:
                            print("Not enough CON!")
                        if rolls["DEX"] < 14:
                            print("Not enough DEX!")
                        if rolls["WIS"] > 16:
                            print("WIS TOO HIGH!")
                            stop = True
                        else:
                            choices = choices.replace("Barbarian", "")
                            classlist.append("Barbarian")
                    elif "Cavalier" in choices:
                        if rolls["STR"] < 15:
                            print("Not enough STR!")
                        if rolls["CON"] < 15:
                            print("Not enough CON!")
                        if rolls["DEX"] < 15:
                            print("Not enough DEX!")
                        if rolls["WIS"] < 10:
                            print("Not enough WIS!")
                            stop = True
                        else:
                            choices = choices.replace("Cavalier", "")
                            classlist.append("Cavalier")
                    elif "UAPaladin" in choices:
                        if rolls["STR"] < 15:
                            print("Not enough STR!")
                        if rolls["CON"] < 15:
                            print("Not enough CON!")
                        if rolls["DEX"] < 15:
                            print("Not enough DEX!")
                        if rolls["WIS"] < 13:
                            print("Not enough WIS!")
                        if rolls["CHA"] < 13:
                            print("Not enough CHA!")
                            stop = True
                        else:
                            choices = choices.replace("UAPaladin", "")
                            classlist.append("UAPaladin")
                    elif "UAPaladin" in choices:
                        if rolls["STR"] < 15:
                            print("Not enough STR!")
                        if rolls["CON"] < 11:
                            print("Not enough CON!")
                        if rolls["DEX"] < 15:
                            print("Not enough DEX!")
                        if rolls["WIS"] < 15:
                            print("Not enough WIS!")

                            stop = True
                        else:
                            choices = choices.replace("Monk", "")
                            classlist.append("Monk")
                if stop:
                    print("This choice isn't valid, try again.")
                else:
                    print("-------------")
                    for i in classlist:
                        print("Class: ", i, "selected.")
                    result = input("Agreed? Y/N")
                    if result.isalpha():
                        if "y".upper() == result.upper():
                            #result = True
                            result = True
                            return classlist, result



def class_saving_throws(classlist, saves):
    class_saves = {}
    class_saves["Poison"] = {"ClericDruid": 10, "ThiefAssassinMonk": 13, "MagicUserIllusionist": 14, "FighterRangerPaladinUAPaladinCavalier": 14}
    class_saves["Petrification"] = {"ThiefAssassinMonk": 12, "ClericDruid": 13, "MagicUserIllusionist": 14, "FighterRangerPaladinUAPaladinCavalier": 15}
    class_saves["Rods, Staves, Wands"] = {"MagicUserIllusionist": 11, "ThiefAssassinMonk": 14, "ClericDruid": 14, "FighterRangerPaladinUAPaladinCavalier": 16}
    class_saves["Breath Weapon"] = {"MagicUserIllusionist": 15, "ThiefAssassinMonk": 16, "ClericDruid": 16, "FighterRangerPaladinUAPaladinCavalier": 17}
    class_saves["Spells"] = {"MagicUserIllusionist": 12, "ThiefAssassinMonk": 15, "ClericDruid": 15, "FighterRangerPaladinUAPaladinCavalier": 17}

    class_saves_high = {}
    class_saves_high["Poison"] = 21
    class_saves_high["Petrification"] = 21
    class_saves_high["Rods, Staves, Wands"] = 21
    class_saves_high["Breath Weapon"] = 21
    class_saves_high["Spells"] = 21

    for c in classlist:
        for t in class_saves["Poison"]:
            if str(c) in t:
                if class_saves["Poison"][t] <= class_saves_high["Poison"]:
                    class_saves_high["Poison"] = class_saves["Poison"][t]
                    saves["Poison"] = class_saves["Poison"][t]

        for t in class_saves["Petrification"]:
            if str(c) in t:
                if class_saves["Petrification"][t] <= class_saves_high["Petrification"]:
                    class_saves_high["Petrification"] = class_saves["Petrification"][t]
                    saves["Petrification"] = class_saves["Petrification"][t]

        for t in class_saves["Rods, Staves, Wands"]:
            if str(c) in t:
                if class_saves["Rods, Staves, Wands"][t] <= class_saves_high["Rods, Staves, Wands"]:
                    class_saves_high["Rods, Staves, Wands"] = class_saves["Rods, Staves, Wands"][t]
                    saves["Rods, Staves, Wands"] = class_saves["Rods, Staves, Wands"][t]

        for t in class_saves["Breath Weapon"]:
            if str(c) in t:
                if class_saves["Breath Weapon"][t] <= class_saves_high["Breath Weapon"]:
                    class_saves_high["Breath Weapon"] = class_saves["Breath Weapon"][t]
                    saves["Breath Weapon"] = class_saves["Breath Weapon"][t]

        for t in class_saves["Spells"]:
            if str(c) in t:
                if class_saves["Spells"][t] <= class_saves_high["Spells"]:
                    class_saves_high["Spells"] = class_saves["Spells"][t]
                    saves["Spells"] = class_saves["Spells"][t]
    return saves



