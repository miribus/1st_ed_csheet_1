def define_abilities(rolls, classlist):
    define_abilities = {}
    if rolls["STR"] in range(3, 4):
        define_abilities["STR"]["HIT"] = "-3"
        define_abilities["STR"]["DMG"] = "-1"
        define_abilities["STR"]["WEIGHT"] = "-350"
        define_abilities["STR"]["OPEN_DOOR"] = "1"
        define_abilities["STR"]["BEND_BARS"] = "0"
    elif rolls["STR"] in range(4, 6):
        define_abilities["STR"]["HIT"] = "-2"
        define_abilities["STR"]["DMG"] = "-1"
        define_abilities["STR"]["WEIGHT"] = "-250"
        define_abilities["STR"]["OPEN_DOOR"] = "1"
        define_abilities["STR"]["BEND_BARS"] = "0"
    elif rolls["STR"] in range(6, 8):
        define_abilities["STR"]["HIT"] = "-1"
        define_abilities["STR"]["DMG"] = "0"
        define_abilities["STR"]["WEIGHT"] = "-150"
        define_abilities["STR"]["OPEN_DOOR"] = "1"
        define_abilities["STR"]["BEND_BARS"] = "0"
    elif rolls["STR"] in range(8, 10):
        define_abilities["STR"]["HIT"] = "0"
        define_abilities["STR"]["DMG"] = "0"
        define_abilities["STR"]["WEIGHT"] = "0"
        define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        define_abilities["STR"]["BEND_BARS"] = "1%"
    elif rolls["STR"] in range(10, 12):
        define_abilities["STR"]["HIT"] = "0"
        define_abilities["STR"]["DMG"] = "0"
        define_abilities["STR"]["WEIGHT"] = "0"
        define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        define_abilities["STR"]["BEND_BARS"] = "2%"
    elif rolls["STR"] in range(12, 14):
        define_abilities["STR"]["HIT"] = "0"
        define_abilities["STR"]["DMG"] = "0"
        define_abilities["STR"]["WEIGHT"] = "+100"
        define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        define_abilities["STR"]["BEND_BARS"] = "4%"
    elif rolls["STR"] in range(14, 16):
        define_abilities["STR"]["HIT"] = "0"
        define_abilities["STR"]["DMG"] = "0"
        define_abilities["STR"]["WEIGHT"] = "+200"
        define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        define_abilities["STR"]["BEND_BARS"] = "7%"
    elif rolls["STR"] in range(16, 17):
        define_abilities["STR"]["HIT"] = "0"
        define_abilities["STR"]["DMG"] = "+1"
        define_abilities["STR"]["WEIGHT"] = "+350"
        define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        define_abilities["STR"]["BEND_BARS"] = "10%"
    elif rolls["STR"] in range(17, 18):
        define_abilities["STR"]["HIT"] = "+1"
        define_abilities["STR"]["DMG"] = "+1"
        define_abilities["STR"]["WEIGHT"] = "+500"
        define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        define_abilities["STR"]["BEND_BARS"] = "13%"
    elif rolls["STR"] in range(18, 19) and not rolls['EX_STR']:
        define_abilities["STR"]["HIT"] = "+1"
        define_abilities["STR"]["DMG"] = "+2"
        define_abilities["STR"]["WEIGHT"] = "+750"
        define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        define_abilities["STR"]["BEND_BARS"] = "16%"
    elif rolls["STR"] in range(18, 19) and rolls['EX_STR'] in range(1, 51):
        define_abilities["STR"]["HIT"] = "+1"
        define_abilities["STR"]["DMG"] = "+3"
        define_abilities["STR"]["WEIGHT"] = "+1000"
        define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        define_abilities["STR"]["BEND_BARS"] = "20%"
    elif rolls["STR"] in range(18, 19) and rolls['EX_STR'] in range(52, 76):
        define_abilities["STR"]["HIT"] = "+2"
        define_abilities["STR"]["DMG"] = "+3"
        define_abilities["STR"]["WEIGHT"] = "+1250"
        define_abilities["STR"]["OPEN_DOOR"] = "1-4"
        define_abilities["STR"]["BEND_BARS"] = "25%"
    elif rolls["STR"] in range(18, 19) and rolls['EX_STR'] in range(76, 91):
        define_abilities["STR"]["HIT"] = "+2"
        define_abilities["STR"]["DMG"] = "+4"
        define_abilities["STR"]["WEIGHT"] = "+1500"
        define_abilities["STR"]["OPEN_DOOR"] = "1-4"
        define_abilities["STR"]["BEND_BARS"] = "30%"
    elif rolls["STR"] in range(18, 19) and rolls['EX_STR'] in range(91, 100):
        define_abilities["STR"]["HIT"] = "+2"
        define_abilities["STR"]["DMG"] = "+5"
        define_abilities["STR"]["WEIGHT"] = "+2000"
        define_abilities["STR"]["OPEN_DOOR"] = "1-4 (Locked/Barred: 1)"
        define_abilities["STR"]["BEND_BARS"] = "35%"
    elif rolls["STR"] in range(18, 19) and rolls['EX_STR'] in range(91, 100):
        define_abilities["STR"]["HIT"] = "+3"
        define_abilities["STR"]["DMG"] = "+6"
        define_abilities["STR"]["WEIGHT"] = "+3000"
        define_abilities["STR"]["OPEN_DOOR"] = "1-5 (Locked/Barred: 2)"
        define_abilities["STR"]["BEND_BARS"] = "40%"

    if rolls["INT"] in range(3, 8):
        define_abilities["INT"]["LANG"] = "No extras."
    elif rolls["INT"] == 8:
        define_abilities["INT"]["LANG"] = "1 Additional Language Possible."
    elif rolls["INT"] == 9:
        define_abilities["INT"]["LANG"] = "1 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "35% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "4"
        define_abilities["INT"]["Max Spells/Level"] = "6"
    elif rolls["INT"] in range(10, 12):
        define_abilities["INT"]["LANG"] = "2 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "45% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "5"
        define_abilities["INT"]["Max Spells/Level"] = "7"
    elif rolls["INT"] == 12:
        define_abilities["INT"]["LANG"] = "3 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "45% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "5"
        define_abilities["INT"]["Max Spells/Level"] = "7"
    elif rolls["INT"] == 13:
        define_abilities["INT"]["LANG"] = "3 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "55% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "6"
        define_abilities["INT"]["Max Spells/Level"] = "9"
    elif rolls["INT"] == 14:
        define_abilities["INT"]["LANG"] = "4 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "55% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "6"
        define_abilities["INT"]["Max Spells/Level"] = "9"
    elif rolls["INT"] == 15:
        define_abilities["INT"]["LANG"] = "4 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "65% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "7"
        define_abilities["INT"]["Max Spells/Level"] = "11"
    elif rolls["INT"] == 16:
        define_abilities["INT"]["LANG"] = "5 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "65% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "7"
        define_abilities["INT"]["Max Spells/Level"] = "11"
    elif rolls["INT"] == 17:
        define_abilities["INT"]["LANG"] = "6 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "75% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "8"
        define_abilities["INT"]["Max Spells/Level"] = "14"
    elif rolls["INT"] == 18:
        define_abilities["INT"]["LANG"] = "7 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "85% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "9"
        define_abilities["INT"]["Max Spells/Level"] = "18"
    elif rolls["INT"] == 19:
        define_abilities["INT"]["LANG"] = "7 Additional Language Possible."
        define_abilities["INT"]["Know Spell"] = "95% Chance to Know Spell"
        define_abilities["INT"]["Min Spells/Level"] = "10"
        define_abilities["INT"]["Max Spells/Level"] = "All"

    if rolls["WIS"] == 3:
        define_abilities["WIS"]["Magical Save"] = "-3"
    elif rolls["WIS"] == 4:
        define_abilities["WIS"]["Magical Save"] = "-2"
    elif rolls["WIS"] in range(5, 8):
        define_abilities["WIS"]["Magical Save"] = "-1"
    elif rolls["WIS"] == 8:
        define_abilities["WIS"]["Magical Save"] = "0"
    elif rolls["WIS"] == 9:
        define_abilities["WIS"]["Magical Save"] = "0"
        define_abilities["WIS"]["Spell Bonus"] = "0"
        define_abilities["WIS"]["Spell Failure"] = "20%"
    elif rolls["WIS"] == 10:
        define_abilities["WIS"]["Magical Save"] = "0"
        define_abilities["WIS"]["Spell Bonus"] = "0"
        define_abilities["WIS"]["Spell Failure"] = "15%"
    elif rolls["WIS"] == 11:
        define_abilities["WIS"]["Magical Save"] = "0"
        define_abilities["WIS"]["Spell Bonus"] = "0"
        define_abilities["WIS"]["Spell Failure"] = "10%"
    elif rolls["WIS"] == 12:
        define_abilities["WIS"]["Magical Save"] = "0"
        define_abilities["WIS"]["Spell Bonus"] = "0"
        define_abilities["WIS"]["Spell Failure"] = "5%"
    elif rolls["WIS"] == 13:
        define_abilities["WIS"]["Magical Save"] = "0"
        define_abilities["WIS"]["Spell Bonus"] = "1:1L"
        define_abilities["WIS"]["Spell Failure"] = "0%"
    elif rolls["WIS"] == 14:
        define_abilities["WIS"]["Magical Save"] = "0"
        define_abilities["WIS"]["Spell Bonus"] = "2:1L"
        define_abilities["WIS"]["Spell Failure"] = "0%"
    elif rolls["WIS"] == 15:
        define_abilities["WIS"]["Magical Save"] = "+1"
        define_abilities["WIS"]["Spell Bonus"] = "2:1L, 1:2L"
        define_abilities["WIS"]["Spell Failure"] = "0%"
    elif rolls["WIS"] == 16:
        define_abilities["WIS"]["Magical Save"] = "+2"
        define_abilities["WIS"]["Spell Bonus"] = "2:1L, 2:2L"
        define_abilities["WIS"]["Spell Failure"] = "0%"
    elif rolls["WIS"] == 17:
        define_abilities["WIS"]["Magical Save"] = "+3"
        define_abilities["WIS"]["Spell Bonus"] = "2:1L, 2:2L, 1:3L"
        define_abilities["WIS"]["Spell Failure"] = "0%"
    elif rolls["WIS"] == 18:
        define_abilities["WIS"]["Magical Save"] = "+4"
        define_abilities["WIS"]["Spell Bonus"] = "2:1L, 2:2L, 1:3L, 1:4L"
        define_abilities["WIS"]["Spell Failure"] = "0%"

    if rolls["DEX"] == 3:
        define_abilities["DEX"]["Reaction"] = "-3"
        define_abilities["DEX"]["Defensive"] = "+4"
    elif rolls["DEX"] == 4:
        define_abilities["DEX"]["Reaction"] = "-2"
        define_abilities["DEX"]["Defensive"] = "+3"
    elif rolls["DEX"] == 5:
        define_abilities["DEX"]["Reaction"] = "-1"
        define_abilities["DEX"]["Defensive"] = "+2"
    elif rolls["DEX"] == 5:
        define_abilities["DEX"]["Reaction"] = "0"
        define_abilities["DEX"]["Defensive"] = "+1"
    elif rolls["DEX"] in range(7,15):
        define_abilities["DEX"]["Reaction"] = "0"
        define_abilities["DEX"]["Defensive"] = "0"
    elif rolls["DEX"] == 15:
        define_abilities["DEX"]["Reaction"] = "0"
        define_abilities["DEX"]["Defensive"] = "-1"
    elif rolls["DEX"] == 16:
        define_abilities["DEX"]["Reaction"] = "+1"
        define_abilities["DEX"]["Defensive"] = "-2"
    elif rolls["DEX"] == 17:
        define_abilities["DEX"]["Reaction"] = "+2"
        define_abilities["DEX"]["Defensive"] = "-3"
    elif rolls["DEX"] == 18:
        define_abilities["DEX"]["Reaction"] = "+3"
        define_abilities["DEX"]["Defensive"] = "-4"

    if rolls["CON"] == 3:
        define_abilities["CON"]["HP Adj"] = "-2"
        define_abilities["CON"]["System Shock"] = "35%"
        define_abilities["CON"]["Ressurection Survival"] = "40%"
    elif rolls["CON"] == 4:
        define_abilities["CON"]["HP Adj"] = "-1"
        define_abilities["CON"]["System Shock"] = "40%"
        define_abilities["CON"]["Ressurection Survival"] = "45%"
    elif rolls["CON"] == 5:
        define_abilities["CON"]["HP Adj"] = "-1"
        define_abilities["CON"]["System Shock"] = "45%"
        define_abilities["CON"]["Ressurection Survival"] = "50%"
    elif rolls["CON"] == 6:
        define_abilities["CON"]["HP Adj"] = "-1"
        define_abilities["CON"]["System Shock"] = "50%"
        define_abilities["CON"]["Ressurection Survival"] = "55%"
    elif rolls["CON"] == 7:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "55%"
        define_abilities["CON"]["Ressurection Survival"] = "60%"
    elif rolls["CON"] == 8:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "60%"
        define_abilities["CON"]["Ressurection Survival"] = "65%"
    elif rolls["CON"] == 9:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "65%"
        define_abilities["CON"]["Ressurection Survival"] = "70%"
    elif rolls["CON"] == 10:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "70%"
        define_abilities["CON"]["Ressurection Survival"] = "75%"
    elif rolls["CON"] == 11:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "75%"
        define_abilities["CON"]["Ressurection Survival"] = "80%"
    elif rolls["CON"] == 12:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "80%"
        define_abilities["CON"]["Ressurection Survival"] = "85%"
    elif rolls["CON"] == 13:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "85%"
        define_abilities["CON"]["Ressurection Survival"] = "90%"
    elif rolls["CON"] == 14:
        define_abilities["CON"]["HP Adj"] = "0"
        define_abilities["CON"]["System Shock"] = "88%"
        define_abilities["CON"]["Ressurection Survival"] = "92%"
    elif rolls["CON"] == 15:
        define_abilities["CON"]["HP Adj"] = "+1"
        define_abilities["CON"]["System Shock"] = "91%"
        define_abilities["CON"]["Ressurection Survival"] = "94%"
    elif rolls["CON"] == 16:
        define_abilities["CON"]["HP Adj"] = "+2"
        define_abilities["CON"]["System Shock"] = "95%"
        define_abilities["CON"]["Ressurection Survival"] = "96%"
    elif rolls["CON"] == 17:
        define_abilities["CON"]["HP Adj"] = "+2"
        fighters = ["Fighter", "Barbarian", "Cavalier", "Paladin", "UAPaladin", "Ranger"]
        for c in classlist:
            if str(c) in fighters:
                define_abilities["CON"]["HP Adj"] = "+3"
        define_abilities["CON"]["System Shock"] = "97%"
        define_abilities["CON"]["Ressurection Survival"] = "98%"
    elif rolls["CON"] == 18:
        define_abilities["CON"]["HP Adj"] = "+2"
        fighters = ["Fighter", "Barbarian", "Cavalier", "Paladin", "UAPaladin", "Ranger"]
        for c in classlist:
            if str(c) in fighters:
                define_abilities["CON"]["HP Adj"] = "+4"
        define_abilities["CON"]["System Shock"] = "99%"
        define_abilities["CON"]["Ressurection Survival"] = "100%"

    if rolls["CHA"] == 3:
        define_abilities["CHA"]["Henchmen"] = "1"
        define_abilities["CHA"]["Loyalty"] = "-30%"
        define_abilities["CHA"]["Reaction"] = "-25%"
    elif rolls["CHA"] == 4:
        define_abilities["CHA"]["Henchmen"] = "1"
        define_abilities["CHA"]["Loyalty"] = "-25%"
        define_abilities["CHA"]["Reaction"] = "-20%"
    elif rolls["CHA"] == 5:
        define_abilities["CHA"]["Henchmen"] = "2"
        define_abilities["CHA"]["Loyalty"] = "-20%"
        define_abilities["CHA"]["Reaction"] = "-15%"
    elif rolls["CHA"] == 6:
        define_abilities["CHA"]["Henchmen"] = "2"
        define_abilities["CHA"]["Loyalty"] = "-15%"
        define_abilities["CHA"]["Reaction"] = "-10%"
    elif rolls["CHA"] == 7:
        define_abilities["CHA"]["Henchmen"] = "3"
        define_abilities["CHA"]["Loyalty"] = "-10%"
        define_abilities["CHA"]["Reaction"] = "-5%"
    elif rolls["CHA"] == 8:
        define_abilities["CHA"]["Henchmen"] = "3"
        define_abilities["CHA"]["Loyalty"] = "-5%"
        define_abilities["CHA"]["Reaction"] = "0%"
    elif rolls["CHA"] in range(9, 12):
        define_abilities["CHA"]["Henchmen"] = "4"
        define_abilities["CHA"]["Loyalty"] = "0%"
        define_abilities["CHA"]["Reaction"] = "0%"
    elif rolls["CHA"] == 12:
        define_abilities["CHA"]["Henchmen"] = "5"
        define_abilities["CHA"]["Loyalty"] = "0%"
        define_abilities["CHA"]["Reaction"] = "0%"
    elif rolls["CHA"] == 13:
        define_abilities["CHA"]["Henchmen"] = "5"
        define_abilities["CHA"]["Loyalty"] = "0%"
        define_abilities["CHA"]["Reaction"] = "+5%"
    elif rolls["CHA"] == 14:
        define_abilities["CHA"]["Henchmen"] = "6"
        define_abilities["CHA"]["Loyalty"] = "+5%"
        define_abilities["CHA"]["Reaction"] = "+10%"
    elif rolls["CHA"] == 15:
        define_abilities["CHA"]["Henchmen"] = "7"
        define_abilities["CHA"]["Loyalty"] = "+15%"
        define_abilities["CHA"]["Reaction"] = "+15%"
    elif rolls["CHA"] == 16:
        define_abilities["CHA"]["Henchmen"] = "8"
        define_abilities["CHA"]["Loyalty"] = "+20%"
        define_abilities["CHA"]["Reaction"] = "+25%"
    elif rolls["CHA"] == 17:
        define_abilities["CHA"]["Henchmen"] = "10"
        define_abilities["CHA"]["Loyalty"] = "+30%"
        define_abilities["CHA"]["Reaction"] = "+30%"
    elif rolls["CHA"] == 18:
        define_abilities["CHA"]["Henchmen"] = "15"
        define_abilities["CHA"]["Loyalty"] = "+40%"
        define_abilities["CHA"]["Reaction"] = "+35%"

    if rolls["CMS"] in range(14, 18):
        fasc = round(rolls["CMS"] / 2)
        define_abilities["CMS"]["Fascinate"] = "Fascinate if Opponent's WIS < {}".format(str(fasc))
    elif rolls["CMS"] in range(18, 22):
        fasc = round(rolls["CMS"] / 3)
        fasc = rolls("CMS") - fasc
        define_abilities["CMS"]["Fascinate"] = "Fascinate if Opponent's WIS < {}".format(str(fasc))

    if "Thief" in classlist or "Assassin" in classlist:
        if rolls["DEX"] == 9:
            define_abilities["DEX"]["Pick Pockets"] = "-15%"
            define_abilities["DEX"]["Open Locks"] = "-10%"
            define_abilities["DEX"]["Find/Remove Traps"] = "-10%"
            define_abilities["DEX"]["Move Silent"] = "-20%"
            define_abilities["DEX"]["Hide In Shadows"] = "-10%"
        elif rolls["DEX"] == 10:
            define_abilities["DEX"]["Pick Pockets"] = "-10%"
            define_abilities["DEX"]["Open Locks"] = "-5%"
            define_abilities["DEX"]["Find/Remove Traps"] = "-10%"
            define_abilities["DEX"]["Move Silent"] = "-15%"
            define_abilities["DEX"]["Hide In Shadows"] = "-5%"
        elif rolls["DEX"] == 11:
            define_abilities["DEX"]["Pick Pockets"] = "-5%"
            define_abilities["DEX"]["Open Locks"] = "0%"
            define_abilities["DEX"]["Find/Remove Traps"] = "-5%"
            define_abilities["DEX"]["Move Silent"] = "-10%"
            define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif rolls["DEX"] == 12:
            define_abilities["DEX"]["Pick Pockets"] = "0%"
            define_abilities["DEX"]["Open Locks"] = "0%"
            define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            define_abilities["DEX"]["Move Silent"] = "-5%"
            define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif rolls["DEX"] in range(13, 16):
            define_abilities["DEX"]["Pick Pockets"] = "0%"
            define_abilities["DEX"]["Open Locks"] = "0%"
            define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            define_abilities["DEX"]["Move Silent"] = "0%"
            define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif rolls["DEX"] == 16:
            define_abilities["DEX"]["Pick Pockets"] = "0%"
            define_abilities["DEX"]["Open Locks"] = "+5%"
            define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            define_abilities["DEX"]["Move Silent"] = "0%"
            define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif rolls["DEX"] == 17:
            define_abilities["DEX"]["Pick Pockets"] = "+5%"
            define_abilities["DEX"]["Open Locks"] = "+10%"
            define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            define_abilities["DEX"]["Move Silent"] = "+5%"
            define_abilities["DEX"]["Hide In Shadows"] = "+5%"
        elif rolls["DEX"] == 18:
            define_abilities["DEX"]["Pick Pockets"] = "+10%"
            define_abilities["DEX"]["Open Locks"] = "+15%"
            define_abilities["DEX"]["Find/Remove Traps"] = "+5%"
            define_abilities["DEX"]["Move Silent"] = "+10%"
            define_abilities["DEX"]["Hide In Shadows"] = "+10%"
    return define_abilities