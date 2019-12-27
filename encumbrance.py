def calculate_encumbrance(name):
    equip_encumbrance = 0
    bulky = False
    fairly = False
    for n in name.char_melee_weapons:
        enc = name.char_melee_weapons[n]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for r in name.char_ranged_weapons:
        enc = name.char_ranged_weapons[r]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for a in name.char_armor:
        enc = name.char_armor[a]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for s in name.char_shield:
        enc = name.char_shield[s]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for i in name.char_inventory:
        enc = name.char_inventory[i]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc

    adjusted_encumbrance = name.char_define_abilities["STR"]["WEIGHT"]
    adjusted_encumbrance = int(adjusted_encumbrance)
    adjusted_encumbrance += 350


    print("ENCH!!!!", equip_encumbrance)