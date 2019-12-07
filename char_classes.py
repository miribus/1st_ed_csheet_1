from enum import Enum
import re

class race_class_choices(Enum):
    Cleric = 1
    Druid = 2
    Fighter = 3
    Thief = 4
    Assassin = 5
    Ranger = 6
    Illusionist = 7
    ClericFighter = 8
    ClericFighterMagicUser = 9
    ClericRanger = 10
    ClericThief = 11
    ClericAssassin = 12
    FighterMagicUser = 13
    FighterIllusionist = 14
    FighterThief = 15
    FighterAssassin = 16
    FighterMagicUserThief = 17
    IllusionistThief = 18
    MagicUserThief = 19


def race_classes(rolls, race, race_class_choices):
    if race == "Elf":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter", "Cleric/Fighter/Magic-User", "Cleric/Ranger (UA)", "Cleric/Magic-User (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Magic-User", "Fighter/Illusionist (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)",
                         "Magic-User/Thief"]
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
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)",
                         "Magic-User/Thief"]
    elif race == "Human":
        class_choices = ["Fighter", "Ranger", "Paladin", "Cleric", "Druid", "Thief", "Assassin", "Magic-User", "Illusionist"]

    result = False
    while not result:
        for c in class_choices:
            class_ch = re.sub(r' \(UA\)|/|-', '', str(c))
            for rc in race_class_choices:
                if str(rc.name) == str(class_ch):
                    print(rc.value, c)

        choices = input("Choose a Class NUMBER:")
        if choices.isdigit():
            if choices in range(1, 20):
                for rc in race_class_choices:
                    if str(choices) == str(rc.value):
                        choices = str(rc.name)
                        print(choices)

                stop = False
                classlist = []
                while len(choices) > 0 and not stop:
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
                if len(choices) > 1 or stop:
                    print("This choice isn't valid, try again.")
                else:
                    result = input("Agreed? Y/N")
                    if result.isalpha():
                        if "y".upper() == result.upper():
                            #result = True
                            return classlist