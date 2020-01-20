import dice

def races_base(race, name):
    print("What GENDER are you playing?")
    result = False
    if str(race).isdigit():
        if int(race) in range(0, 14):
            gender = input("M or F?")
            if gender.isalpha():
                if gender.upper() == "M".upper() or gender.upper() == "F".upper():
                    print(gender)
                    #name.gender = gender
                    if race.upper() == "Dwarf".upper() or "0" == race:
                        race = "Dwarf"
                        result, rolls = dwarf(name.char_abilities, gender)
                    elif race.upper() == "GrayDwarf".upper() or "1" == race:
                        race = "GrayDwarf"
                        result, rolls = graydwarf(name.char_abilities, gender)
                    elif race.upper() == "Elf".upper() or "2" == race:
                        race = "Elf"
                        result, rolls = elf(name.char_abilities, gender)
                    elif race.upper() == "GrayElf".upper() or "3" == race:
                        race = "GrayElf"
                        result, rolls = grayelf(name.char_abilities, gender)
                    elif race.upper() == "WoodElf".upper() or "4" == race:
                        race = "WoodElf"
                        result, rolls = woodelf(name.char_abilities, gender)
                    elif race.upper() == "WildElf".upper() or "5" == race:
                        race = "WildElf"
                        result, rolls = wildelf(name.char_abilities, gender)
                    elif race.upper() == "ValleyElf".upper() or "6" == race:
                        race = "ValleyElf"
                        result, rolls = valleyelf(name.char_abilities, gender)
                    elif race.upper() == "DarkElf".upper() or "7" == race:
                        race = "DarkElf"
                        result, rolls = darkelf(name.char_abilities, gender)
                    elif race.upper() == "Gnome".upper() or "8" == race:
                        race = "Gnome"
                        result, rolls = gnome(name.char_abilities, gender)
                    elif race.upper() == "DeepGnome".upper() or "9" == race:
                        race = "DeepGnome"
                        print("Warning!:  You chose Deep Gnome, you must be Male, changing to Male.")
                        gender = "M"
                        result, rolls = deepgnome(name.char_abilities, gender)
                    elif race.upper() == "Half-Elf".upper() or "10" == race:
                        race = "Half-Elf"
                        result, rolls = half_elf(name.char_abilities, gender)
                    elif race.upper() == "Half-Orc".upper() or "11" == race:
                        race = "Half-Orc"
                        result, rolls = half_orc(name.char_abilities, gender)
                    elif race.upper() == "Human".upper() or "12" == race:
                        race = "Human"
                        result, rolls = human(name.char_abilities, gender)
                    elif race.upper() == "Halfling".upper() or "13" == race:
                        race = "Halfling"
                        result, rolls = halfling(name.char_abilities, gender)
                    name.char_gender = gender
                    name.char_race = race
                    if result:
                        decision = input("Agreed? Y/N:")
                        if str(decision).upper() == "Y".upper():
                            result = True
                        else:
                            result = False
                    else:
                        result = False

    gender = "M"
    return name, result

def minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma):
    result = False
    if rolls["STR"] < strength:
        print("Insufficient! Minimum Strength of", strength, "required")
        return result
    if rolls["INT"] < intelligence:
        print("Insufficient! Minimum Intelligence of", intelligence, "required")
        return result
    if rolls["WIS"] < wisdom:
        print(wisdom, rolls["WIS"])
        print("Insufficient! Minimum Wisdom of", wisdom, "required")
        return result
    if rolls["DEX"] < dexterity:
        print("Insufficient! Minimum Dexterity of", dexterity, "required")
        return result
    if rolls["CON"] < constitution:
        print("Insufficient! Minimum Constitution of", constitution, "required")
        return result
    if rolls["CHA"] < charisma:
        print("Insufficient! Minimum Charisma of", charisma, "required")
        return result
    result = True
    return result

