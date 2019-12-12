import dice

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
                        "IllusionistAssassin"
                        ],
                "MMC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin"
                        ],
                "UMC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin"],
                "LUC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin"],
                "MUC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin"],
                "UUC": ["Monk", "Thief", "Assassin", "Barbarian", "Fighter", "FighterThief", "FighterAssassin",
                        "Druid", "Ranger", "DruidRanger", "DruidFighter", "DruidThief",
                        "Cleric", "MagicUser", "Illusionist", "ClericMagicUser", "ClericFighterMagicUser",
                        "ClericRanger", "ClericThief", "ClericAssassin", "ClericIllusionist", "ClericMagicUserThief",
                        "DruidMagicUser", "FighterMagicUser", "FighterIllusionist", "FighterMagicUserThief",
                        "MagicUserThief", "RangerMagicUser", "MagicUserThief", "MagicUserAssassin", "IllusionistThief",
                        "IllusionistAssassin", "Paladin", "Cavalier", "UAPaladin"]}

soclass_definition = {"LLC": "Lower Lower Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian",
                      "MLC": "Middle Lower Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter",
                      "ULC": "Upper Lower Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid",
                      "LMC": "Lower Middle Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric",
                      "MMC": "Middle Middle Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User",
                      "UMC": "Upper Middle Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User",
                      "LUC": "Lower Upper Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, Paladin, UAPaladin, Cavalier",
                      "MUC": "Middle Upper Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, Paladin, UAPaladin, Cavalier",
                      "UUC": "Upper Upper Class:\n"
                             "You can be: Monk, Thief, Assassin, Barbarian, Fighter, Ranger, Druid, Cleric\n"
                             "            Illusionist, Magic-User, Paladin, UAPaladin, Cavalier"}

def social_class(name):
    global soclasslimit
    print("Roll social class or ignore it?")
    choice = input("Y to roll, N to ignore.")
    if str(choice).upper() != "Y".upper():
        print("You've chosen no.")
        soclass = "MUC"
    else:
        classroll = dice.soclass()
        print("You rolled: ", str(classroll), "for social class")
        if int(classroll) in range(1, 5):
            name.soclass = "LLC"
        elif int(classroll) in range(5, 11):
            name.soclass = "MLC"
        elif int(classroll) in range(11, 21):
            name.soclass = "ULC"
        elif int(classroll) in range(22, 36):
            name.soclass = "LMC"
        elif int(classroll) in range(36, 56):
            name.soclass = "MMC"
        elif int(classroll) in range(57, 88):
            name.soclass = "UMC"
        elif int(classroll) in range(88, 97):
            name.soclass = "LUC"
        elif int(classroll) in range(98, 100):
            name.soclass = "MUC"
        elif int(classroll) in range(100, 101):
            name.soclass = "UUC"
        name.soclass_limit = soclasslimit[name.soclass]
        print("You are:", name.social_class, soclass_definition[name.soclass])
    return name