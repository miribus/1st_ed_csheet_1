def races_base(race, rolls):
    if race == "Dwarf":
        race = "Dwarf"
        result = dwarf(rolls)
    elif race == "Elf":
        race = "Elf"
        result = elf(rolls)
    elif race == "Gnome":
        race = "Gnome"
        result = gnome(rolls)
    elif race == "Half-Elf":
        race = "Half-Elf"
        result = half_elf(rolls)
    elif race == "Half-Orc":
        race = "Half-Orc"
        result = half_orc(rolls)
    elif race == "Human":
        race = "Human"
        result = human(rolls)


def minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma):
    result = False
    if rolls["STR"] < strength:
        print("Insufficient minimum Strength", strength, "required")
        return result
    if rolls["INT"] < dexterity:
        print("Insufficient minimum Intelligence", dexterity, "required")
        return result
    if rolls["WIZ"] < constitution:
        print("Insufficient minimum Wisdom", constitution, "required")
        return result
    if rolls["DEX"] < intelligence:
        print("Insufficient minimum Dexterity", intelligence, "required")
        return result
    if rolls["CON"] < wisdom:
        print("Insufficient minimum Wisdom", wisdom, "required")
        return result
    if rolls["CHA"] < charisma:
        print("Insufficient minimum Charisma", charisma, "required")
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

