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
    return result

def minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma):
    result = False
    if rolls["STR"] < strength:
        print("Insufficient! Minimum Strength of", strength, "required")
        return result
    if rolls["INT"] < dexterity:
        print("Insufficient! Minimum Intelligence of", dexterity, "required")
        return result
    if rolls["WIS"] < constitution:
        print("Insufficient! Minimum Wisdom of", constitution, "required")
        return result
    if rolls["DEX"] < intelligence:
        print("Insufficient! Minimum Dexterity of", intelligence, "required")
        return result
    if rolls["CON"] < wisdom:
        print("Insufficient! Minimum Wisdom of", wisdom, "required")
        return result
    if rolls["CHA"] < charisma:
        print("Insufficient! Minimum Charisma of", charisma, "required")
        return result
    result = True
    return result

def dwarf(rolls):
    strength = 8
    dexterity = 3
    constitution = 12
    intelligence = 3
    wisdom = 3
    charisma = 3
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Dwarf character rolls.")
        return True
    else:
        return False


def elf(rolls):
    strength = 3
    dexterity = 7
    constitution = 8
    intelligence = 8
    wisdom = 3
    charisma = 8
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Elf character rolls.")
        return True
    else:
        return False


def gnome(rolls):
    strength = 6
    dexterity = 3
    constitution = 8
    intelligence = 7
    wisdom = 3
    charisma = 3
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Gnome character rolls.")
        return True
    else:
        return False


def half_elf(rolls):
    strength = 3
    dexterity = 6
    constitution = 6
    intelligence = 4
    wisdom = 3
    charisma = 3
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Half-Elf character rolls.")
        return True
    else:
        return False


def half_orc(rolls):
    strength = 6
    dexterity = 8
    constitution = 10
    intelligence = 6
    wisdom = 3
    charisma = 3
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Half-Orc character rolls.")
        return True
    else:
        return False


def human(rolls):
    strength = 3
    dexterity = 3
    constitution = 3
    intelligence = 3
    wisdom = 3
    charisma = 3
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Human character rolls.")
        return True
    else:
        return False

