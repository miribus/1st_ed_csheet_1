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
    Thief = 25
    Assassin = 26
    MagicUser = 27
    MagicUserThief = 28
    MagicUserAssassin = 29
    Illusionist = 30
    IllusionistThief = 31
    IllusionistAssassin = 32
    Monk = 33
    Barbarian = 34
    UAPaladin = 35
    Cavalier = 36


def race_classes(name):
    #print(name.soclass_limit)
    #print(name.char_race)
    if name.char_race == "Elf":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter (UA)", "Cleric/Fighter/Magic-User", "Cleric/Ranger (UA)",
                         "Cleric/Magic-User (UA)", "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Magic-User",
                         "Fighter/Illusionist (UA)", "Fighter/Thief", "Fighter/Assassin (UA)",
                         "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)", "Magic-User/Thief",
                         "Ranger/Magic-User (UA)", "Magic-User/Assassin (UA)", "Cleric/Fighter/Thief (UA)",
                         "Cleric/Magic-User/Thief (UA)", "Cavalier (UA)", "Druid/Ranger (UA)"]
    elif name.char_race == "Dwarf":
        class_choices = ["Cleric (UA)", "Fighter", "Thief", "Assassin", "Cleric/Fighter (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)"]
    elif name.char_race == "Half-Orc":
        class_choices = ["Cleric", "Fighter", "Thief", "Assassin", "Cleric/Fighter",
                         "Cleric/Thief", "Cleric/Assassin", "Fighter/Thief", "Fighter/Assassin", "Cleric/Fighter"]
    elif name.char_race == "Halfling":
        class_choices = ["Cleric (UA)", "Druid (UA)", "Fighter", "Thief",  "Cleric/Fighter (UA)",
                         "Cleric/Thief (UA)", "Fighter/Thief", "Cavalier (UA)"]
    elif name.char_race == "Gnome":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter (UA)", "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Illusionist",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Illusionist/Thief", "Cleric/Illusionist (UA)",
                         "Illusionist/Assassin"]
    elif name.char_race == "Half-Elf":
        class_choices = ["Cleric (UA)", "Druid", "Fighter", "Magic-User", "Thief", "Assassin", "Ranger", "Illusionist",
                         "Cleric/Fighter (UA)", "Cleric/Fighter/Magic-User", "Cleric/Ranger (UA)",
                         "Cleric/Magic-User (UA)",
                         "Cleric/Thief (UA)", "Cleric/Assassin (UA)", "Fighter/Magic-User", "Fighter/Illusionist (UA)",
                         "Fighter/Thief", "Fighter/Assassin (UA)", "Fighter/Magic-User/Thief", "Illusionist/Thief (UA)",
                         "Magic-User/Thief", "Ranger/Magic-User (UA)", "Magic-User/Assassin (UA)",
                         "Cleric/Fighter/Thief (UA)", "Cleric/Magic-User/Thief (UA)", "Druid/Ranger (UA)"]
    elif name.char_race == "Human":
        class_choices = ["Fighter", "Ranger", "Paladin", "Cleric", "Druid", "Thief", "Assassin", "Magic-User",
                         "Illusionist", "Monk", "Barbarian", "UAPaladin (UA)", "Cavalier (UA)"]

    result = False
    while not result:
        classes = []
        for c in class_choices:
            class_ch = re.sub(r' \(UA\)|/|-', '', str(c))

            for rc in race_class_choices:
                #print(class_ch, rc.name, rc.value, c)
                if str(rc.name) == str(class_ch) and str(rc.name) in name.soclass_limit:
                    #if str(rc.name) not in classes:
                    print(rc.value, c)
                    classes.append(str(rc.name))

        if name.methodv:
            print("You chose Method V and preselected your class")
            choices = name.methodv_choice
        else:
            choices = input("Choose a Class NUMBER:")

        if choices.isdigit():
            if int(choices) in range(1, 37):
                for rc in race_class_choices:
                    #print(rc.name, rc.value)
                    if str(choices) == str(rc.value):
                        choices = str(rc.name)

                stop = False
                name.classlist = []
                old_choices = choices
                while len(choices) > 0 and not stop:
                    stop = False
                    for c in name.classlist:
                        print("Class: ", name.classlist[-1], "Valid.")
                        break
                    if "Cleric" in choices:
                        if name.char_abilities["WIS"] < 9:
                            if name.methodv:
                                name.char_abilities["WIS"] = 9
                            else:
                                print("Not enough WIS!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Cleric", "")
                            name.char_class.append("Cleric")
                    elif "Thief" in choices:
                        if name.char_abilities["DEX"] < 9:
                            if name.methodv:
                                name.char_abilities["DEX"] = 9
                            else:
                                print("Not enough DEX!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Thief", "")
                            name.char_class.append("Thief")
                            name.char_race_abilities["Thief"] = {}
                            name = thief_adjustment(name)
                    elif "Druid" in choices:
                        if name.char_abilities["WIS"] < 12:
                            if name.methodv:
                                name.char_abilities["WIS"] = 12
                            else:
                                print("Not enough WIS!")
                                stop = True
                        if name.char_abilities["CHA"] < 15:
                            if name.methodv:
                                name.char_abilities["CHA"] = 15
                            else:
                                print("Not enough CHA!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Druid", "")
                            name.char_class.append("Druid")
                    elif "Fighter" in choices:
                        if name.char_abilities["STR"] < 9:
                            if name.methodv:
                                name.char_abilities["STR"] = 9
                            else:
                                print("Not enough STR!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Fighter", "")
                            name.char_class.append("Fighter")
                    elif "Paladin" == choices:
                        if name.char_abilities["STR"] < 12:
                            if name.methodv:
                                name.char_abilities["STR"] = 12
                            else:
                                print("Not enough STR!")
                                stop = True
                        if name.char_abilities["INT"] < 9:
                            if name.methodv:
                                name.char_abilities["INT"] = 9
                            else:
                                print("Not enough INT!")
                                stop = True
                        if name.char_abilities["WIS"] < 13:
                            if name.methodv:
                                name.char_abilities["WIS" ] = 13
                            else:
                                print("Not enough WIS!")
                                stop = True
                        if name.char_abilities["CON"] < 9:
                            if name.methodv:
                                name.char_abilities["CON"] = 9
                            else:
                                print("Not enough CON!")
                                stop = True
                        if name.char_abilities["CHA"] < 17:
                            if name.methodv:
                                name.char_abilities["CHA"] = 17
                            else:
                                print("Not enough CHA!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Paladin", "")
                            name.char_class.append("Paladin")
                    elif "Ranger" in choices:
                        if name.char_abilities["STR"] < 13:
                            if name.methodv:
                                name.char_abilities["STR"] = 13
                            else:
                                print("Not enough STR!")
                                stop = True
                        if name.char_abilities["INT"] < 13:
                            if name.methodv:
                                name.char_abilities["INT"] = 13
                            else:
                                print("Not enough INT!")
                                stop = True
                        if name.char_abilities["WIS"] < 14:
                            if name.methodv:
                                name.char_abilities["WIS"] = 14
                            else:
                                print("Not enough WIS!")
                                stop = True
                        if name.char_abilities["CON"] < 14:
                            if name.methodv:
                                name.char_abilities["CON"] = 14
                            else:
                                print("Not enough CON!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Ranger", "")
                            name.char_class.append("Ranger")
                    elif "MagicUser" in choices:
                        if name.char_abilities["INT"] < 9:
                            if name.methodv:
                                name.char_abilities["INT"] = 9
                            else:
                                print("Not enough INT!")
                                stop = True
                        if not stop:
                            choices = choices.replace("MagicUser", "")
                            name.char_class.append("MagicUser")
                    elif "Illusionist" in choices:
                        if name.char_abilities["INT"] < 15:
                            if name.methodv:
                                name.char_abilities["INT"] = 15
                            else:
                                print("Not enough INT!")
                                stop = True
                        elif name.char_abilities["DEX"] < 16:
                            if name.methodv:
                                name.char_abilities["DEX"] = 16
                            else:
                                print("Not enough DEX!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Illusionist", "")
                            name.char_class.append("Illusionist")
                    elif "Assassin" in choices:
                        if name.char_abilities["STR"] < 12:
                            if name.methodv:
                                name.char_abilities["STR"] = 12
                            else:
                                print("Not enough STR!")
                                stop = True
                        if name.char_abilities["DEX"] < 12:
                            if name.methodv:
                                name.char_abilities["DEX"] = 12
                            else:
                                print("Not enough DEX!")
                                stop = True
                        if name.char_abilities["INT"] < 11:
                            if name.methodv:
                                name.char_abilities["INT"] = 11
                            else:
                                print("Not enough INT!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Assassin", "")
                            name.char_class.append("Assassin")
                    elif "Barbarian" in choices:
                        if name.char_abilities["STR"] < 15:
                            if name.methodv:
                                name.char_abilities["STR"] = 15
                            else:
                                print("Not enough STR!")
                                stop = True
                        if name.char_abilities["CON"] < 15:
                            if name.methodv:
                                name.char_abilities["CON"] = 15
                            else:
                                print("Not enough CON!")
                                stop = True
                        if name.char_abilities["DEX"] < 14:
                            if name.methodv:
                                name.char_abilities["DEX"] = 14
                            else:
                                print("Not enough DEX!")
                                stop = True
                        if name.char_abilities["WIS"] > 16:
                            if name.methodv:
                                name.char_abilities["WIS"] = 16
                            else:
                                print("WIS TOO HIGH!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Barbarian", "")
                            name.char_class.append("Barbarian")
                    elif "Cavalier" in choices:
                        if name.char_abilities["STR"] < 15:
                            if name.methodv:
                                name.char_abilities["STR"] = 15
                            else:
                                print("Not enough STR!")
                                stop = True
                        if name.char_abilities["CON"] < 15:
                            if name.methodv:
                                name.char_abilities["CON"] = 15
                            else:
                                print("Not enough CON!")
                                stop = True
                        if name.char_abilities["DEX"] < 15:
                            if name.methodv:
                                name.char_abilities["DEX"] = 15
                            else:
                                print("Not enough DEX!")
                                stop = True
                        if name.char_abilities["WIS"] < 10:
                            if name.methodv:
                                name.char_abilities["WIS"] = 10
                            else:
                                print("Not enough WIS!")
                                stop = True
                        if name.char_abilities["INT"] < 10:
                            if name.methodv:
                                name.char_abilities["INT"] = 10
                            else:
                                print("Not enough INT!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Cavalier", "")
                            name.char_class.append("Cavalier")
                    elif "UAPaladin" == choices:
                        if name.char_abilities["STR"] < 15:
                            if name.methodv:
                                name.char_abilities["STR"] = 15
                            else:
                                print("Not enough STR!")
                                stop = True
                        if name.char_abilities["CON"] < 15:
                            if name.methodv:
                                name.char_abilities["CON"] = 15
                            else:
                                print("Not enough CON!")
                                stop = True
                        if name.char_abilities["DEX"] < 15:
                            if name.methodv:
                                name.char_abilities["DEX"] = 15
                            else:
                                print("Not enough DEX!")
                                stop = True
                        if name.char_abilities["WIS"] < 13:
                            if name.methodv:
                                name.char_abilities["WIS"] = 13
                            else:
                                print("Not enough WIS!")
                                stop = True
                        if name.char_abilities["INT"] < 10:
                            if name.methodv:
                                name.char_abilities["INT"] = 10
                            else:
                                print("Not enough INT!")
                                stop = True
                        if name.char_abilities["CHA"] < 17:
                            if name.methodv:
                                name.char_abilities["CHA"] = 17
                            else:
                                print("Not enough CHA!")
                                stop = True
                        if not stop:
                            choices = choices.replace("UAPaladin", "")
                            name.char_class.append("UAPaladin")
                    elif "Monk" in choices:
                        if name.char_abilities["STR"] < 15:
                            if name.methodv:
                                name.char_abilities["STR"] = 15
                            else:
                                print("Not enough STR!")
                                stop = True
                        if name.char_abilities["CON"] < 11:
                            if name.methodv:
                                name.char_abilities["CON"] = 11
                            else:
                                print("Not enough CON!")
                                stop = True
                        if name.char_abilities["DEX"] < 15:
                            if name.methodv:
                                name.char_abilities["DEX"] = 15
                            else:
                                print("Not enough DEX!")
                                stop = True
                        if name.char_abilities["WIS"] < 15:
                            if name.methodv:
                                name.char_abilities["WIS"] = 15
                            else:
                                print("Not enough WIS!")
                                stop = True
                        if not stop:
                            choices = choices.replace("Monk", "")
                            name.char_class.append("Monk")
                if stop:
                    print("This choice isn't valid, try again.")
                    name.char_class = []
                    result = False
                else:
                    print("-------------")
                    for i in name.char_class:
                        print("Class: ", i, "selected.")
                    result = input("Agreed? Y/N")
                    if "y".upper() == str(result).upper():
                        #result = True
                        result = True
                        return name, result
                    else:
                        name.char_class = []
                        result = False



