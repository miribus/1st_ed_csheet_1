import dice, os, char_classes, char_classes_gui

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

soclasslimit = char_classes_gui.soclasslimit
soclass_definition = {"LLC": "Lower Lower Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, UAPaladin (0L), Cavalier (0L)",
                      "MLC": "Middle Lower Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, UAPaladin (0L), Cavalier (0L)",
                      "ULC": "Upper Lower Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, UAPaladin (0L), Cavalier (0L)",
                      "LMC": "Lower Middle Class:\n"
                              "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, UAPaladin (0L), Cavalier (0L)",
                      "MMC": "Middle Middle Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, UAPaladin (0L), Cavalier (0L), Paladin (PHB)",
                      "UMC": "Upper Middle Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, Paladin(PHB), UAPaladin, Cavalier",
                      "LUC": "Lower Upper Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, Paladin(PHB), UAPaladin, Cavalier",
                      "MUC": "Middle Upper Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, Paladin(PHB), UAPaladin, Cavalier",
                      "UUC": "Upper Upper Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, Paladin(PHB), UAPaladin, Cavalier"}

def social_class(name, choice, soclass):
    global soclasslimit
    #print("Roll social class or ignore it?")
    #choice = input("Y to roll, N to ignore.")
    #clear_screen()
    if str(choice).upper() != "Y".upper():
        #print("You've chosen no")
        name.social_class = "MUC"
    else:
        classroll = dice.soclass()
        if name.char_name == "Wreck":
            classroll = 100
        if name.self_roll:
            possible = [str(n) for n in range(1, 101)]
            possible.append("00")
            #classroll = 9999
            #while str(classroll) not in possible:
            #    classroll = input("What is your social class roll?")
            classroll = soclass
            if classroll == "00":
                classroll = 100
        print("You rolled: ", str(classroll), "for social class")
        if int(classroll) in range(1, 5):
            name.social_class = "LLC"
        elif int(classroll) in range(5, 11):
            name.social_class = "MLC"
        elif int(classroll) in range(11, 21):
            name.social_class = "ULC"
        elif int(classroll) in range(21, 36):
            name.social_class = "LMC"
        elif int(classroll) in range(36, 56):
            name.social_class = "MMC"
        elif int(classroll) in range(56, 88):
            name.social_class = "UMC"
        elif int(classroll) in range(88, 97):
            name.social_class = "LUC"
        elif int(classroll) in range(97, 100):
            name.social_class = "MUC"
        elif int(classroll) in range(100, 101):
            name.social_class = "UUC"
    name.soclass_limit = soclasslimit[name.social_class]
    print("You are:", name.social_class, soclass_definition[name.social_class])
    return name



'''
soclasslimit = {"LLC": ["Monk", "Thief", "Assassin", "Barbarian"],
                "MLC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin"],
                "ULC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief"],
                "LMC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "ClericFighter"
                        ],
                "MMC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "ClericFighter"
                        ],
                "UMC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin", "ClericFighter"],
                "LUC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin", "ClericFighter"],
                "MUC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin", "ClericFighter"],
                "UUC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin", "ClericFighter"]}
'''