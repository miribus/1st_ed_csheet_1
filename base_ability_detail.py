def define_abilities(name):
    fighters = ["Fighter", "Barbarian", "Cavalier", "Paladin", "UAPaladin", "Ranger"]
    if name.char_abilities["STR"] in range(3, 4):
        name.char_define_abilities["STR"]["HIT"] = "-3"
        name.char_define_abilities["STR"]["DMG"] = "-1"
        name.char_define_abilities["STR"]["WEIGHT"] = "-350"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1"
        name.char_define_abilities["STR"]["BEND_BARS"] = "0"
    elif name.char_abilities["STR"] in range(4, 6):
        name.char_define_abilities["STR"]["HIT"] = "-2"
        name.char_define_abilities["STR"]["DMG"] = "-1"
        name.char_define_abilities["STR"]["WEIGHT"] = "-250"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1"
        name.char_define_abilities["STR"]["BEND_BARS"] = "0"
    elif name.char_abilities["STR"] in range(6, 8):
        name.char_define_abilities["STR"]["HIT"] = "-1"
        name.char_define_abilities["STR"]["DMG"] = "0"
        name.char_define_abilities["STR"]["WEIGHT"] = "-150"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1"
        name.char_define_abilities["STR"]["BEND_BARS"] = "0"
    elif name.char_abilities["STR"] in range(8, 10):
        name.char_define_abilities["STR"]["HIT"] = "0"
        name.char_define_abilities["STR"]["DMG"] = "0"
        name.char_define_abilities["STR"]["WEIGHT"] = "0"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        name.char_define_abilities["STR"]["BEND_BARS"] = "1%"
    elif name.char_abilities["STR"] in range(10, 12):
        name.char_define_abilities["STR"]["HIT"] = "0"
        name.char_define_abilities["STR"]["DMG"] = "0"
        name.char_define_abilities["STR"]["WEIGHT"] = "0"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        name.char_define_abilities["STR"]["BEND_BARS"] = "2%"
    elif name.char_abilities["STR"] in range(12, 14):
        name.char_define_abilities["STR"]["HIT"] = "0"
        name.char_define_abilities["STR"]["DMG"] = "0"
        name.char_define_abilities["STR"]["WEIGHT"] = "+100"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        name.char_define_abilities["STR"]["BEND_BARS"] = "4%"
    elif name.char_abilities["STR"] in range(14, 16):
        name.char_define_abilities["STR"]["HIT"] = "0"
        name.char_define_abilities["STR"]["DMG"] = "0"
        name.char_define_abilities["STR"]["WEIGHT"] = "+200"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-2"
        name.char_define_abilities["STR"]["BEND_BARS"] = "7%"
    elif name.char_abilities["STR"] in range(16, 17):
        name.char_define_abilities["STR"]["HIT"] = "0"
        name.char_define_abilities["STR"]["DMG"] = "+1"
        name.char_define_abilities["STR"]["WEIGHT"] = "+350"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        name.char_define_abilities["STR"]["BEND_BARS"] = "10%"
    elif name.char_abilities["STR"] in range(17, 18):
        name.char_define_abilities["STR"]["HIT"] = "+1"
        name.char_define_abilities["STR"]["DMG"] = "+1"
        name.char_define_abilities["STR"]["WEIGHT"] = "+500"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        name.char_define_abilities["STR"]["BEND_BARS"] = "13%"
    elif name.char_abilities["STR"] in range(18, 19) and not name.char_abilities["EX_STR"]:
        name.char_define_abilities["STR"]["HIT"] = "+1"
        name.char_define_abilities["STR"]["DMG"] = "+2"
        name.char_define_abilities["STR"]["WEIGHT"] = "+750"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        name.char_define_abilities["STR"]["BEND_BARS"] = "16%"
    elif name.char_abilities["STR"] in range(18, 19) and name.char_abilities['EX_STR'] in range(1, 51):
        name.char_define_abilities["STR"]["HIT"] = "+1"
        name.char_define_abilities["STR"]["DMG"] = "+3"
        name.char_define_abilities["STR"]["WEIGHT"] = "+1000"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-3"
        name.char_define_abilities["STR"]["BEND_BARS"] = "20%"
    elif name.char_abilities["STR"] in range(18, 19) and name.char_abilities['EX_STR'] in range(52, 76):
        name.char_define_abilities["STR"]["HIT"] = "+2"
        name.char_define_abilities["STR"]["DMG"] = "+3"
        name.char_define_abilities["STR"]["WEIGHT"] = "+1250"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-4"
        name.char_define_abilities["STR"]["BEND_BARS"] = "25%"
    elif name.char_abilities["STR"] in range(18, 19) and name.char_abilities['EX_STR'] in range(76, 91):
        name.char_define_abilities["STR"]["HIT"] = "+2"
        name.char_define_abilities["STR"]["DMG"] = "+4"
        name.char_define_abilities["STR"]["WEIGHT"] = "+1500"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-4"
        name.char_define_abilities["STR"]["BEND_BARS"] = "30%"
    elif name.char_abilities["STR"] in range(18, 19) and name.char_abilities['EX_STR'] in range(91, 100):
        name.char_define_abilities["STR"]["HIT"] = "+2"
        name.char_define_abilities["STR"]["DMG"] = "+5"
        name.char_define_abilities["STR"]["WEIGHT"] = "+2000"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-4 (Locked/Barred: 1)"
        name.char_define_abilities["STR"]["BEND_BARS"] = "35%"
    elif name.char_abilities["STR"] in range(18, 19) and name.char_abilities['EX_STR'] in range(91, 100):
        name.char_define_abilities["STR"]["HIT"] = "+3"
        name.char_define_abilities["STR"]["DMG"] = "+6"
        name.char_define_abilities["STR"]["WEIGHT"] = "+3000"
        name.char_define_abilities["STR"]["OPEN_DOOR"] = "1-5 (Locked/Barred: 2)"
        name.char_define_abilities["STR"]["BEND_BARS"] = "40%"

    if name.char_abilities["INT"] in range(3, 8):
        name.char_define_abilities["INT"]["LANG"] = "No extras."
    elif name.char_abilities["INT"] == 8:
        name.char_define_abilities["INT"]["LANG"] = "1 Additional Language Possible."
    elif name.char_abilities["INT"] == 9:
        name.char_define_abilities["INT"]["LANG"] = "1 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "35% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "4"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "6"
    elif name.char_abilities["INT"] in range(10, 12):
        name.char_define_abilities["INT"]["LANG"] = "2 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "45% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "5"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "7"
    elif name.char_abilities["INT"] == 12:
        name.char_define_abilities["INT"]["LANG"] = "3 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "45% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "5"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "7"
    elif name.char_abilities["INT"] == 13:
        name.char_define_abilities["INT"]["LANG"] = "3 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "55% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "6"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "9"
    elif name.char_abilities["INT"] == 14:
        name.char_define_abilities["INT"]["LANG"] = "4 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "55% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "6"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "9"
    elif name.char_abilities["INT"] == 15:
        name.char_define_abilities["INT"]["LANG"] = "4 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "65% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "7"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "11"
    elif name.char_abilities["INT"] == 16:
        name.char_define_abilities["INT"]["LANG"] = "5 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "65% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "7"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "11"
    elif name.char_abilities["INT"] == 17:
        name.char_define_abilities["INT"]["LANG"] = "6 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "75% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "8"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "14"
    elif name.char_abilities["INT"] == 18:
        name.char_define_abilities["INT"]["LANG"] = "7 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "85% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "9"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "18"
    elif name.char_abilities["INT"] == 19:
        name.char_define_abilities["INT"]["LANG"] = "7 Additional Language Possible."
        name.char_define_abilities["INT"]["Know Spell"] = "95% Chance to Know Spell"
        name.char_define_abilities["INT"]["Min Spells/Level"] = "10"
        name.char_define_abilities["INT"]["Max Spells/Level"] = "All"

    if name.char_abilities["WIS"] == 3:
        name.char_define_abilities["WIS"]["Magical Save"] = "-3"
    elif name.char_abilities["WIS"] == 4:
        name.char_define_abilities["WIS"]["Magical Save"] = "-2"
    elif name.char_abilities["WIS"] in range(5, 8):
        name.char_define_abilities["WIS"]["Magical Save"] = "-1"
    elif name.char_abilities["WIS"] == 8:
        name.char_define_abilities["WIS"]["Magical Save"] = "0"
    elif name.char_abilities["WIS"] == 9:
        name.char_define_abilities["WIS"]["Magical Save"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "20%"
    elif name.char_abilities["WIS"] == 10:
        name.char_define_abilities["WIS"]["Magical Save"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "15%"
    elif name.char_abilities["WIS"] == 11:
        name.char_define_abilities["WIS"]["Magical Save"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "10%"
    elif name.char_abilities["WIS"] == 12:
        name.char_define_abilities["WIS"]["Magical Save"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "5%"
    elif name.char_abilities["WIS"] == 13:
        name.char_define_abilities["WIS"]["Magical Save"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "1:1L"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "0%"
    elif name.char_abilities["WIS"] == 14:
        name.char_define_abilities["WIS"]["Magical Save"] = "0"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "2:1L"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "0%"
    elif name.char_abilities["WIS"] == 15:
        name.char_define_abilities["WIS"]["Magical Save"] = "+1"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "2:1L, 1:2L"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "0%"
    elif name.char_abilities["WIS"] == 16:
        name.char_define_abilities["WIS"]["Magical Save"] = "+2"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "2:1L, 2:2L"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "0%"
    elif name.char_abilities["WIS"] == 17:
        name.char_define_abilities["WIS"]["Magical Save"] = "+3"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "2:1L, 2:2L, 1:3L"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "0%"
    elif name.char_abilities["WIS"] == 18:
        name.char_define_abilities["WIS"]["Magical Save"] = "+4"
        name.char_define_abilities["WIS"]["Cleric Spell Bonus"] = "2:1L, 2:2L, 1:3L, 1:4L"
        name.char_define_abilities["WIS"]["Cleric Spell Failure"] = "0%"

    if name.char_abilities["DEX"] == 3:
        name.char_define_abilities["DEX"]["Reaction"] = "-3"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "+4"
    elif name.char_abilities["DEX"] == 4:
        name.char_define_abilities["DEX"]["Reaction"] = "-2"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "+3"
    elif name.char_abilities["DEX"] == 5:
        name.char_define_abilities["DEX"]["Reaction"] = "-1"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "+2"
    elif name.char_abilities["DEX"] == 5:
        name.char_define_abilities["DEX"]["Reaction"] = "0"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "+1"
    elif name.char_abilities["DEX"] in range(7,15):
        name.char_define_abilities["DEX"]["Reaction"] = "0"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "0"
    elif name.char_abilities["DEX"] == 15:
        name.char_define_abilities["DEX"]["Reaction"] = "0"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "-1"
    elif name.char_abilities["DEX"] == 16:
        name.char_define_abilities["DEX"]["Reaction"] = "+1"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "-2"
    elif name.char_abilities["DEX"] == 17:
        name.char_define_abilities["DEX"]["Reaction"] = "+2"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "-3"
    elif name.char_abilities["DEX"] == 18:
        name.char_define_abilities["DEX"]["Reaction"] = "+3"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "-4"
    elif name.char_abilities["DEX"] == 19:
        name.char_define_abilities["DEX"]["Reaction"] = "+3"
        name.char_define_abilities["DEX"]["Missile To Hit"] = name.char_define_abilities["DEX"]["Reaction"]
        name.char_define_abilities["DEX"]["Defensive"] = "-4"

    if name.char_abilities["CON"] == 3:
        name.char_define_abilities["CON"]["HP Adj"] = "-2"
        name.char_define_abilities["CON"]["System Shock"] = "35%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "40%"
    elif name.char_abilities["CON"] == 4:
        name.char_define_abilities["CON"]["HP Adj"] = "-1"
        name.char_define_abilities["CON"]["System Shock"] = "40%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "45%"
    elif name.char_abilities["CON"] == 5:
        name.char_define_abilities["CON"]["HP Adj"] = "-1"
        name.char_define_abilities["CON"]["System Shock"] = "45%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "50%"
    elif name.char_abilities["CON"] == 6:
        name.char_define_abilities["CON"]["HP Adj"] = "-1"
        name.char_define_abilities["CON"]["System Shock"] = "50%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "55%"
    elif name.char_abilities["CON"] == 7:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "55%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "60%"
    elif name.char_abilities["CON"] == 8:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "60%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "65%"
    elif name.char_abilities["CON"] == 9:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "65%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "70%"
    elif name.char_abilities["CON"] == 10:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "70%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "75%"
    elif name.char_abilities["CON"] == 11:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "75%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "80%"
    elif name.char_abilities["CON"] == 12:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "80%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "85%"
    elif name.char_abilities["CON"] == 13:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "85%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "90%"
    elif name.char_abilities["CON"] == 14:
        name.char_define_abilities["CON"]["HP Adj"] = "0"
        name.char_define_abilities["CON"]["System Shock"] = "88%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "92%"
    elif name.char_abilities["CON"] == 15:
        name.char_define_abilities["CON"]["HP Adj"] = "+1"
        name.char_define_abilities["CON"]["System Shock"] = "91%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "94%"
    elif name.char_abilities["CON"] == 16:
        name.char_define_abilities["CON"]["HP Adj"] = "+2"
        name.char_define_abilities["CON"]["System Shock"] = "95%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "96%"
    elif name.char_abilities["CON"] == 17:
        name.char_define_abilities["CON"]["HP Adj"] = "+2"
        for c in name.char_class:
            if str(c) in fighters:
                name.char_define_abilities["CON"]["HP Adj"] = "+3"
        name.char_define_abilities["CON"]["System Shock"] = "97%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "98%"
    elif name.char_abilities["CON"] == 18:
        name.char_define_abilities["CON"]["HP Adj"] = "+2"
        for c in name.char_class:
            if str(c) in fighters:
                name.char_define_abilities["CON"]["HP Adj"] = "+4"
        name.char_define_abilities["CON"]["System Shock"] = "99%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "100%"
    elif name.char_abilities["CON"] == 19:
        name.char_define_abilities["CON"]["HP Adj"] = "+2"
        for c in name.char_class:
            if str(c) in fighters:
                name.char_define_abilities["CON"]["HP Adj"] = "+5"
        name.char_define_abilities["CON"]["System Shock"] = "99%"
        name.char_define_abilities["CON"]["Ressurection Survival"] = "100%"
        name.char_define_abilities["CON"]["Poison Save"] = "+1"
        name.char_define_abilities["CON"]["Hearty"] = "Cannot Roll 1 for HP"

    if name.char_abilities["CHA"] == 3:
        name.char_define_abilities["CHA"]["Henchmen"] = "1"
        name.char_define_abilities["CHA"]["Loyalty"] = "-30%"
        name.char_define_abilities["CHA"]["Reaction"] = "-25%"
    elif name.char_abilities["CHA"] == 4:
        name.char_define_abilities["CHA"]["Henchmen"] = "1"
        name.char_define_abilities["CHA"]["Loyalty"] = "-25%"
        name.char_define_abilities["CHA"]["Reaction"] = "-20%"
    elif name.char_abilities["CHA"] == 5:
        name.char_define_abilities["CHA"]["Henchmen"] = "2"
        name.char_define_abilities["CHA"]["Loyalty"] = "-20%"
        name.char_define_abilities["CHA"]["Reaction"] = "-15%"
    elif name.char_abilities["CHA"] == 6:
        name.char_define_abilities["CHA"]["Henchmen"] = "2"
        name.char_define_abilities["CHA"]["Loyalty"] = "-15%"
        name.char_define_abilities["CHA"]["Reaction"] = "-10%"
    elif name.char_abilities["CHA"] == 7:
        name.char_define_abilities["CHA"]["Henchmen"] = "3"
        name.char_define_abilities["CHA"]["Loyalty"] = "-10%"
        name.char_define_abilities["CHA"]["Reaction"] = "-5%"
    elif name.char_abilities["CHA"] == 8:
        name.char_define_abilities["CHA"]["Henchmen"] = "3"
        name.char_define_abilities["CHA"]["Loyalty"] = "-5%"
        name.char_define_abilities["CHA"]["Reaction"] = "0%"
    elif name.char_abilities["CHA"] in range(9, 12):
        name.char_define_abilities["CHA"]["Henchmen"] = "4"
        name.char_define_abilities["CHA"]["Loyalty"] = "0%"
        name.char_define_abilities["CHA"]["Reaction"] = "0%"
    elif name.char_abilities["CHA"] == 12:
        name.char_define_abilities["CHA"]["Henchmen"] = "5"
        name.char_define_abilities["CHA"]["Loyalty"] = "0%"
        name.char_define_abilities["CHA"]["Reaction"] = "0%"
    elif name.char_abilities["CHA"] == 13:
        name.char_define_abilities["CHA"]["Henchmen"] = "5"
        name.char_define_abilities["CHA"]["Loyalty"] = "0%"
        name.char_define_abilities["CHA"]["Reaction"] = "+5%"
    elif name.char_abilities["CHA"] == 14:
        name.char_define_abilities["CHA"]["Henchmen"] = "6"
        name.char_define_abilities["CHA"]["Loyalty"] = "+5%"
        name.char_define_abilities["CHA"]["Reaction"] = "+10%"
    elif name.char_abilities["CHA"] == 15:
        name.char_define_abilities["CHA"]["Henchmen"] = "7"
        name.char_define_abilities["CHA"]["Loyalty"] = "+15%"
        name.char_define_abilities["CHA"]["Reaction"] = "+15%"
    elif name.char_abilities["CHA"] == 16:
        name.char_define_abilities["CHA"]["Henchmen"] = "8"
        name.char_define_abilities["CHA"]["Loyalty"] = "+20%"
        name.char_define_abilities["CHA"]["Reaction"] = "+25%"
    elif name.char_abilities["CHA"] == 17:
        name.char_define_abilities["CHA"]["Henchmen"] = "10"
        name.char_define_abilities["CHA"]["Loyalty"] = "+30%"
        name.char_define_abilities["CHA"]["Reaction"] = "+30%"
    elif name.char_abilities["CHA"] == 18:
        name.char_define_abilities["CHA"]["Henchmen"] = "15"
        name.char_define_abilities["CHA"]["Loyalty"] = "+40%"
        name.char_define_abilities["CHA"]["Reaction"] = "+35%"

    if name.char_abilities["CMS"] in range(14, 18):
        fasc = round(name.char_abilities["CMS"] / 2)
        name.char_define_abilities["CMS"]["Fascinate"] = "Fascinate if Opponent's WIS < {}".format(str(fasc))
    elif name.char_abilities["CMS"] in range(18, 22):
        fasc = round(name.char_abilities["CMS"] / 3)
        fasc = name.char_abilities["CMS"] - fasc
        name.char_define_abilities["CMS"]["Fascinate"] = "Fascinate if Opponent's WIS < {}".format(str(fasc))

    if "Thief" in name.char_class or "Assassin" in name.char_class or "Monk" in name.char_class or "Barbarian" in\
            name.char_class:
        if name.char_abilities["DEX"] == 9:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "-15%"
            name.char_define_abilities["DEX"]["Open Locks"] = "-10%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "-10%"
            name.char_define_abilities["DEX"]["Move Silent"] = "-20%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "-10%"
        elif name.char_abilities["DEX"] == 10:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "-10%"
            name.char_define_abilities["DEX"]["Open Locks"] = "-5%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "-10%"
            name.char_define_abilities["DEX"]["Move Silent"] = "-15%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "-5%"
        elif name.char_abilities["DEX"] == 11:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "-5%"
            name.char_define_abilities["DEX"]["Open Locks"] = "0%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "-5%"
            name.char_define_abilities["DEX"]["Move Silent"] = "-10%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif name.char_abilities["DEX"] == 12:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "0%"
            name.char_define_abilities["DEX"]["Open Locks"] = "0%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            name.char_define_abilities["DEX"]["Move Silent"] = "-5%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif name.char_abilities["DEX"] in range(13, 16):
            name.char_define_abilities["DEX"]["Pick Pockets"] = "0%"
            name.char_define_abilities["DEX"]["Open Locks"] = "0%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            name.char_define_abilities["DEX"]["Move Silent"] = "0%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif name.char_abilities["DEX"] == 16:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "0%"
            name.char_define_abilities["DEX"]["Open Locks"] = "+5%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            name.char_define_abilities["DEX"]["Move Silent"] = "0%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "0%"
        elif name.char_abilities["DEX"] == 17:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "+5%"
            name.char_define_abilities["DEX"]["Open Locks"] = "+10%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "0%"
            name.char_define_abilities["DEX"]["Move Silent"] = "+5%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "+5%"
        elif name.char_abilities["DEX"] == 18:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "+10%"
            name.char_define_abilities["DEX"]["Open Locks"] = "+15%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "+5%"
            name.char_define_abilities["DEX"]["Move Silent"] = "+10%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "+10%"
        elif name.char_abilities["DEX"] == 19:
            name.char_define_abilities["DEX"]["Pick Pockets"] = "+15%"
            name.char_define_abilities["DEX"]["Open Locks"] = "+20%"
            name.char_define_abilities["DEX"]["Find/Remove Traps"] = "+10%"
            name.char_define_abilities["DEX"]["Move Silent"] = "+12%"
            name.char_define_abilities["DEX"]["Hide In Shadows"] = "+1%"
    return name