def class_saving_throws(name):
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

    for c in name.char_class:
        for t in class_saves["Poison"]:
            if str(c) in t:
                if class_saves["Poison"][t] <= class_saves_high["Poison"]:
                    class_saves_high["Poison"] = class_saves["Poison"][t]
                    name.char_saves["Poison"] = class_saves["Poison"][t]

        for t in class_saves["Petrification"]:
            if str(c) in t:
                if class_saves["Petrification"][t] <= class_saves_high["Petrification"]:
                    class_saves_high["Petrification"] = class_saves["Petrification"][t]
                    name.char_saves["Petrification"] = class_saves["Petrification"][t]

        for t in class_saves["Rods, Staves, Wands"]:
            if str(c) in t:
                if class_saves["Rods, Staves, Wands"][t] <= class_saves_high["Rods, Staves, Wands"]:
                    class_saves_high["Rods, Staves, Wands"] = class_saves["Rods, Staves, Wands"][t]
                    name.char_saves["Rods, Staves, Wands"] = class_saves["Rods, Staves, Wands"][t]

        for t in class_saves["Breath Weapon"]:
            if str(c) in t:
                if class_saves["Breath Weapon"][t] <= class_saves_high["Breath Weapon"]:
                    class_saves_high["Breath Weapon"] = class_saves["Breath Weapon"][t]
                    name.char_saves["Breath Weapon"] = class_saves["Breath Weapon"][t]

        for t in class_saves["Spells"]:
            if str(c) in t:
                if class_saves["Spells"][t] <= class_saves_high["Spells"]:
                    class_saves_high["Spells"] = class_saves["Spells"][t]
                    name.char_saves["Spells"] = class_saves["Spells"][t]
    return name


