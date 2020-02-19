import dice

def age(name):
    if name.self_roll:
        if len(str(name.char_age)) > 0:
            possible = [str(n) for n in range(1, 1601)]
            age = "00"
            while str(age) not in possible:
                age = input("What is your age roll?")
            age = int(age)
    if "Dwarf" in name.char_race:
        if name.self_roll:
            name.char_age = age
        else:
            for c in name.char_class:
                ages = []
                if "Cleric" in str(c) or "Druid" in str(c):
                    ages.append(250 + dice.normal(20, 2))
                elif "Fighter" in str(c) or "Paladin" in str(c) or "Ranger" in str(c):
                    ages.append(40 + dice.normal(4, 5))
                elif "Thief" in str(c) or "Assassin" in str(c):
                    ages.append(75 + dice.normal(6, 3))
            ages.sort()
            name.char_age = str(ages[-1])
        if int(name.char_age) in range(35, 51) or int(name.char_age) < 35:
            name.char_age_desc = "Young Adult"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            if int(name.char_age) < 35:
                name.char_age = 35
        elif int(name.char_age) in range(51, 151):
            name.char_age_desc = "Mature"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(151, 251):
            name.char_age_desc = "Middle Aged"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
        elif int(name.char_age) in range(251, 351):
            name.char_age_desc = "Old"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(351, 451) or int(name.char_age) > 450:
            name.char_age_desc = "Venerable"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
            name.char_abilities["STR"] -= 1
            name.char_abilities["DEX"] -= 1
            name.char_abilities["CON"] -= 1
            name.char_abilities["INT"] += 1
            name.char_abilities["WIS"] += 1
            if int(name.char_age) > 450:
                name.char_age = 450

    elif "Elf" in name.char_race:
        if name.self_roll:
            name.char_age = age
        else:
            for c in name.char_class:
                ages = []
                if "Cleric" in str(c) or "Druid" in str(c) or "Cavalier" in str(c):
                    ages.append(500 + dice.normal(10, 10))
                elif "Fighter" in str(c) or "Paladin" in str(c) or "Ranger" in str(c):
                    ages.append(130 + dice.normal(6, 5))
                elif "MagicUser" in str(c) or "Illusionist" in str(c):
                    ages.append(150 + dice.normal(6, 5))
                elif "Thief" in str(c) or "Assassin" in str(c):
                    ages.append(100 + dice.normal(6, 5))
            ages.sort()
            name.char_age = str(ages[-1])
        if int(name.char_age) in range(100, 176) or int(name.char_age) < 100:
            name.char_age_desc = "Young Adult"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            if int(name.char_age) < 100:
                name.char_age = 100
        elif int(name.char_age) in range(177, 551):
            name.char_age_desc = "Mature"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(551, 876):
            name.char_age_desc = "Middle Aged"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
        elif int(name.char_age) in range(876, 1201):
            name.char_age_desc = "Old"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(1201, 1601) or int(name.char_age) > 1600:
            name.char_age_desc = "Venerable"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
            name.char_abilities["STR"] -= 1
            name.char_abilities["DEX"] -= 1
            name.char_abilities["CON"] -= 1
            name.char_abilities["INT"] += 1
            name.char_abilities["WIS"] += 1
            if int(name.char_age) > 1600:
                name.char_age = 1600
    elif "Gnome" in name.char_race:
        if name.self_roll:
            name.char_age = age
        else:
            for c in name.char_class:
                ages = []
                if "Cleric" in str(c) or "Druid" in str(c):
                    ages.append(300 + dice.normal(12, 3))
                elif "Fighter" in str(c) or "Paladin" in str(c) or "Ranger" in str(c):
                    ages.append(60 + dice.normal(4, 5))
                elif "MagicUser" in str(c) or "Illusionist" in str(c):
                    ages.append(100 + dice.normal(12, 2))
                elif "Thief" in str(c) or "Assassin" in str(c):
                    ages.append(80 + dice.normal(4, 5))
            ages.sort()
            name.char_age = str(ages[-1])
        if int(name.char_age) in range(50, 91) or name.char_age > 50:
            name.char_age_desc = "Young Adult"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            if int(name.char_age) < 50:
                name.char_age = 50
        elif int(name.char_age) in range(91, 301):
            name.char_age_desc = "Mature"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(301, 451):
            name.char_age_desc = "Middle Aged"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
        elif int(name.char_age) in range(451, 601):
            name.char_age_desc = "Old"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(601, 751) or int(name.char_age) > 750:
            name.char_age_desc = "Venerable"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
            name.char_abilities["STR"] -= 1
            name.char_abilities["DEX"] -= 1
            name.char_abilities["CON"] -= 1
            name.char_abilities["INT"] += 1
            name.char_abilities["WIS"] += 1
            if int(name.char_age) > 750:
                name.char_age = 750
    elif name.char_race == "Half-Elf":
        if name.self_roll:
            name.char_age = age
        else:
            for c in name.char_class:
                ages = []
                if "Cleric" in str(c) or "Druid" in str(c) or "Cavalier" in str(c):
                    ages.append(40 + dice.normal(4, 2))
                elif "Fighter" in str(c) or "Paladin" in str(c) or "Ranger" in str(c):
                    ages.append(22 + dice.normal(4, 3))
                elif "MagicUser" in str(c) or "Illusionist" in str(c):
                    ages.append(30 + dice.normal(8, 2))
                elif "Thief" in str(c) or "Assassin" in str(c):
                    ages.append(22 + dice.normal(8, 3))
            ages.sort()
            name.char_age = str(ages[-1])
        if int(name.char_age) in range(25, 41) or name.char_age < 25:
            name.char_age_desc = "Young Adult"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            if int(name.char_age) < 25:
                name.char_age = 25
        elif int(name.char_age) in range(41, 100):
            name.char_age_desc = "Mature"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(101, 175):
            name.char_age_desc = "Middle Aged"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
        elif int(name.char_age) in range(176, 251):
            name.char_age_desc = "Old"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(251, 325) or int(name.char_age) > 324:
            name.char_age_desc = "Venerable"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
            name.char_abilities["STR"] -= 1
            name.char_abilities["DEX"] -= 1
            name.char_abilities["CON"] -= 1
            name.char_abilities["INT"] += 1
            name.char_abilities["WIS"] += 1
            if int(name.char_age) > 324:
                name.char_age = 324
    elif name.char_race == "Halfling":
        if name.self_roll:
            name.char_age = age
        else:
            for c in name.char_class:
                ages = []
                if "Cleric" in str(c) or "Druid" in str(c):
                    ages.append(30 + dice.normal(4, 3))
                elif "Fighter" in str(c) or "Paladin" in str(c) or "Ranger" in str(c):
                    ages.append(20 + dice.normal(4, 3))
                elif "Thief" in str(c) or "Assassin" in str(c):
                    ages.append(40 + dice.normal(4, 2))
            ages.sort()
            name.char_age = str(ages[-1])
        if int(name.char_age) in range(22, 34) or name.char_age < 22:
            name.char_age_desc = "Young Adult"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            if int(name.char_age) < 22:
                name.char_age = 22
        elif int(name.char_age) in range(34, 69):
            name.char_age_desc = "Mature"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(69, 102):
            name.char_age_desc = "Middle Aged"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
        elif int(name.char_age) in range(102, 145):
            name.char_age_desc = "Old"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(146, 200) or int(name.char_age) > 199:
            name.char_age_desc = "Venerable"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
            name.char_abilities["STR"] -= 1
            name.char_abilities["DEX"] -= 1
            name.char_abilities["CON"] -= 1
            name.char_abilities["INT"] += 1
            name.char_abilities["WIS"] += 1
            if int(name.char_age) > 199:
                name.char_age = 199
    elif name.char_race == "Half-Orc":
        if name.self_roll:
            name.char_age = age
        else:
            for c in name.char_class:
                ages = []
                if "Cleric" in str(c) or "Druid" in str(c):
                    ages.append(20 + dice.normal(4, 1))
                elif "Fighter" in str(c) or "Paladin" in str(c) or "Ranger" in str(c):
                    ages.append(13 + dice.normal(4, 1))
                elif "Thief" in str(c) or "Assassin" in str(c):
                    ages.append(20 + dice.normal(4, 2))
            ages.sort()
            name.char_age = str(ages[-1])
        if int(name.char_age) in range(12, 16) or name.char_age < 12:
            name.char_age_desc = "Young Adult"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            if int(name.char_age) < 12:
                name.char_age = 12
        elif int(name.char_age) in range(16, 31):
            name.char_age_desc = "Mature"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(31, 46):
            name.char_age_desc = "Middle Aged"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
        elif int(name.char_age) in range(46, 61):
            name.char_age_desc = "Old"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(61, 81) or int(name.char_age) > 80:
            name.char_age_desc = "Venerable"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
            name.char_abilities["STR"] -= 1
            name.char_abilities["DEX"] -= 1
            name.char_abilities["CON"] -= 1
            name.char_abilities["INT"] += 1
            name.char_abilities["WIS"] += 1
            if int(name.char_age) > 80:
                name.char_age = 80
    elif name.char_race == "Human":
        if name.self_roll:
            name.char_age = age
        else:
            for c in name.char_class:
                ages = []
                if "Cleric" in str(c) or "Druid" in str(c):
                    ages.append(18 + dice.normal(4, 1))
                elif "Fighter" in str(c):
                    ages.append(15 + dice.normal(4, 1))
                elif "Paladin" in str(c) or "UAPaladin" in str(c) or "Cavalier" in str(c):
                    ages.append(17 + dice.normal(4, 1))
                elif "Ranger" in str(c):
                    ages.append(20 + dice.normal(4, 1))
                elif "MagicUser" in str(c):
                    ages.append(24 + dice.normal(8, 2))
                elif "Illusionist" in str(c):
                    ages.append(30 + dice.normal(6, 1))
                elif "Thief" in str(c):
                    ages.append(18 + dice.normal(4, 1))
                elif "Assassin" in str(c):
                    ages.append(20 + dice.normal(4, 1))
                elif "Barbarian" in str(c):
                    ages.append(14 + dice.normal(4, 1))
                elif "Monk" in str(c):
                    ages.append(21 + dice.normal(4, 1))
            ages.sort()
            name.char_age = str(ages[-1])
        if int(name.char_age) in range(14, 21) or name.char_age < 14:
            print("This one")
            name.char_age_desc = "Young Adult"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            if int(name.char_age) < 14:
                name.char_age = 14
        elif int(name.char_age) in range(21, 41):
            name.char_age_desc = "Mature"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(41, 61):
            name.char_age_desc = "Middle Aged"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
        elif int(name.char_age) in range(61, 91):
            name.char_age_desc = "Old"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
        elif int(name.char_age) in range(91, 121) or int(name.char_age) > 120:
            name.char_age_desc = "Venerable"
            name.char_abilities["WIS"] -= 1
            name.char_abilities["CON"] += 1
            name.char_abilities["STR"] += 1
            name.char_abilities["WIS"] += 1
            if "EX_STR" in name.char_abilities:
                name.char_abilities["EX_STR"] = round(name.char_abilities["EX_STR"] / 2)
            else:
                name.char_abilities["STR"] -= 1
            name.char_abilities["STR"] -= 2
            name.char_abilities["DEX"] -= 2
            name.char_abilities["CON"] -= 1
            name.char_abilities["WIS"] += 1
            name.char_abilities["STR"] -= 1
            name.char_abilities["DEX"] -= 1
            name.char_abilities["CON"] -= 1
            name.char_abilities["INT"] += 1
            name.char_abilities["WIS"] += 1
            if int(name.char_age) > 120:
                name.char_age = 120
    return name