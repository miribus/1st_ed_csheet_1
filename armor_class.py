def calculate_armor_class(name):
    if "Barbarian" in name.char_class and name.char_abilities["DEX"] > 14:
        bulk = False
        if len(name.char_armor) > 0:
            for a in name.char_armor:
                if name.char_armor[a]["Bulk"] != "non":
                    bulk = True
        if len(name.char_shield) > 0:
            for s in name.char_shield:
                if name.char_shield[s]["Bulk"] != "non":
                    bulk = True
        if not bulk:
            defense = name.char_abilities["DEX"] - 14
            defense = defense * 2
            name.char_AC["AC"] -= defense
            name.char_AC["Rear"] -= defense
            name.char_AC["Shieldless"] -= defense
    else:
        name.char_AC["AC"] += int(name.char_define_abilities["DEX"]["Defensive"])
        name.char_AC["Rear"] += int(name.char_define_abilities["DEX"]["Defensive"])
        name.char_AC["Shieldless"] += int(name.char_define_abilities["DEX"]["Defensive"])

    for a in name.char_armor:
        name.char_AC["AC"] += int(name.char_armor[a]["Reduction"])
        name.char_AC["Surprised"] += int(name.char_armor[a]["Reduction"])
        name.char_AC["Shieldless"] += int(name.char_armor[a]["Reduction"])
        name.char_AC["Rear"] += int(name.char_armor[a]["Reduction"])
    for s in name.char_shield:
        name.char_AC["AC"] += int(name.char_shield[s]["Reduction"])
        name.char_AC["Surprised"] += int(name.char_shield[s]["Reduction"])
    return name