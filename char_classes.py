'''
    if char_class == "asn":
        saves = assasin()
    elif char_class == "clr":
        saves = cleric()
    elif char_class == "dru":
        saves = druid()
    elif char_class == "ftr":
        saves = fighter()
    elif char_class == "ran":
        saves = ranger()
    elif char_class == "pal":
        saves = paladin()
    elif char_class == "mag":
        saves = magic_user()
    elif char_class == "ill":
        saves = illusionist()
    elif char_class == "thi":
        saves = thief()
'''

def races_base(race, rolls):
    if race.upper() == "Dwarf".upper() or "0" == race:
        race = "Dwarf"
        result = dwarf(rolls)
    elif race.upper() == "Elf".upper() or "1" == race:
        race = "Elf"
        result = elf(rolls)
    elif race.upper() == "Gnome".upper() or "2" == race:
        race = "Gnome"
        result = gnome(rolls)
    elif race.upper() == "Half-Elf".upper() or "3" == race:
        race = "Half-Elf"
        result = half_elf(rolls)
    elif race.upper() == "Half-Orc".upper() or "4" == race:
        race = "Half-Orc"
        result = half_orc(rolls)
    elif race.upper() == "Human".upper() or "5" == race:
        race = "Human"
        result = human(rolls)
    else:
        print("Invalid race choice")
        result = False
    return race, result

def class_min_abilities(rolls):
    result = False
    if rolls["STR"] < strength:
        print("Insufficient! Minimum Strength of", strength, "required")
        return result
    if rolls["INT"] < intelligence:
        print("Insufficient! Minimum Intelligence of", intelligence, "required")
        return result
    if rolls["WIS"] < wisdom:
        print("Insufficient! Minimum Wisdom of", wisdom, "required")
        return result
    if rolls["DEX"] < dexterity:
        print("Insufficient! Minimum Dexterity of", dexterity, "required")
        return result
    if rolls["CON"] < constitution:
        print("Insufficient! Minimum Wisdom of", constitution, "required")
        return result
    if rolls["CHA"] < charisma:
        print("Insufficient! Minimum Charisma of", charisma, "required")
        return result
    result = True
    return result

def dwarf(rolls):
