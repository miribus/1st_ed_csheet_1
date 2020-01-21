import openpyxl
import os, re

template_dir = str(os.getcwd()+"\\sheet_template\\")
sheets_dir = str(os.getcwd()+"\\sheets\\")


template = template_dir+"template_1st_ed.xlsx"

templ = openpyxl.load_workbook(template)
tp = templ.active

def character_print(name):
    global output
    output = sheets_dir + str(name.char_name)+".xlsx"
    tp['B1'] = name.char_name
    tp['E1'] = name.char_alignment
    tp['B2'] = name.char_race
    if len(name.char_class_levels) == 1:
        tp['E2'] = str(name.char_class_levels[0])
    elif len(name.char_class_levels) == 2:
        tp['E2'] = str(name.char_class_levels[0]) + "/" + str(name.char_class_levels[1])
    elif len(name.char_class_levels) == 3:
        tp['E2'] = str(name.char_class_levels[0]) + "/" + str(name.char_class_levels[1]) + "/" + \
                   str(name.char_class_levels[2])

    if len(name.char_class) == 1:
        tp['G1'] = str(name.char_class[0])
    elif len(name.char_class) == 2:
        tp['G1'] = str(name.char_class[0]) + "/" + str(name.char_class[1])
    elif len(name.char_class) == 3:
        tp['G1'] = str(name.char_class[0]) + "/" + str(name.char_class[1]) + "/" + \
                   str(name.char_class[2])

    tp['E3'] = str(name.social_class)

    if len(name.char_class_nextXP) == 1:
        tp['B80'] = str(name.char_class_nextXP[0])
        tp['C80'] = str(name.char_class[0]) + " " +str(name.char_class_xpBonus[0]) \
            if len(name.char_class_xpBonus) > 0 else str(name.char_class[0])
    elif len(name.char_class_levels) == 2:
        tp['B80'] = str(name.char_class_nextXP[0])
        tp['B81'] = str(name.char_class_nextXP[1])
        tp['C80'] = str(name.char_class[0]) + " " +str(name.char_class_xpBonus[0])
        tp['C81'] = str(name.char_class[1]) + " " +str(name.char_class_xpBonus[1])
    elif len(name.char_class_levels) == 3:
        tp['B80'] = str(name.char_class_nextXP[0])
        tp['B81'] = str(name.char_class_nextXP[1])
        tp['B82'] = str(name.char_class_nextXP[2])
        tp['C80'] = str(name.char_class[0]) + " " + str(name.char_class_xpBonus[0])
        tp['C81'] = str(name.char_class[1]) + " " + str(name.char_class_xpBonus[1])
        tp['C82'] = str(name.char_class[2]) + " " + str(name.char_class_xpBonus[2])
    tp['G2'] = str(name.char_age)
    tp['N2'] = str(name.char_HP)
    tp['I3'] = str(name.char_gender)
    if name.char_abilities["EX_STR"]:
        extr = "/"+str(name.char_abilities["EX_STR"])
    else:
        extr = ""
    strtr = ""
    dextr = ""
    contr = ""
    chatr = ""
    if "Cavalier" in name.char_class_abilities or "UAPaladin" in name.char_class_abilities and not name.self_roll:
        if "STR Training" in name.char_class_abilities[name.char_class[0]]:
            strtr = "/" + str(name.char_class_abilities[name.char_class[0]]["STR Training"])
        if "DEX Training" in name.char_class_abilities[name.char_class[0]]:
            dextr = "/" + str(name.char_class_abilities[name.char_class[0]]["DEX Training"])
        if "CON Training" in name.char_class_abilities[name.char_class[0]]:
            contr = "/" + str(name.char_class_abilities[name.char_class[0]]["CON Training"])
        if "UAPaladin" in name.char_class:
            if "CHA Training" in name.char_class_abilities[name.char_class[0]]:
                chatr = "/" + str(name.char_class_abilities[name.char_class[0]]["CHA Training"])
    elif "Cavalier" in name.char_class_abilities or "UAPaladin" in name.char_class_abilities and name.self_roll:
        strtr = "/"
        dextr = "/"
        contr = "/"
        chatr = "/"
    if extr != "":
        tp['B6'] = str(name.char_abilities["STR"])+str(extr)
    else:
        tp['B6'] = str(name.char_abilities["STR"]) + str(strtr)
    tp['D6'] = str(name.char_define_abilities["STR"]["HIT"])
    tp['F6'] = str(name.char_define_abilities["STR"]["DMG"])
    tp['H6'] = str(name.char_define_abilities["STR"]["WEIGHT"])
    tp['J6'] = str(name.char_define_abilities["STR"]["OPEN_DOOR"])
    tp['L6'] = str(name.char_define_abilities["STR"]["BEND_BARS"])
    tp['B7'] = str(name.char_abilities["INT"])
    tp['D7'] = str(name.char_define_abilities["INT"]["LANG"])
    tp['F7'] = str(name.char_define_abilities["INT"]["Know Spell"])
    tp['H7'] = str(name.char_define_abilities["INT"]["Min Spells/Level"])
    tp['I7'] = str(name.char_define_abilities["INT"]["Max Spells/Level"])
    tp['B8'] = str(name.char_abilities["WIS"])
    tp['D8'] = str(name.char_define_abilities["WIS"]["Magical Save"])
    tp['F8'] = str(name.char_define_abilities["WIS"]["Cleric Spell Failure"])
    tp['H8'] = str(name.char_define_abilities["WIS"]["Cleric Spell Bonus"])
    tp['B9'] = str(name.char_abilities["DEX"])+dextr
    tp['D9'] = str(name.char_define_abilities["DEX"]["Reaction"])
    tp['F9'] = str(name.char_define_abilities["DEX"]["Missile To Hit"])
    tp['H9'] = str(name.char_define_abilities["DEX"]["Defensive"])
    tp['B10'] = str(name.char_abilities["CON"])+contr
    tp['D10'] = str(name.char_define_abilities["CON"]["HP Adj"])
    tp['F10'] = str(name.char_define_abilities["CON"]["System Shock"])
    tp['H10'] = str(name.char_define_abilities["CON"]["Ressurection Survival"])
    tp['B11'] = str(name.char_abilities["CHA"])+chatr
    tp['D11'] = str(name.char_define_abilities["CHA"]["Henchmen"])
    tp['F11'] = str(name.char_define_abilities["CHA"]["Loyalty"])
    tp['H11'] = str(name.char_define_abilities["CHA"]["Reaction"])
    tp['B12'] = str(name.char_abilities["CMS"])
    tp['D12'] = str(name.char_define_abilities["CMS"]["Fascinate"])
    if "Thief" in name.char_class or "Barbarian" in name.char_class or "Monk" in name.char_class:
        tp['I10'] = "PPK: " + str(name.char_define_abilities["DEX"]["Pick Pockets"]) + "  " + \
                    "OPL: " + str(name.char_define_abilities["DEX"]["Open Locks"]) + "  " + \
                    "FTR: " + str(name.char_define_abilities["DEX"]["Find/Remove Traps"]) + "  " + \
                    "MVS: " + str(name.char_define_abilities["DEX"]["Move Silent"]) + "  " + \
                    "HIS: " + str(name.char_define_abilities["DEX"]["Hide In Shadows"])
    tp['N9'] = str(name.char_saves["Poison"])
    tp['N10'] = str(name.char_saves["Petrification"])
    tp['N11'] = str(name.char_saves["Rods, Staves, Wands"])
    tp['N12'] = str(name.char_saves["Breath Weapon"])
    tp['N13'] = str(name.char_saves["Spells"])
    tp['B14'] = str(name.char_AC["AC"])
    tp['D14'] = re.sub(r'\[|]|\'', '', str(name.char_movement_rate))
    tp['B15'] = str(name.char_AC["Surprised"])
    tp['B16'] = str(name.char_AC["Shieldless"])
    tp['B17'] = str(name.char_AC["Rear"])
    tp['B18'] = str(name.char_AC["Naked"])
    tp['D15'] = str(name.char_encumbrance["Current"])
    tp['D16'] = str(name.char_encumbrance["Fairly"])
    tp['D17'] = str(name.char_encumbrance["Bulky"])
    tp['D18'] = str(name.char_encumbrance["Encumbered"])
    #
    for a in name.char_armor:
        tp['E15'] = str(a)
        tp['G15'] = str(name.char_armor[a]["Armor Class"])
        tp['H15'] = str(name.char_armor[a]["Bulk"])
        break
    for s in name.char_shield:
        tp['E16'] = str(s)
        tp['G16'] = str(name.char_shield[s]["Armor Class"])
        tp['H16'] = str(name.char_shield[s]["Bulk"])
        break
    #
    weapon_slots = [["20", "21"], ["23", "24"], ["26", "27"], ["29", "30"], ["32", "33"], ["35", "36"],
                    ["38", "39"], ["41", "42"]]

    all_weapons = {}
    for w in name.char_melee_weapons:
        all_weapons[w] = name.char_melee_weapons[w]
    for w in name.char_ranged_weapons:
        all_weapons[w] = name.char_ranged_weapons[w]
    idx = -1
    more_inventory = []
    for a in all_weapons:
        idx += 1
        if idx < 8:
            tp["A{}".format(weapon_slots[idx][0])] = a
            tp["C{}".format(weapon_slots[idx][0])] = "S-M: "+ all_weapons[a]["Damage S-M"] + \
                                                 "/ L: " + all_weapons[a]["Damage L"]
            tp["E{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 0"]
            tp["F{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 1"]
            tp["G{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 2"]
            tp["H{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 3"]
            tp["I{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 4"]
            tp["J{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 5"]
            tp["K{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 6"]
            tp["L{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 7"]
            tp["M{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 8"]
            tp["N{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 9"]
            tp["O{}".format(weapon_slots[idx][0])] = all_weapons[a]["THACADJ 10"]
            tp["P{}".format(weapon_slots[idx][0])] = all_weapons[a]["Type"]
            tp["B{}".format(weapon_slots[idx][1])] = all_weapons[a]["Speed"]
            tp["D{}".format(weapon_slots[idx][1])] = all_weapons[a]["Length"] + \
                                                     " / " + all_weapons[a]["Space"]
            tp["F{}".format(weapon_slots[idx][1])] = all_weapons[a]["Norm Hit"]
            tp["H{}".format(weapon_slots[idx][1])] = all_weapons[a]["Norm Dmg"]
            tp["J{}".format(weapon_slots[idx][1])] = all_weapons[a]["Notes"]
        if idx > 7:
            wp = [a, all_weapons[a]["Encumbrance"]]
            more_inventory.append(wp)
    for i in name.char_inventory:
        iv = [i, name.char_inventory[i]["Encumbrance"]]
        more_inventory.append(iv)

    idx = 0
    prof_slots = ["62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73"]
    tp["N61"] = "Non Proficient Penalty: {}".format(str(name.char_weapon_prof_penalty))
    for p in name.char_weapon_prof:
        tp["N{}".format(prof_slots[idx])] = p
        idx += 1
    tp['A44'] = re.sub(r'\[|]|\']', '', str(name.char_race_abilities["Racial Languages"]))

    idx = 0
    skills_slots = ["E44", "E47", "E50", "E53", "E56", "E59", "E62", "E65", "E68", "E71",
                    "H44", "H47", "H50", "H53", "H56", "H59", "H62", "H65", "H68", "H71",
                    "K44", "K47", "K50", "K53", "K56", "K59", "K62", "K65", "K68", "K71",
                    "N44", "N47", "N50", "N53", "N56"]

    class_skills = {}
    for a in name.char_class_abilities:
        for k in name.char_class_abilities[a]:
            class_skills[k] = str(k)+": "+re.sub(r'} | { ', '', str(name.char_class_abilities[a][k]))
            print(re.sub(r'} | { ', '', str(name.char_class_abilities[a][k])))
    for r in name.char_race_abilities:
        class_skills[r] = str(r)+": "+re.sub(r'} | { ', '', str(name.char_race_abilities[r]))
        print(re.sub(r'} | { ', '', str(name.char_race_abilities[r])))
    for c in class_skills:
        tp[skills_slots[idx]] = class_skills[c]
        idx += 1
        if idx > 35:
            break

    inventory_slots = ["49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67",
                       "68", "69", "70", "71", "72", "73",
                       "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117",
                       "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131",
                       "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145",
                       "146"]

    idx = -1
    for m in more_inventory:
        idx += 1
        if idx < 25:
            tp['A{}'.format(inventory_slots[idx])] = str(m[0])
            tp['C{}'.format(inventory_slots[idx])] = str(m[1])
        if idx > 67:
            break
        if idx > 24:
            tp['F{}'.format(inventory_slots[idx])] = str(m[0])
            tp['I{}'.format(inventory_slots[idx])] = str(m[1])

    tp['E79'] = name.char_money["pp"]
    tp['E80'] = name.char_money["gp"]
    tp['E81'] = name.char_money["ep"]
    tp['E82'] = name.char_money["sp"]
    tp['E83'] = name.char_money["cp"]

    templ.save(output)