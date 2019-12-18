import random

def ability_roller(sides, qty):
    sides = sides+1
    qty = qty+1
    bests = []
    for i in range(1, qty):
        num = random.randrange(1, sides)
        #print(num)
        bests.append(num)
    bests.sort()
    result = bests[-1]+bests[-2]+bests[-3]

    print(result)
    return result

def soclass():
    result = random.randrange(1, 101)
    return result

def exceptional_strength():
    result = random.randrange(1, 101)
    return result

def normal(sides, qty):
    sides = sides+1
    qty = qty+1
    num = 0
    for i in range(1, qty):
        num += random.randrange(1, sides)

    return num


def HP(sides, qty, name, min):
    sides = sides+1
    qty = qty+1
    num = 0
    for i in range(1, qty):
        num += random.randrange(1, sides)
        if num < min:
            num = min
        if name.char_abilities["CON"] == 19:
            if num == 1:
                num = 2
    return num

def unearthed():
    method = False
    while not method:
        print("36 Cavalier\n",
              "35 Paladin\n",
              "1 Cleric\n",
              "11 Druid\n",
              "16 Fighter\n",
              "34 Barbarian\n",
              "22 Ranger\n",
              "27 Magic-user\n",
              "30 Illusionist\n",
              "25 Thief\n",
              "26 Assassin\n",
              "33 Monk\n")
        choice = input("Choose a class NUMBER:")
        if choice.isdigit():
            if str(choice) in ["36", "35", "1", "11", "16", "34", "22", "27", "30", "25", "26", "33"]:
                if choice == "36":
                    abilities = {"STR": ability_roller(6, 8),
                                 "INT": ability_roller(6, 6),
                                 "WIS": ability_roller(6, 4),
                                 "DEX": ability_roller(6, 7),
                                 "CON": ability_roller(6, 9),
                                 "CHA": ability_roller(6, 3),
                                 "CMS": ability_roller(6, 5),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "35":
                    abilities = {"STR": ability_roller(6, 7),
                                 "INT": ability_roller(6, 5),
                                 "WIS": ability_roller(6, 8),
                                 "DEX": ability_roller(6, 3),
                                 "CON": ability_roller(6, 6),
                                 "CHA": ability_roller(6, 9),
                                 "CMS": ability_roller(6, 4),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "1":
                    abilities = {"STR": ability_roller(6, 7),
                                 "INT": ability_roller(6, 4),
                                 "WIS": ability_roller(6, 9),
                                 "DEX": ability_roller(6, 5),
                                 "CON": ability_roller(6, 8),
                                 "CHA": ability_roller(6, 6),
                                 "CMS": ability_roller(6, 3),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "11":
                    abilities = {"STR": ability_roller(6, 7),
                                 "INT": ability_roller(6, 4),
                                 "WIS": ability_roller(6, 8),
                                 "DEX": ability_roller(6, 5),
                                 "CON": ability_roller(6, 6),
                                 "CHA": ability_roller(6, 9),
                                 "CMS": ability_roller(6, 3),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "16" or choice == "34":
                    abilities = {"STR": ability_roller(6, 9),
                                 "INT": ability_roller(6, 3),
                                 "WIS": ability_roller(6, 5),
                                 "DEX": ability_roller(6, 7),
                                 "CON": ability_roller(6, 8),
                                 "CHA": ability_roller(6, 6),
                                 "CMS": ability_roller(6, 4),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "22":
                    abilities = {"STR": ability_roller(6, 7),
                                 "INT": ability_roller(6, 6),
                                 "WIS": ability_roller(6, 8),
                                 "DEX": ability_roller(6, 5),
                                 "CON": ability_roller(6, 9),
                                 "CHA": ability_roller(6, 4),
                                 "CMS": ability_roller(6, 3),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "27":
                    abilities = {"STR": ability_roller(6, 4),
                                 "INT": ability_roller(6, 9),
                                 "WIS": ability_roller(6, 7),
                                 "DEX": ability_roller(6, 8),
                                 "CON": ability_roller(6, 6),
                                 "CHA": ability_roller(6, 5),
                                 "CMS": ability_roller(6, 3),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "30":
                    abilities = {"STR": ability_roller(6, 3),
                                 "INT": ability_roller(6, 8),
                                 "WIS": ability_roller(6, 7),
                                 "DEX": ability_roller(6, 9),
                                 "CON": ability_roller(6, 5),
                                 "CHA": ability_roller(6, 6),
                                 "CMS": ability_roller(6, 4),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "25":
                    abilities = {"STR": ability_roller(6, 6),
                                 "INT": ability_roller(6, 5),
                                 "WIS": ability_roller(6, 3),
                                 "DEX": ability_roller(6, 9),
                                 "CON": ability_roller(6, 7),
                                 "CHA": ability_roller(6, 4),
                                 "CMS": ability_roller(6, 8),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "26":
                    abilities = {"STR": ability_roller(6, 6),
                                 "INT": ability_roller(6, 7),
                                 "WIS": ability_roller(6, 4),
                                 "DEX": ability_roller(6, 9),
                                 "CON": ability_roller(6, 8),
                                 "CHA": ability_roller(6, 3),
                                 "CMS": ability_roller(6, 5),
                                 "EX_STR": False}
                    return abilities, choice

                elif choice == "33":
                    abilities = {"STR": ability_roller(6, 7),
                                 "INT": ability_roller(6, 5),
                                 "WIS": ability_roller(6, 9),
                                 "DEX": ability_roller(6, 8),
                                 "CON": ability_roller(6, 6),
                                 "CHA": ability_roller(6, 4),
                                 "CMS": ability_roller(6, 3),
                                 "EX_STR": False}
                    return abilities, choice

                else:
                    method = False
            else:
                method = False
        else:
            method = False