def thief_adjustment(name):
    if name.char_race == "Dwarf":
        name.char_race_abilities["Thief"]["Pick Pockets"] = "0%"
        name.char_race_abilities["Thief"]["Open Locks"] = "+10%"
        name.char_race_abilities["Thief"]["Find/Remove Traps"] = "+15%"
        name.char_race_abilities["Thief"]["Move Silent"] = "0%"
        name.char_race_abilities["Thief"]["Hide In Shadows"] = "0%"
        name.char_race_abilities["Thief"]["Hear Noise"] = "0%"
        name.char_race_abilities["Thief"]["Climb Walls"] = "-10%"
        name.char_race_abilities["Thief"]["Read Languages"] = "-5%"
    elif name.char_race == "Elf":
        name.char_race_abilities["Thief"]["Pick Pockets"] = "+5%"
        name.char_race_abilities["Thief"]["Open Locks"] = "-5%"
        name.char_race_abilities["Thief"]["Find/Remove Traps"] = "0%"
        name.char_race_abilities["Thief"]["Move Silent"] = "+5%"
        name.char_race_abilities["Thief"]["Hide In Shadows"] = "+10%"
        name.char_race_abilities["Thief"]["Hear Noise"] = "+5%"
        name.char_race_abilities["Thief"]["Climb Walls"] = "0%"
        name.char_race_abilities["Thief"]["Read Languages"] = "0%"
    elif name.char_race == "Gnome":
        name.char_race_abilities["Thief"]["Pick Pockets"] = "0%"
        name.char_race_abilities["Thief"]["Open Locks"] = "+5%"
        name.char_race_abilities["Thief"]["Find/Remove Traps"] = "+10%"
        name.char_race_abilities["Thief"]["Move Silent"] = "+5%"
        name.char_race_abilities["Thief"]["Hide In Shadows"] = "+5%"
        name.char_race_abilities["Thief"]["Hear Noise"] = "+10%"
        name.char_race_abilities["Thief"]["Climb Walls"] = "-15%"
        name.char_race_abilities["Thief"]["Read Languages"] = "0%"
    elif name.char_race == "Half-Elf":
        name.char_race_abilities["Thief"]["Pick Pockets"] = "+10%"
        name.char_race_abilities["Thief"]["Open Locks"] = "0%"
        name.char_race_abilities["Thief"]["Find/Remove Traps"] = "0%"
        name.char_race_abilities["Thief"]["Move Silent"] = "0%"
        name.char_race_abilities["Thief"]["Hide In Shadows"] = "+5%"
        name.char_race_abilities["Thief"]["Hear Noise"] = "0%"
        name.char_race_abilities["Thief"]["Climb Walls"] = "0%"
        name.char_race_abilities["Thief"]["Read Languages"] = "0%"
    elif name.char_race == "Halfling":
        name.char_race_abilities["Thief"]["Pick Pockets"] = "+5%"
        name.char_race_abilities["Thief"]["Open Locks"] = "+5%"
        name.char_race_abilities["Thief"]["Find/Remove Traps"] = "+5%"
        name.char_race_abilities["Thief"]["Move Silent"] = "+10%"
        name.char_race_abilities["Thief"]["Hide In Shadows"] = "+15%"
        name.char_race_abilities["Thief"]["Hear Noise"] = "+5%"
        name.char_race_abilities["Thief"]["Climb Walls"] = "-15%"
        name.char_race_abilities["Thief"]["Read Languages"] = "-5%"
    elif name.char_race == "Half-Orc":
        name.char_race_abilities["Thief"]["Pick Pockets"] = "-5%"
        name.char_race_abilities["Thief"]["Open Locks"] = "+5%"
        name.char_race_abilities["Thief"]["Find/Remove Traps"] = "+5%"
        name.char_race_abilities["Thief"]["Move Silent"] = "0%"
        name.char_race_abilities["Thief"]["Hide In Shadows"] = "0%"
        name.char_race_abilities["Thief"]["Hear Noise"] = "+5%"
        name.char_race_abilities["Thief"]["Climb Walls"] = "+5%"
        name.char_race_abilities["Thief"]["Read Languages"] = "-10%"
    elif name.char_race == "Human":
        name.char_race_abilities["Thief"]["Pick Pockets"] = "0%"
        name.char_race_abilities["Thief"]["Open Locks"] = "0%"
        name.char_race_abilities["Thief"]["Find/Remove Traps"] = "0%"
        name.char_race_abilities["Thief"]["Move Silent"] = "0%"
        name.char_race_abilities["Thief"]["Hide In Shadows"] = "0%"
        name.char_race_abilities["Thief"]["Hear Noise"] = "0%"
        name.char_race_abilities["Thief"]["Climb Walls"] = "0%"
        name.char_race_abilities["Thief"]["Read Languages"] = "0%"
    return name