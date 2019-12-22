import dice, char_races, char_classes, social_class, base_ability_detail, age, class_abilities
import alignments, os
#import re

class playerSheet:
    def __init__(self, charname):
        global methodv, abilities, methodv_choice
        if methodv:
            self.char_abilities = abilities
        else:
            self.char_abilities = {"STR": dice.ability_roller(6, 5),
                                   "INT": dice.ability_roller(6, 5),
                                   "WIS": dice.ability_roller(6, 5),
                                   "DEX": dice.ability_roller(6, 5),
                                   "CON": dice.ability_roller(6, 5),
                                   "CHA": dice.ability_roller(6, 5),
                                   "CMS": dice.ability_roller(6, 3),
                                   "EX_STR": False}
        if len(charname) == 0:
            charname = "Trololo"
        elif charname == "Wreck":
            self.char_abilities = {"STR": 18,
                                   "INT": 18,
                                   "WIS": 18,
                                   "DEX": 18,
                                   "CON": 18,
                                   "CHA": 18,
                                   "CMS": 18,
                                   "EX_STR": False}
        self.methodv = methodv
        self.methodv_choice = methodv_choice
        self.char_alignment = ""
        self.char_name = charname
        self.char_social_class = ""
        self.player_name = ""
        self.char_age = ""
        self.char_age_desc = ""
        self.char_class = []
        self.char_class_levels = []
        self.char_class_xpBonus = []
        self.char_class_abilities = {}
        self.char_race = ""
        self.char_gender = ""
        self.char_define_abilities = {}
        self.char_define_abilities["STR"] = {}
        self.char_define_abilities["INT"] = {}
        self.char_define_abilities["WIS"] = {}
        self.char_define_abilities["DEX"] = {}
        self.char_define_abilities["CON"] = {}
        self.char_define_abilities["CHA"] = {}
        self.char_define_abilities["CMS"] = {}
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
        self.soclass_limit = []
        self.social_class = ""

methodv = False
method = False
while not method:
    print("1 Human-Only Choose Class: Method V\n",
          "2 Random: DMG Method III\n",
          )
    choice = input("Choose a Number>")
    if choice != "1" and choice != "2":
        method = False
    else:
        method = True
if method:
    if int(choice) == 1:
        abilities, methodv_choice = dice.unearthed()
        methodv = True
    else:
        methodv_choice = False

name = playerSheet(input("Character Name?:"))
print(name.char_abilities)
name = social_class.social_class(name)
result = False
while not result:
    print("Choose a race:\n",
          "0 Dwarf\n",
          "1 Elf\n",
          "2 Gnome\n",
          "3 Half-Elf\n",
          "4 Half-Orc\n",
          "5 Human\n",
          "6 Halfling\n")
    if name.methodv:
        print("You chose method V, you must be human.")
        name, result = char_races.races_base("5", name)
    else:
        name, result = char_races.races_base(input("Choose Race:"), name)
decision = input("Agreed? Y/N:")

if decision.isalpha():
    if "y".upper() == decision.upper():
        result = False

        while not result:
            name, result = char_classes.race_classes(name)
        name = char_classes.class_saving_throws(name)
        name = char_races.base_bonuses(name)
        name = age.age(name)
        name = char_races.race_ability_updater(name)
        name = base_ability_detail.define_abilities(name)
        name = class_abilities.class_details(name)
        name = alignments.choose_alignment(name)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("*********************************")
print("\n")
print("Character Name: ", name.char_name)
print("Class(es): ", name.char_class)
print("Alignment: ", name.char_alignment)
print("Race: ", name.char_race)
print("Age: ", name.char_age, name.char_age_desc)
print("Social Class:", name.char_social_class)
print("HP: ", name.char_HP)
print(name.char_saves)
print("Strength:", name.char_abilities["STR"])
if name.char_abilities['EX_STR']:
    print("Exceptional Strength:", name.char_abilities['EX_STR'])
print(name.char_define_abilities["STR"])
print("##########")
print("Intelligence:", name.char_abilities["INT"])
print(name.char_define_abilities["INT"])
print("##########")
print("Wisdom:", name.char_abilities["WIS"])
print(name.char_define_abilities["WIS"])
print("##########")
print("Dexterity;", name.char_abilities["DEX"])
print(name.char_define_abilities["DEX"])
print("##########")
print("Constitution", name.char_abilities["CON"])
print(name.char_define_abilities["CON"])
print("##########")
print("Charisma:", name.char_abilities["CHA"])
print(name.char_define_abilities["CHA"])
print("##########")
print("Comeliness:", name.char_abilities["CMS"])
print(name.char_define_abilities["CMS"])
print("##########")
print("\n")
print("Race Abilities:")
for a in name.char_race_abilities:
    print(a, name.char_race_abilities[a])
print("***********")
print("Class Abilities:")
for c in name.char_class_abilities:
    for a in name.char_class_abilities[c]:
        print(a,  name.char_class_abilities[c][a])
print("-------------")
quitout = input("Enter to quit")
tables = str(os.getcwd()+"\\tables\\")
print(os.listdir(tables))
print("***********")


