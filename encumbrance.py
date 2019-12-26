def calculate_encumbrance(name):
    equip_encumbrance = 0
    for n in name.char_melee_weapons:
        enc = name.char_melee_weapons[n]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
    for r in name.char_ranged_weapons:
        enc = name.char_melee_weapons[n]["Encumbrance"]
        enc = str(enc).replace("w", "")
        enc = int(enc)
        equip_encumbrance += enc
