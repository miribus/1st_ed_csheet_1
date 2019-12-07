import dice, saving_throws, char_races

class playerSheet:
    def __init__(self, charname):

        if len(charname) == 0:
            charname = "Trololo"
        self.char_name = charname
        self.player_name = "todd"
        self.char_class = []
        self.char_race = ""
        self.char_gender = ""
        self.char_abilities = {"STR": dice.ability_roller(6, 5),
                               "INT": dice.ability_roller(6, 5),
                               "WIS": dice.ability_roller(6, 5),
                               "DEX": dice.ability_roller(6, 5),
                               "CON": dice.ability_roller(6, 5),
                               "CHA": dice.ability_roller(6, 5)}
        self.char_HP = 0
        self.char_AC = {"Base AC:":10, "Shield AC:":0, "Rear AC:":0}
        self.char_saves = ""
        self.char_armor = ""
        self.char_shield = ""
        self.char_inventory = {}
        self.char_adjustments = {}
        self.char_race_abilities = {}

name = playerSheet(input("Character Name?:"))
print(name.char_abilities)
result = False
while not result:
    print("Choose a race:",
          "[ ",
          "0 Dwarf",
          "1 Elf",
          "2 Gnome",
          "3 Half-Elf",
          "4 Half-Orc",
          "5 Human",
          "6 Halfling",
          " ]")
    race, result, gender = char_races.races_base(input("Choose Race:"), name.char_abilities)
    if not result:
        result = False
    else:
        decision = input("Agreed? Y/N:")
        if "y".upper() == decision.upper():
            result = result
            name.char_race = race
            name.char_gender = gender
            race_class_choices = char_races.race_class_choices
            name.char_class = char_races.race_classes(name.char_abilities, name.char_race, race_class_choices)
print(name.char_race)
print(name.char_abilities)
print(name.char_class)

#name.char_saves = saving_throws.class_saves("thi")
#print(name.char_saves)
