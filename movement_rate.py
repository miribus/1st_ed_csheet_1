def calculate_move(name, fairly, bulky, encumbered):
    if encumbered:
        name.char_movement_rate["Base"] = "4\""
        return name
    elif bulky:
        name.char_movement_rate["Base"] = "6\""
        return name
    elif fairly:
        name.char_movement_rate["Base"] = "9\""
        return name
    elif "Barbarian" in name.char_class:
        name.char_movement_rate["Base"] = "15\""
        return name
    else:
        name.char_movement_rate["Base"] = "12\""
        return name
