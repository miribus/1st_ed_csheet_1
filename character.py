import dice, saving_throws, char_races

class playerSheet:
    def __init__(self, charname):

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
race = char_races.

#name.char_saves = saving_throws.class_saves("thi")
#print(name.char_saves)
