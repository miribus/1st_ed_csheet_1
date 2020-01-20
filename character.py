import dice, char_races, char_classes, social_class, base_ability_detail, age, class_abilities
import alignments, os, item_shop, encumbrance, armor_class, psionic_check
import char_to_xls
#import re

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class playerSheet:
    def __init__(self, charname):
        global methodv, abilities, methodv_choice
        self.self_roll = False
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
        self.psionic = False
        self.methodv = methodv
        self.methodv_choice = methodv_choice
        self.char_alignment = ""
        self.char_name = charname
        self.player_name = ""
        self.char_age = ""
        self.char_age_desc = ""
        self.char_class = []
        self.char_class_levels = []
        self.char_class_nextXP = []
        self.char_class_name = []
        self.char_class_xpBonus = []
        self.char_class_abilities = {}
        self.char_weapon_prof_slots = 0
        self.char_weapon_prof_penalty = -6
        self.char_weapon_prof = []
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
        self.char_AC = {"AC":10, "Shieldless":10, "Rear":10, "Surprised":10, "Naked":10}
        self.char_saves = {}
        self.char_saves["Poison"] = 21
        self.char_saves["Petrification"] = 21
        self.char_saves["Rods, Staves, Wands"] = 21
        self.char_saves["Breath Weapon"] = 21
        self.char_saves["Spells"] = 21
        self.char_armor = {}
        self.char_shield = {}
        self.char_melee_weapons = {}
        self.char_ranged_weapons = {}
        self.char_inventory = {}
        self.char_encumbrance = {}
        self.char_movement_rate = {}
        #self.char_adjustments = {}
        self.char_race_abilities = {}
        self.soclass_limit = []
        self.social_class = ""
        self.char_money = {}
        self.char_money["pp"] = 0
        self.char_money["gp"] = 0
        self.char_money["ep"] = 0
        self.char_money["sp"] = 0
        self.char_money["cp"] = 0

methodv = False
method = False
while not method:
    print(" 1 *Human-Only* Choose Class: Method V\n",
          "2 Random: DMG Method III\n",
          "3 Enter Your own\n"
          )
    choice = input("Choose a Number>")
    if choice != "1" and choice != "2" and choice != "3":
        method = False
    else:
        method = True
if method:
    if int(choice) == 1:
        abilities, methodv_choice = dice.unearthed()
        methodv = True
    else:
        methodv_choice = False

#clear screen
clear_screen()

name = playerSheet(input("Character Name?:"))
if int(choice) == 3:
    name.self_roll = True
    possible = [str(n) for n in range(3, 19)]
    possible.append("False")
    for a in name.char_abilities:
        abil = "00"
        while str(abil) not in possible:
            if str(a) == "EX_STR":
                abil = False
            else:
                abil = input("Type your {} roll:".format(a))
        name.char_abilities[a] = int(abil)

print(name.char_abilities)
name = social_class.social_class(name)
result = False
while not result:
    print("Choose a race:\n",
          "0 Dwarf\n",
          "1 GrayDwarf\n",
          "2 Elf\n",
          "3 GrayElf\n",
          "4 WoodElf\n",
          "5 WildElf\n",
          "6 ValleyElf\n",
          "7 DarkElf\n",
          "8 Gnome\n",
          "9 Deep Gnome\n",
          "10 Half-Elf\n",
          "11 Half-Orc\n",
          "12 Human\n",
          "13 Halfling\n")
    if name.methodv:
        print("You chose method V, you must be human.")
        name, result = char_races.races_base("12", name)
    else:
        name, result = char_races.races_base(input("Choose Race:"), name)
clear_screen()

if result:
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
    name = class_abilities.starting_money(name)
    result = False
    while not result:
        clear_screen()
        print("****PROFICIENCIES*******")
        name, result = class_abilities.weapon_prof(name)
        print(name.char_weapon_prof)
        print("***********")
    print("*****ITEM SHOP******\n")
    print("\n")
    if "Cavalier" in name.char_class or "UAPaladin" in name.char_class:
        name = item_shop.cavalier_start(name)
    result = False
    while not result:
        clear_screen()
        name, result = item_shop.buy_weapons(name)
    result = False
    while not result:
        clear_screen()
        name, result = item_shop.buy_armor(name)
    result = False
    while not result:
        clear_screen()
        name, result = item_shop.buy_provisions(name)
    print("*****LEAVE ITEM SHOP******\n")
    name = class_abilities.calculate_combat_bonuses(name)
    name = armor_class.calculate_armor_class(name)
clear_screen()
print("******CHARACTER SHEET*********")
print("\n")
print("Character Name: ", name.char_name)
print("Class(es): ", name.char_class, name.char_class_name)
print(name.char_class_levels)
print(name.char_class_nextXP)
print("Alignment: ", name.char_alignment)
print("Race: ", name.char_race)
print("Age: ", name.char_age, name.char_age_desc)
print("Social Class:", name.social_class)
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
print("Money:")
print(name.char_money)
print("Race Abilities:")
for a in name.char_race_abilities:
    print(a, name.char_race_abilities[a])
print("***********")
print("Class Abilities:")
for c in name.char_class_abilities:
    for a in name.char_class_abilities[c]:
        print(a,  name.char_class_abilities[c][a])
print("-------------")
print(name.char_armor)
print(name.char_shield)
for w in name.char_melee_weapons:
    print(w, name.char_melee_weapons[w])
for w in name.char_ranged_weapons:
    print("RANGED", w, name.char_ranged_weapons[w])
for i in name.char_inventory:
    print("Inventory:", i, name.char_inventory[i])
print("#$#$#$#$#$#$#$#$")
name = encumbrance.calculate_encumbrance(name)
print(name.char_movement_rate)
print(name.char_encumbrance)
print(name.char_weapon_prof)
print(name.char_AC)

char_to_xls.character_print(name)
name = psionic_check.psionic_check(name)

quitout = input("Enter to quit")


