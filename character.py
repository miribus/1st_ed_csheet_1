import dice, saving_throws, char_races

class playerSheet:
    def __init__(self, charname):

        if len(charname) == 0:
            charname = "Trololo"
        self.char_name = charname
        self.player_name = "todd"
        self.char_class = {"Class 1:":0}
        self.char_race = ""
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
        self.char_inventory = []
        self.char_adjustments = []

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
          " ]")
    race = char_races.races_base(input("Choose Race:"), name.char_abilities)
    decision = input("Agreed? Y/N:")
    if "y".upper() == decision.upper():
        result = race


#name.char_saves = saving_throws.class_saves("thi")
#print(name.char_saves)
