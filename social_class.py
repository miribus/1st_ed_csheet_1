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

def social_class():
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
            soclass = "LLC"
        elif int(classroll) in range(5, 11):
            soclass = "MLC"
        elif int(classroll) in range(11, 21):
            soclass = "ULC"
        elif int(classroll) in range(22, 36):
            soclass = "LMC"
        elif int(classroll) in range(36, 56):
            soclass = "MMC"
        elif int(classroll) in range(57, 88):
            soclass = "UMC"
        elif int(classroll) in range(88, 97):
            soclass = "LUC"
        elif int(classroll) in range(98, 100):
            soclass = "MUC"
        elif int(classroll) in range(100, 101):
            soclass = "UUC"

        print("You are:", soclass, "You can be the following:", soclasslimit[soclass])
    return soclass, soclasslimit[soclass]