def race_ability_updater(name):
    if name.char_race.upper() == "Dwarf".upper():
        result, rolls = dwarf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "GrayDwarf".upper():
        result, rolls = graydwarf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "Elf".upper():
        result, rolls = elf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "GrayElf".upper():
        result, rolls = grayelf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "WoodElf".upper():
        result, rolls = woodelf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "WildElf".upper():
        result, rolls = wildelf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "ValleyElf".upper():
        result, rolls = valleyelf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "DarkElf".upper():
        result, rolls = darkelf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "Gnome".upper():
        result, rolls = gnome(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "DeepGnome".upper():
        result, rolls = deepgnome(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "Half-Elf".upper():
        result, rolls = half_elf(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "Half-Orc".upper():
        result, rolls = half_orc(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "Human".upper():
        result, rolls = human(name.char_abilities, name.char_gender)
    elif name.char_race.upper() == "Halfling".upper():
        result, rolls = halfling(name.char_abilities, name.char_gender)
    name.char_abilities["STR"] = rolls["STR"]
    name.char_abilities["INT"] = rolls["INT"]
    name.char_abilities["WIS"] = rolls["WIS"]
    name.char_abilities["DEX"] = rolls["DEX"]
    name.char_abilities["CON"] = rolls["CON"]
    name.char_abilities["CHA"] = rolls["CHA"]
    return name

def dwarf(rolls, gender):
    strength = 8
    if gender == "Female":
        mx_strength = 17
    else:
        mx_strength = 18
    dexterity = 3
    mx_dexterity = 17
    constitution = 12
    mx_constitution = 19
    intelligence = 3
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 16
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Dwarf character rolls.")
        return True, rolls
    else:
        return False, rolls


def graydwarf(rolls, gender):
    strength = 8
    if gender == "Female":
        mx_strength = 17
    else:
        mx_strength = 18
    dexterity = 3
    mx_dexterity = 17
    constitution = 12
    mx_constitution = 19
    intelligence = 3
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 16
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Gray Dwarf character rolls.")
        return True, rolls
    else:
        return False, rolls



def elf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 16
    else:
        mx_strength = 18
    dexterity = 7
    mx_dexterity = 19
    constitution = 8
    mx_constitution = 18
    intelligence = 8
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 8
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Elf character rolls.")
        return True, rolls
    else:
        return False, rolls


def darkelf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 16
    else:
        mx_strength = 18
    dexterity = 7
    mx_dexterity = 19
    constitution = 8
    mx_constitution = 18
    intelligence = 8
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 8
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have Dark Elf character rolls.")
        return True, rolls
    else:
        return False, rolls


def grayelf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 16
    else:
        mx_strength = 18
    dexterity = 7
    mx_dexterity = 19
    constitution = 8
    mx_constitution = 18
    intelligence = 8
    mx_intelligence = 19
    wisdom = 3
    mx_wisdom = 18
    charisma = 8
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Gray Elf character rolls.")
        return True, rolls
    else:
        return False, rolls


def valleyelf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 16
    else:
        mx_strength = 18
    dexterity = 7
    mx_dexterity = 19
    constitution = 8
    mx_constitution = 18
    intelligence = 8
    mx_intelligence = 19
    wisdom = 3
    mx_wisdom = 18
    charisma = 8
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Valley Elf character rolls.")
        return True, rolls
    else:
        return False, rolls


def woodelf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 16
    else:
        mx_strength = 18
    dexterity = 7
    mx_dexterity = 19
    constitution = 8
    mx_constitution = 18
    intelligence = 8
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 8
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Wood Elf character rolls.")
        return True, rolls
    else:
        return False, rolls


def wildelf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 16
    else:
        mx_strength = 18
    dexterity = 7
    mx_dexterity = 19
    constitution = 8
    mx_constitution = 18
    intelligence = 8
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 8
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Wild Elf character rolls.")
        return True, rolls
    else:
        return False, rolls

def gnome(rolls, gender):
    strength = 6
    if gender == "Female":
        mx_strength = 15
    else:
        mx_strength = 18
    dexterity = 3
    mx_dexterity = 18
    constitution = 8
    mx_constitution = 18
    intelligence = 7
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Gnome character rolls.")
        return True, rolls
    else:
        return False, rolls

def deepgnome(rolls, gender):
    strength = 6
    if gender == "Female":
        mx_strength = 15
    else:
        mx_strength = 18
    dexterity = 3
    mx_dexterity = 18
    constitution = 8
    mx_constitution = 18
    intelligence = 7
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Gnome character rolls.")
        return True, rolls
    else:
        return False, rolls


def half_elf(rolls, gender):
    strength = 3
    if gender == "Female":
        mx_strength = 17
    else:
        mx_strength = 18
    dexterity = 6
    mx_dexterity = 18
    constitution = 6
    mx_constitution = 18
    intelligence = 4
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Half-Elf character rolls.")
        return True, rolls
    else:
        return False, rolls


def half_orc(rolls, gender):
    strength = 6
    if gender == "Female":
        mx_strength = 18
    else:
        mx_strength = 18
    dexterity = 8
    mx_dexterity = 17
    constitution = 10
    mx_constitution = 19
    intelligence = 6
    mx_intelligence = 17
    wisdom = 3
    mx_wisdom = 14
    charisma = 3
    mx_charisma = 12
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Half-Orc character rolls.")
        return True, rolls
    else:
        return False, rolls


def human(rolls, gender):
    strength = 3
    mx_strength = 18
    dexterity = 3
    mx_dexterity = 18
    constitution = 3
    mx_constitution = 18
    intelligence = 3
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 18
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Human character rolls.")
        return True, rolls
    else:
        return False, rolls

def halfling(rolls, gender):
    strength = 6
    if gender == "Female":
        mx_strength = 14
    else:
        mx_strength = 17
    dexterity = 3
    mx_dexterity = 18
    constitution = 3
    mx_constitution = 19
    intelligence = 3
    mx_intelligence = 18
    wisdom = 3
    mx_wisdom = 17
    charisma = 3
    mx_charisma = 18
    if rolls["STR"] > mx_strength:
        rolls["STR"] = mx_strength
    if rolls["DEX"] > mx_dexterity:
        rolls["DEX"] = mx_dexterity
    if rolls["CON"] > mx_constitution:
        rolls["CON"] = mx_constitution
    if rolls["INT"] > mx_intelligence:
        rolls["INT"] = mx_intelligence
    if rolls["WIS"] > mx_wisdom:
        rolls["WIS"] = mx_wisdom
    if rolls["CHA"] > mx_charisma:
        rolls["CHA"] = mx_charisma
    result = minimums(rolls, strength, dexterity, constitution, intelligence, wisdom, charisma)
    if result:
        print("You have valid Halfling character rolls.")
        return True, rolls
    else:
        return False, rolls

def base_bonuses(name):
    name.char_race_abilities["Save Bonus"] = {}
    if name.char_abilities["INT"] > 15:
        elflang = str(name.char_abilities["INT"]-15)
        elflang = "+{} more".format(elflang)
    else:
        elflang = ""

    if name.char_race == "Elf":
        name.char_abilities["DEX"] += 1
        name.char_abilities["CON"] -= 1
        name.char_race_abilities["Sleep/Charm Resistance"] = "90%"
        name.char_race_abilities["Combat Bonus"] = "Short/Long Swords +1 To Hit, Bows +1 To Hit"
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Hobgoblin", "Orcish",
                                              "Gnoll", "Common", elflang, "Alignment"]
        name.char_race_abilities["Elven Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        name.char_race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)", "Secret: d6, Score 1-2 (Detect: 1-3)"]
    elif name.char_race == "DarkElf":
        name.char_abilities["DEX"] += 1
        name.char_abilities["CON"] -= 1
        name.char_race_abilities["Sleep/Charm Resistance"] = "90%"
        name.char_race_abilities["DE Save Bonus"] = "+2 vs. Magical Saves"
        name.char_race_abilities["Combat Bonus"] = "Can dual-wield 1h weapons without penalty."
        name.char_race_abilities["Infravision"] = "12\""
        name.char_race_abilities["Racial Languages"] = ["Undercommon", "Gnome", "Alignment", "Common", "Elvish"]
        name.char_race_abilities["Detect New Construction Underground"] = "d4, score 1-3"
        name.char_race_abilities["Detect Sliding/Shifting Construction Underground"] = "d6, score 1-4"
        name.char_race_abilities["Detect Stone Trapwork"] = "d4, score 1-2"
        name.char_race_abilities["Elven Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        name.char_race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)", "Secret: d6, Score 1-2 (Detect: 1-3)"]
        name.char_race_abilities["Spell Ability"] = "Once per day: Dancing Lights, Faerie Fire, Darkness 5\' Radius"
        name.char_race_abilities["Racial Light Penalties"] = "Avoid light or suffer -2 Dex, -2 To hit and +2 to be hit penalties, and loss of surprise"
    elif name.char_race == "GrayElf":
        name.char_abilities["DEX"] += 1
        name.char_abilities["INT"] += 1
        name.char_abilities["CON"] -= 1
        name.char_race_abilities["Sleep/Charm Resistance"] = "90%"
        name.char_race_abilities["Combat Bonus"] = "Short/Long Swords +1 To Hit, Bows +1 To Hit"
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Hobgoblin", "Orcish",
                                              "Gnoll", "Common", elflang, "Alignment"]
        name.char_race_abilities["Elven Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        name.char_race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)", "Secret: d6, Score 1-2 (Detect: 1-3)"]
    elif name.char_race == "ValleyElf":
        name.char_abilities["DEX"] += 1
        name.char_abilities["INT"] += 1
        name.char_abilities["CON"] -= 1
        name.char_race_abilities["Sleep/Charm Resistance"] = "90%"
        name.char_race_abilities["Combat Bonus"] = "Short/Long Swords +1 To Hit, Bows +1 To Hit"
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Hobgoblin", "Orcish",
                                              "Gnoll", "Common", elflang, "Alignment"]
        name.char_race_abilities["Elven Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        name.char_race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)", "Secret: d6, Score 1-2 (Detect: 1-3)"]
    elif name.char_race == "WoodElf":
        name.char_abilities["DEX"] += 1
        name.char_abilities["INT"] -= 1
        name.char_abilities["CON"] -= 1
        name.char_abilities["STR"] += 1
        name.char_race_abilities["Sleep/Charm Resistance"] = "90%"
        name.char_race_abilities["Combat Bonus"] = "Short/Long Swords +1 To Hit, Bows +1 To Hit"
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Racial Languages"] = ["Elvish", "Common", "Woodland Creature"]
        name.char_race_abilities["Elven Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        name.char_race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)", "Secret: d6, Score 1-2 (Detect: 1-3)"]
    elif name.char_race == "WildElf":
        name.char_abilities["DEX"] += 1
        name.char_abilities["CON"] -= 1
        name.char_abilities["STR"] += 2
        name.char_race_abilities["Sleep/Charm Resistance"] = "90%"
        name.char_race_abilities["Combat Bonus"] = "Short/Long Swords +1 To Hit, Bows +1 To Hit"
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Racial Languages"] = ["Elvish", "Common"]
        name.char_race_abilities["Elven Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        name.char_race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)", "Secret: d6, Score 1-2 (Detect: 1-3)"]
        name.char_race_abilities["Set Woodland Trap"] = "90% to set snares and natural traps"
    elif name.char_race == "Dwarf":
        name.char_abilities["CON"] += 1
        name.char_abilities["CHA"] -= 1
        name.char_race_abilities["Save Bonus"]["Rods, Staves, Wands"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Save Bonus"]["Poison"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Save Bonus"]["Spells"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Detect Grade Underground"] = "d4, score 1-3"
        name.char_race_abilities["Detect New Construction Underground"] = "d4, score 1-3"
        name.char_race_abilities["Detect Sliding/Shifting Construction Underground"] = "d6, score 1-4"
        name.char_race_abilities["Detect Stone Trapwork"] = "d4, score 1-2"
        name.char_race_abilities["Detect Depth Underground"] = "d4, score 1-2"
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Racial Languages"] = ["Dwarven", "Gnome", "Goblin", "Kobold", "Orcish", "Common", "Alignment"]
        name.char_race_abilities["Combat Bonus"] = ["+1 To hit: Half-Orc, Goblin, Hobgoblin, Orc",
                                          "-4 Penalty to be hit by Enemy Giants, Titans, Ogres or, Trolls"]
    elif name.char_race == "GrayDwarf":
        name.char_abilities["CON"] += 1
        name.char_abilities["CHA"] -= 1
        name.char_race_abilities["Save Bonus"]["Rods, Staves, Wands"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Save Bonus"]["Poison"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Save Bonus"]["Spells"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Detect Grade Underground"] = "d4, score 1-3"
        name.char_race_abilities["Immunity"] = "Immune to Paralyzation, Illusions and non-natural Poisons"
        name.char_race_abilities["Detect New Construction Underground"] = "d4, score 1-3"
        name.char_race_abilities["Detect Sliding/Shifting Construction Underground"] = "d6, score 1-4"
        name.char_race_abilities["Detect Stone Trapwork"] = "d4, score 1-2"
        name.char_race_abilities["Detect Depth Underground"] = "d4, score 1-2"
        name.char_race_abilities["Infravision"] = "12\""
        name.char_race_abilities["Racial Languages"] = ["Dwarven", "Undercommon", "Common", "+2 MAX More Regardless of Int."]
        name.char_race_abilities["Combat Bonus"] = "-4 Penalty to be hit by Enemy Giants, Titans, Ogres or, Trolls"
        name.char_race_abilities["Dueargar Movement"] = "3-6 (d6) to Surprise (If alone or with similar), only surprised 1in d10"
        name.char_race_abilities[
            "Racial Light Penalties"] = "Avoid light or suffer -2 Dex, -2 To hit and +2 to be hit penalties, and loss of surprise"
    elif name.char_race == "Half-Orc":
        name.char_abilities["STR"] += 1
        name.char_abilities["CON"] += 1
        name.char_abilities["CHA"] -= 2
        name.char_race_abilities["Racial Languages"] = ["Orcish", "Common", "Alignment"]
        name.char_race_abilities["Infravision"] = "60'"
    elif name.char_race == "Halfling":
        name.char_abilities["STR"] -= 1
        name.char_abilities["DEX"] += 1
        name.char_race_abilities["Save Bonus"]["Poison"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Save Bonus"]["Spells"] = str('+')+str(str(round(name.char_abilities["CON"] / 3.5))[0])
        name.char_race_abilities["Save Bonus"]["Rods, Staves, Wands"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Infravision"] = "30' (Or 60' if Stoutish)"
        name.char_race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Dwarven", "Orcish",
                                              "Common", "Alignment", "+{} more".format(name.char_abilities["INT"]-16)]
        name.char_race_abilities["Halfling Surprise"] = ["d4, 1-4 in Non-Metal Armor and Alone or w/ Elves/Halflings, Score 1-2 if opening door "]
        name.char_race_abilities["Detect Grade Underground"] = "d4, score 1-3"
        name.char_race_abilities["Determine Direction Underground"] = "d10, score 1-5"
    elif name.char_race == "Gnome":
        name.char_race_abilities["Save Bonus"]["Rods, Staves, Wands:"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Save Bonus"]["Spells:"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Racial Languages"] = ["Dwarven", "Gnome", "Goblin", "Kobold", "Orcish", "Common",
                                              "Burrowing Mammal", "Alignment"]
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Detect Grade Underground"] = "d10, score 1-8"
        name.char_race_abilities["Detect Unsafe Walls/Ceilings/Floors"] = "d10, score 1-7"
        name.char_race_abilities["Detect Depth Underground"] = "d10, score 1-6"
        name.char_race_abilities["Determine Direction Underground"] = "d10, score 1-5"
        name.char_race_abilities["Combat Bonus"] = ["+1 Kobolds, Goblions",
                                          "-4 To Be hit by, Gnolls, Trolls, Giants, Bugbears, Giants, Titans"]
    elif name.char_race == "DeepGnome":
        name.char_race_abilities["Save Bonus"]["Rods, Staves, Wands:"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["Save Bonus"]["Spells:"] = str('+')+str(int(str(round(name.char_abilities["CON"] / 3.5))[0]))
        name.char_race_abilities["DG Save Bonus"] = "+2 vs. Poison, +3 vs. all other Saves"
        name.char_race_abilities["Immunity"] = "Immune to Illusions and Phantasms"
        name.char_race_abilities["Racial Languages"] = ["Deep Gnome"]
        name.char_race_abilities["Infravision"] = "12\""
        name.char_race_abilities["Ultravision"] = "3\""
        name.char_race_abilities["Detect Grade Underground"] = "d10, score 1-8"
        name.char_race_abilities["Detect Unsafe Walls/Ceilings/Floors"] = "d10, score 1-7"
        name.char_race_abilities["Detect Depth Underground"] = "d10, score 1-6"
        name.char_race_abilities["Determine Direction Underground"] = "d10, score 1-5"
        name.char_race_abilities["Combat Bonus"] = ["+1 Kobolds, Goblions",
                                          "-4 To Be hit by, Gnolls, Trolls, Giants, Bugbears, Giants, Titans, Ogres/Magi"]
        name.char_race_abilities[
            "Svirfneblin Movement"] = "1-9 (d10) to Surprise (If alone or with similar), only surprised 1in d12"
        name.char_race_abilities["Racial Light Penalties"] = "Reduce vision to 3\" and -1 to hit"
    elif name.char_race == "Half-Elf":
        name.char_race_abilities["Sleep/Charm Resistance"] = "30%"
        name.char_race_abilities["Racial Languages"] = ["Elvish", "Gnome", "Halfling", "Goblin", "Hobgoblin", "Orcish",
                                              "Gnoll", "Common", "Alignment", "+{} more".format(name.char_abilities["INT"] - 16)]
        name.char_race_abilities["Infravision"] = "60'"
        name.char_race_abilities["Detect Secret Doors"] = ["Concealed: d6, Score 1 (Detect: 1-2)",
                                                 "Secret: d6, Score 1-2 (Detect: 1-3)"]
    else:
        name.char_race_abilities["Racial Languages"] = ["Common", "Alignment"]
    fighters = ["Fighter", "Barbarian", "Cavalier", "Paladin", "UAPaladin", "Ranger"]
    if name.char_abilities["STR"] == 18:
        for c in name.char_class:
            if str(c) in fighters:
                name.char_abilities["EX_STR"] = dice.exceptional_strength(name)

    return name
