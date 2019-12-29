import movement_rate

def calculate_encumbrance(name):
    equip_encumbrance = 0
    bulky = False
    fairly = False
    encumbered = False
    for n in name.char_melee_weapons:
        enc = name.char_melee_weapons[n]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for r in name.char_ranged_weapons:
        if "Thrown" not in name.char_ranged_weapons[r]["Type"]:
            enc = name.char_ranged_weapons[r]["Encumbrance"]
            enc = str(enc).replace("w", "")
            enc = int(enc)
            equip_encumbrance += enc
    for a in name.char_armor:
        enc = name.char_armor[a]["Encumbrance"]
        if name.char_armor[a]["Bulk"] == 'bulky':
            bulky = True
        elif name.char_armor[a]["Bulk"] == 'fairly':
            fairly = True
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for s in name.char_shield:
        enc = name.char_shield[s]["Encumbrance"]
        if name.char_shield[s]["Bulk"] == 'bulky':
            bulky = True
        elif name.char_shield[s]["Bulk"] == 'fairly':
            fairly = True
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for i in name.char_inventory:
        if '*' not in i:
            enc = name.char_inventory[i]["Encumbrance"]
            enc = str(enc).replace("w", "")
            enc = int(enc)
            equip_encumbrance += enc

    adjusted_encumbrance = name.char_define_abilities["STR"]["WEIGHT"]
    adjusted_encumbrance = int(adjusted_encumbrance)
    adjusted_encumbrance += 350
    name.char_encumbrance["Fairly"] = 350 + adjusted_encumbrance
    name.char_encumbrance["Bulky"] = name.char_encumbrance["Fairly"] + 400
    name.char_encumbrance["Encumbered"] = name.char_encumbrance["Bulky"] + 300
    name.char_encumbrance["Overloaded"] = name.char_encumbrance["Encumbered"] + 350

    #if adjusted_encumbrance - equip_encumbrance >= -350:
    #    print("Not", adjusted_encumbrance, equip_encumbrance)
    if adjusted_encumbrance - equip_encumbrance in range(-350, -750):
        fairly = True
    elif adjusted_encumbrance - equip_encumbrance in range(-750, -1050):
        bulky = True
    elif adjusted_encumbrance - equip_encumbrance in range(-1050, -1401):
        encumbered = True

    name = movement_rate.calculate_move(name, fairly, bulky, encumbered)
    name.char_encumbrance["Current"] = equip_encumbrance
    return name