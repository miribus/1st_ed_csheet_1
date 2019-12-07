from enum import Enum
import re

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


def race_classes(rolls, race, race_class_choices):
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
                         "Monk", "Barbarian", "UAPaladin"]

    result = False
    while not result:
        for c in class_choices:
            class_ch = re.sub(r' \(UA\)|/|-', '', str(c))
            for rc in race_class_choices:
                if str(rc.name) == str(class_ch):
                    print(rc.value, c)

        choices = input("Choose a Class NUMBER:")
        if choices.isdigit():
            if int(choices) in range(1, 37):
                for rc in race_class_choices:
                    print(rc.name, rc.value)
                    if str(choices) == str(rc.value):
                        choices = str(rc.name)

                stop = False
                classlist = []
                while len(choices) > 0 and not stop:
                    stop = False
                    for i in classlist:
                        print("Class: ", i, "selected.")
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
                if len(choices) > 1:
                    print("This choice isn't valid, try again.")
                else:
                    result = input("Agreed? Y/N")
                    if result.isalpha():
                        if "y".upper() == result.upper():
                            #result = True
                            result = True
                            return classlist, result
        for c in class_choices:
            class_ch = re.sub(r' \(UA\)|/|-', '', str(c))
            for rc in race_class_choices:
                if str(rc.name) == str(class_ch):
                    print(rc.value, c)

        choices = input("Choose a Class NUMBER:")