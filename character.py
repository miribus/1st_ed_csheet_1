import dice, saving_throws, char_races, char_classes, social_class

class playerSheet:
    def __init__(self, charname):

        if len(charname) == 0:
            charname = "Trololo"
        self.char_name = charname
        self.char_social_class = ""
        self.player_name = "todd"
        self.char_class = []
        self.char_race = ""
        self.char_gender = ""
        self.char_abilities = {"STR": dice.ability_roller(6, 5),
                               "INT": dice.ability_roller(6, 5),
                               "WIS": dice.ability_roller(6, 5),
                               "DEX": dice.ability_roller(6, 5),
                               "CON": dice.ability_roller(6, 5),
                               "CHA": dice.ability_roller(6, 5),
                               "CMS": dice.ability_roller(6, 3)}
        self.char_HP = 0
        self.char_AC = {"Base AC:":10, "Shield AC:":0, "Rear AC:":0}
        self.char_saves = {}
        self.char_saves["Poison"] = 21
        self.char_saves["Petrification"] = 21
        self.char_saves["Rods, Staves, Wands"] = 21
        self.char_saves["Breath Weapon"] = 21
        self.char_saves["Spells"] = 21
        self.char_armor = ""
        self.char_shield = ""
        self.char_inventory = {}
        self.char_adjustments = {}
        self.char_race_abilities = {}

name = playerSheet(input("Character Name?:"))
print(name.char_abilities)
name.char_social_class, soclass_limit =  social_class.social_class()
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
decision = input("Agreed? Y/N:")

if decision.isalpha():
    if "y".upper() == decision.upper():
        result = result
        name.char_race = race
        name.char_gender = gender
        race_class_choices = char_classes.race_class_choices
        result = False
        while not result:
            name.char_class, result = char_classes.race_classes(name.char_abilities, name.char_race,
                                                            race_class_choices, soclass_limit)
        name.char_saves = char_classes.class_saving_throws(name.char_class, name.char_saves)
        name.char_race_abilities, name.char_race_abilities = char_races.base_bonuses(
            name.char_abilities, name.char_race, name.char_class
            )
print(name.char_race)
print(name.char_social_class)
print(name.char_abilities)
print(name.char_class)
print(name.char_saves)
#print(name.char_race_abilities)
for a in name.char_race_abilities:
    print(a, name.char_race_abilities[a])