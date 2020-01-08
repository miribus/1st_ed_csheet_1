import dice, csv, os

tables = str(os.getcwd()+"\\tables\\")
weapons_csv = tables+"weapons_csv.csv"
#

with open(weapons_csv, 'r') as WCSV:
    wcsv_write = csv.reader(WCSV, delimiter = ",")
    weapons_list = list(wcsv_write)

def fighter_check(name):
    fighter = False
    if "Fighter" in name.char_class or "Ranger" in name.char_class:
        if len(name.char_class) == 1:
            fighter = True
    return fighter

def class_details(name):
    for c in name.char_class:
        if "Cleric" == str(c):
            if not name.char_weapon_prof_slots > 2:
                name.char_weapon_prof_slots = 2
            if not name.char_weapon_prof_penalty > -3:
                name.char_weapon_prof_penalty = -3
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("1500")
            name.char_class_name = "Acolyte"
            if name.char_abilities["WIS"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            if "Cleric" not in name.char_class_abilities:
                name.char_class_abilities["Cleric"] = {}
                name.char_class_abilities["Cleric"]["Turn Undead"] = {}
            name.char_class_abilities["Cleric"]["Turn Undead"]["Skeleton"] = "10"
            name.char_class_abilities["Cleric"]["Turn Undead"]["Zombie"] = "13"
            name.char_class_abilities["Cleric"]["Turn Undead"]["Ghoul"] = "16"
            name.char_class_abilities["Cleric"]["Turn Undead"]["Shadow"] = "19"
            name.char_class_abilities["Cleric"]["Turn Undead"]["Wight"] = "20"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(8, 1, name, 5)+int(HPadj)
            name.char_HP += HP

        elif "Druid" == str(c):
            name.char_race_abilities["Racial Languages"].append("Druidic")
            if not name.char_weapon_prof_slots > 2:
                name.char_weapon_prof_slots = 2
            if not name.char_weapon_prof_penalty > -4:
                name.char_weapon_prof_penalty = -4
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("2000")
            name.char_class_name = "Aspirant"
            if name.char_abilities["WIS"] > 15 and name.char_abilities["CHA"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(8, 1, name, 5)+int(HPadj)
            name.char_HP += HP

        elif "Fighter" == str(c):
            if not name.char_weapon_prof_slots > 4:
                name.char_weapon_prof_slots = 4
            if not name.char_weapon_prof_penalty > -2:
                name.char_weapon_prof_penalty = -2
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("2000")
            name.char_class_name = "Veteran"
            if name.char_abilities["STR"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            if "Fighter" not in name.char_class_abilities:
                name.char_class_abilities["Fighter"] = {}
                if len(name.char_class) == 1:
                    name.char_class_abilities["Fighter"]["Specialization (UA) 1"] = "2x WP Slots for Spec, 3x WP Slots for Double Spec;" \
                                                                             "+1/+2 (Single) +3/+3 (Double Spec: no missile, polearm," \
                                                                             "or 2h sword). Damage Bonus only at \'point blank\' range"
                    name.char_class_abilities["Fighter"]["Specialization (UA) 2"] = "Atk/Rnd: Melee: 3/2, Bow: 2/1, LxB: 1/1, " \
                                                                            "HxB: 1/2, Lasso/SSling: 1/1, Thrown Dagger: 3/1, " \
                                                                            "Thrown Dart: 4/1, Other: 3/2"
            name.char_class_abilities["Fighter"]["Superior Fighting"] = "1/Level attack per creatures less than 1HD"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(10, 1, name, 6)+int(HPadj)
            name.char_HP += HP
        elif "Paladin" == str(c) and "UAPaladin" not in str(c):
            if not name.char_weapon_prof_slots > 3:
                name.char_weapon_prof_slots = 3
            if not name.char_weapon_prof_penalty > -3:
                name.char_weapon_prof_penalty = -3
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("2750")
            name.char_class_name = "Gallant"
            if name.char_abilities["STR"] > 15 and name.char_abilities["WIS"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            if "Paladin" not in name.char_class_abilities:
                name.char_class_abilities["Paladin"] = {}
                name.char_class_abilities["Paladin"]["Special"] = {}
                name.char_class_abilities["Paladin"]["Save Bonus"] = ""
                name.char_class_abilities["Paladin"]["Immunity"] = "Disease, Fear"
            name.char_class_abilities["Paladin"]["Save Bonus"] = "+2 all Saving Throws"
            name.char_class_abilities["Paladin"]["Special"]["Lay on Hands"] = "+2 per level/day"
            name.char_class_abilities["Paladin"]["Special"]["Cure Disease"] = "1/wk per 5 levels"
            name.char_class_abilities["Paladin"]["Special"]["Protection from Evil"] = '1\" radius all 24/7'
            name.char_class_abilities["Paladin"]["Superior Fighting"] = "1/Level attack per creatures less than 1HD"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(10, 1, name, 6)+int(HPadj)
            name.char_HP += HP
        elif "Ranger" == str(c):
            if not name.char_weapon_prof_slots > 3:
                name.char_weapon_prof_slots = 3
            if not name.char_weapon_prof_penalty > -2:
                name.char_weapon_prof_penalty = -2
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("2250")
            name.char_class_name = "Runner"
            if name.char_abilities["STR"] > 15 and name.char_abilities["WIS"] > 15 and name.char_abilities["INT"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            if "Ranger" not in name.char_class_abilities:
                name.char_class_abilities["Ranger"] = {}
                name.char_class_abilities["Ranger"]["Special"] = {}
            name.char_class_abilities["Ranger"]["Combat Bonus"] = "+1 Dmg/Lvl against: Bugbear, Ettin, Giant,"\
                                                                  "Gnoll, Goblin, Hobgoblin, Kobold, Ogre,"\
                                                                  "Ogre Magi, Orc, Troll"

            name.char_class_abilities["Ranger"]["Surprise"] = "1-3/d6 Surprise if alone, w/Elves." \
                                                              " 1/d6 to be Surprised if alone, w/Elves"
            name.char_class_abilities["Ranger"]["Special"]["Tracking"] = "Tracking Unearthed Arcana Pg: 21"
            if len(name.char_class) == 1:
                name.char_class_abilities["Ranger"][
                    "Specialization (UA) 1"] = "2x WP Slots for Spec, 3x WP Slots for Double Spec;" \
                                                                         "+1/+2 (Single) +3/+3 (Double Spec: no missile, polearm," \
                                                                         "or 2h sword). Damage Bonus only at \'point blank\' range"
                name.char_class_abilities["Ranger"]["Specialization (UA) 2"] = "Atk/Rnd: Melee: 3/2, Bow: 2/1, LxB: 1/1, " \
                                                                                "HxB: 1/2, Lasso/SSling: 1/1, Thrown Dagger: 3/1, " \
                                                                                "Thrown Dart: 4/1, Other: 3/2"
            name.char_class_abilities["Ranger"]["Superior Fighting"] = "1/Level attack per creatures less than 1HD"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(8, 2, name, 9) + int(HPadj) + int(HPadj)
            name.char_HP += HP
        elif "MagicUser" == str(c):
            if not name.char_weapon_prof_slots > 1:
                name.char_weapon_prof_slots = 1
            if not name.char_weapon_prof_penalty > -5:
                name.char_weapon_prof_penalty = -5
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("2500")
            name.char_class_name = "Prestidigitator"
            if name.char_abilities["INT"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(4, 1, name, 3) + int(HPadj)
            name.char_HP += HP
        elif "Illusionist" == str(c):
            if not name.char_weapon_prof_penalty > -5:
                name.char_weapon_prof_penalty = -5
            if not name.char_weapon_prof_slots > 1:
                name.char_weapon_prof_slots = 1
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("2250")
            name.char_class_name = "Prestidigitator"
            name.char_class_xpBonus.append("0%")
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(4, 1, name, 3) + int(HPadj)
            name.char_HP += HP
        elif "Thief" == str(c):
            name.char_race_abilities["Racial Languages"].append("Thief Cant")
            if not name.char_weapon_prof_slots > 2:
                name.char_weapon_prof_slots = 2
            if not name.char_weapon_prof_penalty > -3:
                name.char_weapon_prof_penalty = -3
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("1250")
            name.char_class_name = "Rogue"
            if name.char_abilities["DEX"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            if "Thief" not in name.char_class_abilities:
                name.char_class_abilities["Thief"] = {}
            pick_pockets = ["30%", name.char_race_abilities["Thief"]["Pick Pockets"], name.char_define_abilities["DEX"]["Pick Pockets"]]
            pick_pockets = [p.replace("%", "") for p in pick_pockets]
            pick_pockets = int(pick_pockets[0]) + int(pick_pockets[1]) + int(pick_pockets[2])
            name.char_class_abilities["Thief"]["Pick Pockets"] = str(pick_pockets)+"%"

            open_locks = ["25%",name.char_race_abilities["Thief"]["Open Locks"],name.char_define_abilities["DEX"]["Open Locks"]]
            open_locks = [p.replace("%", "") for p in open_locks]
            open_locks = int(open_locks[0]) + int(open_locks[1]) + int(open_locks[2])
            name.char_class_abilities["Thief"]["Open Locks"] = str(open_locks)+"%"

            find_traps = ["20%", name.char_race_abilities["Thief"]["Find/Remove Traps"],
                                                                       name.char_define_abilities["DEX"]["Find/Remove Traps"]]
            find_traps = [p.replace("%", "") for p in find_traps]
            find_traps = int(find_traps[0]) + int(find_traps[1]) + int(find_traps[2])
            name.char_class_abilities["Thief"]["Find/Remove Traps"] = str(find_traps)+"%"

            move_silent = ["15%",name.char_race_abilities["Thief"]["Move Silent"],
                                                                 name.char_define_abilities["DEX"]["Move Silent"]]
            move_silent = [p.replace("%", "") for p in move_silent]
            move_silent = int(move_silent[0]) + int(move_silent[1]) + int(move_silent[2])
            name.char_class_abilities["Thief"]["Move Silent"] = str(move_silent)+"%"

            hide_shadows = ["10%", name.char_race_abilities["Thief"]["Hide In Shadows"],name.char_define_abilities["DEX"]["Hide In Shadows"]]
            hide_shadows = [p.replace("%", "") for p in hide_shadows]
            hide_shadows = int(hide_shadows[0]) + int(hide_shadows[1]) + int(hide_shadows[2])
            name.char_class_abilities["Thief"]["Hide In Shadows"] = str(hide_shadows) + "%"

            hear_noise = ["10%",name.char_race_abilities["Thief"]["Hear Noise"],"0%"]
            hear_noise = [p.replace("%", "") for p in hear_noise]
            hear_noise = int(hear_noise[0]) + int(hear_noise[1]) + int(hear_noise[2])
            name.char_class_abilities["Thief"]["Hear Noise"] = str(hear_noise)+"%"

            climb_walls = ["85%",name.char_race_abilities["Thief"]["Climb Walls"],"0%"]
            climb_walls = [p.replace("%", "") for p in climb_walls]
            climb_walls = int(climb_walls[0]) + int(climb_walls[1]) + int(climb_walls[2])
            name.char_class_abilities["Thief"]["Climb Walls"] = str(climb_walls)+"%"

            read_languages = ["0%",name.char_race_abilities["Thief"]["Read Languages"],"0%"]
            read_languages = [p.replace("%", "") for p in read_languages]
            read_languages = int(read_languages[0]) + int(read_languages[1]) + int(read_languages[2])
            name.char_class_abilities["Thief"]["Read Languages"] = str(read_languages)+"%"

            name.char_class_abilities["Thief"]["Backstab"] = "2x Damage / 3 levels with one-handed Club, Dagger/Knife or Sword"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(6, 1, name, 4) + int(HPadj)
            name.char_HP += HP
        elif "Assassin" == str(c):
            if not name.char_weapon_prof_slots > 3:
                name.char_weapon_prof_slots = 3
            if not name.char_weapon_prof_penalty > -2:
                name.char_weapon_prof_penalty = -2
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("1500")
            name.char_class_name = "Apprentice"
            name.char_class_xpBonus.append("0%")
            if "Assassin" not in name.char_class_abilities:
                name.char_class_abilities["Assassin"] = {}
            name.char_class_abilities["Assassin"]["Assassinate"] = ["~50% to Assassinate: Victim 0L: 50gp, Victim 1-2L: "
                                                                    "100gp, Victim 3-4L: 150gp, Victim 5-6L: 200gp, "
                                                                    "Victim 7-9L: 250gp"]
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(6, 1, name, 4) + int(HPadj)
            name.char_HP += HP
        elif "Monk" == str(c):
            if not name.char_weapon_prof_slots > 1:
                name.char_weapon_prof_slots = 1
            if not name.char_weapon_prof_penalty > -3:
                name.char_weapon_prof_penalty = -3
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("2250")
            name.char_class_name = "Novice"
            name.char_class_xpBonus.append("0%")
            if "Monk" not in name.char_class_abilities:
                name.char_class_abilities["Monk"] = {}
                name.char_class_abilities["Monk"]["Thief"] = {}
            name.char_class_abilities["Monk"]["Defense"] = "No DEX Bonus for Defense (AC)"
            name.char_class_abilities["Monk"]["Combat"] = "+1/2 DMG per Level w/ Weapon"
            name.char_class_abilities["Monk"]["Combat"] = "Save vs. Petrification to avoid normal missiles"
            name.char_class_abilities["Monk"]["Magic"] = "Save vs. to avoid all damage in some cases"
            name.char_class_abilities["Monk"]["Breath Weapon"] = "Save vs. to avoid all damage in some cases"
            name.char_class_abilities["Monk"]["Thief"] = {}
            name.char_class_abilities["Monk"]["Thief"]["Open Locks"] = ["25%",
                                                                name.char_define_abilities["DEX"]["Open Locks"]]
            name.char_class_abilities["Monk"]["Thief"]["Find/Remove Traps"] = ["20%",
                                                                       name.char_define_abilities["DEX"]["Find/Remove Traps"]]
            name.char_class_abilities["Monk"]["Thief"]["Move Silent"] = ["15%",
                                                                 name.char_define_abilities["DEX"]["Move Silent"]]
            name.char_class_abilities["Monk"]["Thief"]["Hide In Shadows"] = ["10%",
                                                                     name.char_define_abilities["DEX"]["Hide In Shadows"]]
            name.char_class_abilities["Monk"]["Thief"]["Hear Noise"] = ["10%"]
            name.char_class_abilities["Monk"]["Thief"]["Climb Walls"] = ["85%"]
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(4, 2, name, 5) + int(HPadj) + int(HPadj)
            name.char_HP += HP
        elif "Cavalier" == str(c):
            if not name.char_weapon_prof_slots > 3:
                name.char_weapon_prof_slots = 3
            if not name.char_weapon_prof_penalty > -3:
                name.char_weapon_prof_penalty = -3
            if name.social_class not in ["LUC", "UUC", "MUC"]:
                name.char_class_levels.append("0")
                name.char_class_nextXP.append("-501")
                name.char_class_name = "Horseman"
            else:
                name.char_class_levels.append("1")
                name.char_class_nextXP.append("2750")
                name.char_class_name = "Armiger"
            name.char_class_xpBonus.append("0%")

            if "Cavalier" not in name.char_class_abilities:
                name.char_class_abilities["Cavalier"] = {}
                name.char_class_abilities["Cavalier"]["Save Bonus"] = ""

            name.char_class_abilities["Cavalier"]["Honor"] = ["Cannot run from combat", "Must wear metal armor", "Must adhere to code to gain XP",
                                                              "Must be proficient in lance, favors close range swords", "Elves or Half Elves may use composite"
                                                              " short bows with honor."]
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            if name.social_class in ["LUC", "MUC", "UUC"]:
                name.char_class_abilities["Cavalier"]["Superior Fighting"] = "1/Level attack per creatures less than 1HD"
                name.char_class_abilities["Cavalier"][
                    "Lance"] = "Lance Proficiency Required, +1 DMG per Lvl when Mounted," \
                               "+1 DMG when dismounted."
                name.char_class_abilities["Cavalier"][
                    "Parry"] = "Unearthed Arcana Pg 15, reduce Attacker To hit by your bonus"
                name.char_class_abilities["Cavalier"]["Immununity"] = "Fear"
                name.char_class_abilities["Cavalier"]["Horsemanship"] = "Attacks from Horseback as +1 Level (UA Pg 15)"
                name.char_class_abilities["Cavalier"][
                    "Horsemanship2"] = "-85% thrown from saddle, or injured +1% per level"
                name.char_class_abilities["Cavalier"][
                    "Horsemanship3"] = "+2HP per hit die for horse, determine best quality HP steed"
                name.char_class_abilities["Cavalier"]["Resistances"] = "Mind Affecting spells 90% failure"
                name.char_class_abilities["Cavalier"]["Good Aligned"] = "Radiate Protection from Fear 1\" radius"
                name.char_class_abilities["Cavalier"]["Save Bonus"] = "+2 Illusions"
                name.char_class_abilities["Cavalier"]["STR Training"] = dice.exceptional_strength(name)
                name.char_class_abilities["Cavalier"]["DEX Training"] = dice.exceptional_strength(name)
                name.char_class_abilities["Cavalier"]["CON Training"] = dice.exceptional_strength(name)
                HP = dice.HP(10, 1, name, 6) + int(HPadj) + 3
            else:
                HP = dice.HP(4, 1, name, 3) + int(HPadj) + 1
            name.char_HP += HP
        elif "UAPaladin" == str(c):
            if not name.char_weapon_prof_slots > 3:
                name.char_weapon_prof_slots = 3
            if not name.char_weapon_prof_penalty > -3:
                name.char_weapon_prof_penalty = -3
            if name.char_abilities["STR"] > 15 and name.char_abilities["WIS"] > 15:
                name.char_class_xpBonus.append("+10%")
            else:
                name.char_class_xpBonus.append("0%")
            if name.social_class not in ["LUC", "UUC", "MUC"]:
                name.char_class_levels.append("0")
                name.char_class_nextXP.append("-501")
                name.char_class_name = "Horseman"
            else:
                name.char_class_levels.append("1")
                name.char_class_nextXP.append("2750")
                name.char_class_name = "Gallant"
            if "UAPaladin" not in name.char_class_abilities:
                name.char_class_abilities["UAPaladin"] = {}
                name.char_class_abilities["UAPaladin"]["Special"] = {}
                name.char_class_abilities["UAPaladin"]["Save Bonus"] = []

            name.char_class_abilities["UAPaladin"]["Honor"] = ["Cannot run from combat", "Must wear metal armor",
                                                              "Must adhere to code to gain XP", "Must be proficient in "
                                                               "lance, favors close range swords"]
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            if name.social_class in ["LUC", "MUC", "UUC"]:
                HP = dice.HP(10, 1, name, 6) + int(HPadj) + 3
                name.char_class_abilities["UAPaladin"]["Superior Fighting"] = "1/Level attack per creatures less than 1HD"
                name.char_class_abilities["UAPaladin"]["Save Bonus"] = ["+2 all Saving Throws"]
                name.char_class_abilities["UAPaladin"]["Special"]["Lay on Hands"] = "+2 per level/day"
                name.char_class_abilities["UAPaladin"]["Special"]["Cure Disease"] = "1/wk per 5 levels"
                name.char_class_abilities["UAPaladin"]["Special"]["Protection from Evil"] = '1\" radius all 24/7'
                name.char_class_abilities["UAPaladin"][
                    "Lance"] = "Lance Proficiency Required, +1 DMG per Lvl when Mounted," \
                               "+1 DMG when dismounted. +1 ToHit while Mounted."
                name.char_class_abilities["UAPaladin"][
                    "Parry"] = "Unearthed Arcana Pg 15, reduce Attacker To hit by your bonus"
                name.char_class_abilities["UAPaladin"]["Horsemanship"] = "Attacks from Horseback as +1 Level (UA Pg 15)"
                name.char_class_abilities["UAPaladin"][
                    "Horsemanship2"] = "-85% thrown from saddle, or injured +1% per level"
                name.char_class_abilities["UAPaladin"][
                    "Horsemanship3"] = "+2HP per hit die for horse, determine best quality HP steed"
                name.char_class_abilities["UAPaladin"]["Resistances"] = "Mind Affecting spells 90% failure"
                name.char_class_abilities["UAPaladin"]["Special"][
                    "Protection from Fear"] = "Radiate Protection from Fear 1\" radius"
                name.char_class_abilities["UAPaladin"]["Immunity"] = "Disease, Fear"
                name.char_class_abilities["UAPaladin"]["STR Training"] = dice.exceptional_strength(name)
                name.char_class_abilities["UAPaladin"]["DEX Training"] = dice.exceptional_strength(name)
                name.char_class_abilities["UAPaladin"]["CON Training"] = dice.exceptional_strength(name)
                name.char_class_abilities["UAPaladin"]["CHA Training"] = dice.exceptional_strength(name)
            else:
                HP = dice.HP(4, 1, name, 3) + int(HPadj) + 1
            name.char_HP += HP
        elif "Barbarian" == str(c):
            if not name.char_weapon_prof_slots > 6:
                name.char_weapon_prof_slots = 6
            if not name.char_weapon_prof_penalty > -1:
                name.char_weapon_prof_penalty = -1
            name.char_class_levels.append("1")
            name.char_class_nextXP.append("6000")
            name.char_class_name = "Barbarian"
            name.char_class_xpBonus.append("0%")
            if "Barbarian" not in name.char_class_abilities:
                name.char_class_abilities["Barbarian"] = {}
                name.char_class_abilities["Barbarian"]["Special"] = {}
                name.char_class_abilities["Barbarian"]["Save Bonus"] = []
            name.char_class_abilities["Barbarian"]["AC Bonus"] = ["If AC < 14: +2/pt AC Not Bulky, +1 AC if Bulky"
                                                                   " per point over 14"]
            name.char_class_abilities["Barbarian"]["Constitution"] = ["+2 HP/lvl over 14"]
            name.char_class_abilities["Barbarian"]["Movement"] = ["Base Movement Rate of 15\" if non-bulky"]
            name.char_class_abilities["Barbarian"]["Weapons"] = ["Initial weapons must include: Hand Axe, Knife and Spear"]
            name.char_class_abilities["Barbarian"]["Superior Fighting"] = "1/Level attack per creatures less than 1HD"
            name.char_class_abilities["Barbarian"]["Restrictions"] = [
                "Cannot use magic weapons or armor, will destroy it for XP"]
            name.char_class_abilities["Barbarian"]["Special"]["Climb Cliffs and Trees"] = ["Unearthed Arcana Pg 20"]
            name.char_class_abilities["Barbarian"]["Special"]["Hide In Natural Surroundings"] = ["Unearthed Arcana Pg 20"]
            name.char_class_abilities["Barbarian"]["Surprise"] = "1-3/d6 Surprise or 1-4/d6 in familiar terrain." \
                                                                "10% to be surprised, 5% if in familiar terrain"
            name.char_class_abilities["Barbarian"]["Defense"] = "5% per level to avoid backstab/attack, can get free attack vs." \
                                                                "backstabbing attacker"
            name.char_class_abilities["Barbarian"]["Special"]["Leaping"] = "10\' forward or 3\' back or 3\' upward"
            name.char_class_abilities["Barbarian"]["Special"]["Detect Illusion"] = "5%/level detect illusion"
            name.char_class_abilities["Barbarian"]["Special"]["Detect Magic"] = "25%/+5% level (after 1st) detect" \
                                                                                "magic (not illusion)"
            name.char_class_abilities["Barbarian"]["Special"]["Leadership"] = "+1/level to CHA when dealing with Barbarians"
            name.char_class_abilities["Barbarian"]["Special"]["Survival"] = "Generic Wilderness Survival"
            name.char_class_abilities["Barbarian"]["Special"]["First Aid"] = "Generic Heal Wound"
            name.char_class_abilities["Barbarian"]["Special"]["Cure Poison"] = "10% chance 1/per day, or 50% + Victim\'s"\
                                                                               "CON score if known."
            name.char_class_abilities["Barbarian"]["Special"]["Cure Disease"] = "10% chance 1/per day, or 50% + Victim\'s" \
                                                                               "CON score if known."
            name.char_class_abilities["Barbarian"]["Special"]["Tracking"] = "As Ranger"
            name.char_class_abilities["Barbarian"]["Special"]["Outdoor Craft"] = "Animal Detect/Predict Weather" \
                                                                                "as 3rd Level Druid"
            name.char_class_abilities["Barbarian"]["Save Bonus"] = ["+4 Poison", "+3 Paralysis", "+3 Death Magic",
                                                                    "+3 Petrification and Polymorph", "+2 Rod, Staff, Wand",
                                                                    "+2 Breath Weapon", "+1 to spells at 4th (+1/4lvl"]

            print("Choose One:")
            result = False
            while not result:
                print(" 0 Animal Handling\n",
                      "1 Horsemanship\n",
                      "2 Long Distance Running\n",
                      "3 Running\n",
                      "4 Small Paddled Craft\n",
                      "5 Small Rowed Craft\n",
                      "6 Imitate Sound\n",
                      "7 Snare Building\n")
                choice = input("Choose a Number:")
                if choice.isdigit():
                    if int(choice) in range(0, 8):
                        result = True
            if choice == "0":
                name.char_class_abilities["Barbarian"]["Native"] = "Animal Handling (UA, Pg20)"
            elif choice == "1":
                name.char_class_abilities["Barbarian"]["Native"] = "Horsemanship (UA, Pg20)"
            elif choice == "2":
                name.char_class_abilities["Barbarian"]["Native"] = "Long Distance Running (UA, Pg20)"
            elif choice == "3":
                name.char_class_abilities["Barbarian"]["Native"] = "Running (UA, Pg20)"
            elif choice == "4":
                name.char_class_abilities["Barbarian"]["Native"] = "Small Paddled Craft (UA, Pg20)"
            elif choice == "5":
                name.char_class_abilities["Barbarian"]["Native"] = "Small Rowed Craft (UA, Pg20)"
            elif choice == "6":
                name.char_class_abilities["Barbarian"]["Native"] = "Imitate Sound (UA, Pg20)"
            elif choice == "7":
                    name.char_class_abilities["Barbarian"]["Native"] = "Snare Building (UA, Pg20)"
            if name.char_abilities["CON"] > 14:
                bonus = name.char_abilities["CON"] - 14
                bonus = bonus * 2
                name.char_define_abilities["CON"]["HP Adj"] = "+"+str(bonus)
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(12, 1, name, 7) + int(HPadj)
            name.char_HP += HP


    name.char_HP = round(name.char_HP/len(name.char_class))
    if name.self_roll:
        possible = [str(n) for n in range(1, 30)]
        HP = 9999
        while str(HP) not in possible:
            HP = input("What is your HP?:")
        HP = int(HP)
        name.char_HP = HP
    return name

def class_equipment_checker(name):
    char_list = []
    if 'Fighter' in name.char_class or 'Ranger' in name.char_class or 'Barbarian' in name.char_class or 'Assassin' \
            in name.char_class or 'Paladin' in name.char_class:
        if 'UAPaladin' not in name.char_class:
            char_list.append("Fighter")
    if 'Monk' in name.char_class:
        char_list.append("Monk")
    if "Cleric" in name.char_class:
        char_list.append("Cleric")
    if "Druid" in name.char_class:
        char_list.append("Druid")
    if 'MagicUser' in name.char_class or 'Illusionist' in name.char_class:
        char_list.append("MagicUser")
    if 'Thief' in name.char_class:
        char_list.append("Thief")
    if 'Cavalier' in name.char_class:
        char_list.append("Cavalier")
    if 'UAPaladin' in name.char_class:
        char_list.append("Paladin")
    return char_list

def starting_money(name):
    if "Fighter" in name.char_class or "Barbarian" in name.char_class or "Ranger" in name.char_class:
        gold = dice.normal(4, 5)
        gold = gold*10
    elif "Paladin" in name.char_class and "UAPaladin" not in name.char_class:
        gold = dice.normal(4, 5)
        gold = gold*10
    elif "Druid" in name.char_class or "Cleric" in name.char_class:
        gold = dice.normal(6, 3)
        gold = gold * 10
    elif "Thief" in name.char_class or "Assassin" in name.char_class:
        gold = dice.normal(6, 2)
        gold = gold * 10
    elif "MagicUser" in name.char_class or "Illusionist" in name.char_class:
        gold = dice.normal(4, 2)
        gold = gold * 10
    elif "Monk" in name.char_class:
        gold = dice.normal(4, 5)
    elif "UAPaladin" in name.char_class or "Cavalier" in name.char_class:
        if name.social_class in ["LUC", "MUC", "UUC"]:
            if name.social_class == "UUC":
                gold = dice.normal(6, 1)+12
            else:
                gold = dice.normal(12, 1)+6
        else:
            gold = dice.normal(4, 2)
        gold = gold*10

    if name.self_roll:
        possible = [str(n) for n in range(1, 300)]
        gold = 9999
        while str(gold) not in possible:
            gold = input("What is your gold?")
            gold = int(gold)

    name.char_money["gp"] = gold
    return name


def weapon_prof(name):
    m_weapons = {}
    mweapons = []
    mweapons.append("")
    classlist = name.char_class
    for i in range(1, 75):
        mweapons.append(weapons_list[int(i)][1])
        char_list = class_equipment_checker(name)
        match = False
        for c in char_list:
            if c in str(weapons_list[int(i)][35]):
                match = True
        if match:
            m_weapons[weapons_list[int(i)][1]] = {}
            m_weapons[weapons_list[int(i)][1]]["Damage S-M"] = str(weapons_list[int(i)][3])
            m_weapons[weapons_list[int(i)][1]]["Damage L"] = str(weapons_list[int(i)][4])
            m_weapons[weapons_list[int(i)][1]]["Length"] = str(weapons_list[int(i)][9])
            m_weapons[weapons_list[int(i)][1]]["Space"] = str(weapons_list[int(i)][10])
            m_weapons[weapons_list[int(i)][1]]["Speed"] = str(weapons_list[int(i)][11])
            m_weapons[weapons_list[int(i)][1]]["Notes"] = str(weapons_list[int(i)][6]).replace("\n", " ")
            m_weapons[weapons_list[int(i)][1]]["Encumbrance"] = str(weapons_list[int(i)][8])
            m_weapons[weapons_list[int(i)][1]]["Type"] = str(weapons_list[int(i)][2])
            m_weapons[weapons_list[int(i)][1]]["Cost"] = str(weapons_list[int(i)][7])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][12]))] = str(
                weapons_list[int(i)][12])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][13]))] = str(
                weapons_list[int(i)][13])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][14]))] = str(
                weapons_list[int(i)][14])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][15]))] = str(
                weapons_list[int(i)][15])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][16]))] = str(
                weapons_list[int(i)][16])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][17]))] = str(
                weapons_list[int(i)][17])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][18]))] = str(
                weapons_list[int(i)][18])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][19]))] = str(
                weapons_list[int(i)][19])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][20]))] = str(
                weapons_list[int(i)][20])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][21]))] = str(
                weapons_list[int(i)][21])
            m_weapons[weapons_list[int(i)][1]]["THACDJ: {}".format(str(weapons_list[0][22]))] = str(
                weapons_list[int(i)][22])
            print(i, weapons_list[int(i)][1],
                  "     Classes:", weapons_list[int(i)][34],
                  "     DMG S-M", weapons_list[int(i)][3],
                  "     DMG L", weapons_list[int(i)][4],
                  "     Note:", weapons_list[int(i)][6],
                  "     Encumbrance:", weapons_list[int(i)][8])

    prof_message = ""
    if fighter_check(name):
            prof_message += "Specialization must be done at 1st level, on any one specific weapon.  Double specialization " \
                  "can be done later.\n" \
                  "Limited to Single Class Fighters or Rangers.  Rangers must specialize" \
                  "in a specific set of weapons.\n" \
                  "Long/Short/Composite Bows require 1 additional proficiency slot to specialize.\n" \
                  "To specialize, choose the same weapon repeatedly (up to 3x)\n"
            if "Ranger" in name.char_class:
                prof_message += "You are a Ranger, you have proficiency prerequisites\n."\
                    "You MUST choose a Bow or Light Crossbow, but not both.\n"\
                    "If specializing, you MUST only choose from:\n Bow or Light Crossbow,\n"\
                    "Spear, Axe (Battle or Hand), Dagger, Knife or Sword (any).\n"\
                    "You MUST have all of the above weapons taken by 4th level.\n"
    if "Ranger" in name.char_class and len(name.char_class) > 1:
        prof_message += "You are a Ranger, you have proficiency prerequisites.\n"\
            "You MUST choose a Bow or Light Crossbow, but not both.\n"\
            "You MUST have all of these weapons taken by 4th level:\n"\
            "Spear, Axe (Battle or Hand), Dagger, Knife or Sword (any).\n"
    if 'Barbarian' in name.char_class:
        prof_message += "You are a Barbarian, you have proficiency prerequisites.\n" \
            "Barbarians MUST choose each of these: Hand Axe, Knife, and Spear to startn"\
            "The DM may require others, otherwise you're free to choose anything a Fighter can take.\n"
    if 'Cavalier' in name.char_class or 'UAPaladin' in name.char_class:
        prof_message += "You are a Cavalier or Paladin (Unearthed Arcana Version), you have proficiency prerequisites.\n"\
            "Technically you can use any weapon, but you must gain proficiency in the following first:\n"\
            "Lance (any),\n Long, Broad, Short or Bastard Swords and Scimitar.\n"\
            "Horseman's Mace, Horseman's Flail,\n"\
            "Horesman's Military Pick,\nDagger\n"\
            "Elven (High) or Half Elven (High) Cavaliers can select: Composite Short Bow\n"\
            "All other weapons are generally prohibited until higher levels\n"\
            "Depending on your Social Class, you may have been pre-equipped will get some of these for free next.\n"\
            "Your first Weapon of Choice is your Lance offering a bonus per UA Pg 14\n"
    print(prof_message)

    result = False
    while not result:

        print("Select a NUMBER to gain proficiency.")
        print("You have {} choices remaining.".format(name.char_weapon_prof_slots - len(name.char_weapon_prof)))
        print("You have chosen:", name.char_weapon_prof)
        choice = input("Choose a NUMBER to GAIN PROFICIENCY an item, or Q to quit:")
        if str(choice).upper() == "q".upper():
            result = True
            return name, result
        if choice.isdigit():
            if int(choice) in range(1, 75):
                if name.char_weapon_prof_slots - len(name.char_weapon_prof) > 0:
                    if "Bow" in str(mweapons[int(choice)]):
                        if "Cavalier" in name.char_class and not name.char_race == "Elf":
                            print("Only High Elves can choose this.")
                            return name, result
                        elif mweapons[int(choice)] in name.char_weapon_prof:
                            if name.char_weapon_prof_slots - len(name.char_weapon_prof) - 1 <= 0:
                                print("Not enough slots")
                                choice = input("Are you done? Y or N:")
                                if str(choice).upper() == "y".upper():
                                    result = True
                                return name, result
                    if mweapons[int(choice)] in name.char_weapon_prof:
                        if fighter_check(name):
                            #indx = 0
                            #for i in name.char_weapon_prof:
                            #    if mweapons[int(choice)] in i:
                            #        indx += 1
                            #indx += 1
                            if mweapons[int(choice)]+"_Specialized" in name.char_weapon_prof:
                                if mweapons[int(choice)] + "_Double-Specialized" not in name.char_weapon_prof and not \
                                        "Crossbow" in mweapons[int(choice)] :
                                    name.char_weapon_prof.append(mweapons[int(choice)]+"_Double-Specialized")
                                else:
                                    print("You already mastered Specialization.")
                                    choice = input("Are you done? Y or N:")
                                    if str(choice).upper() == "y".upper():
                                        result = True
                                    return name, result
                            else:
                                if "Bow" not in str(mweapons[int(choice)]) and "Light Crossbow" \
                                        not in str(mweapons[int(choice)]) and "Ranger" in name.char_class:
                                    print("Ranger can only specialize in Bow or Light Crossbow.")
                                    choice = input("Are you done? Y or N:")
                                    if str(choice).upper() == "y".upper():
                                        result = True
                                    return name, result
                                else:
                                    name.char_weapon_prof.append(mweapons[int(choice)] + "_Specialized")
                            if "Bow" in str(mweapons[int(choice)]):
                                name.char_weapon_prof.append(mweapons[int(choice)] + "_Specialized_Slot-2")
                        else:
                            print("You already chose this.")
                            choice = input("Are you done? Y or N:")
                            if str(choice).upper() == "y".upper():
                                result = True
                            return name, result
                    else:
                        name.char_weapon_prof.append(mweapons[int(choice)])

                    choice = input("Are you done? Y or N:")
                    if str(choice).upper() == "y".upper():
                        result = True
                    return name, result
                else:
                    print("Not enough slots")
                    choice = input("Are you done? Y or N:")
                    if str(choice).upper() == "y".upper():
                        result = True
                    return name, result

def calculate_combat_bonuses(name):
    plist = []
    for p in name.char_weapon_prof:
        p = str(p).split("_")
        plist.append(str(p[0]))

    for w in name.char_melee_weapons:
        if w in name.char_weapon_prof:
            for p in name.char_weapon_prof:
                if w == p:
                    slots = [s for s in plist if s == p]
                    if not name.char_melee_weapons[w]["Type"] == 'Bow' and not \
                            name.char_melee_weapons[w]["Type"] == 'Crossbow':
                        if len(slots) == 2:
                            name.char_melee_weapons[w]["Norm Hit"] += 1
                            name.char_melee_weapons[w]["Norm Dmg"] += 2
                            name.char_melee_weapons[w]["Norm Hit"] += int(name.char_define_abilities["STR"]["HIT"])
                            name.char_melee_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])
                        elif len(slots) == 3:
                            name.char_melee_weapons[w]["Norm Hit"] += 3
                            name.char_melee_weapons[w]["Norm Dmg"] += 3
                            name.char_melee_weapons[w]["Norm Hit"] += int(name.char_define_abilities["STR"]["HIT"])
                            name.char_melee_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])
                        if len(slots) == 2 or len(slots) == 3:
                            name.char_melee_weapons[w]["Notes"] += "SPEC: Attack 3/2 rounds."
                        if len(slots) == 1 and not "Monk" in name.char_class:
                            name.char_melee_weapons[w]["Norm Hit"] += int(name.char_define_abilities["STR"]["HIT"])
                            name.char_melee_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])
                        else:
                            name.char_melee_weapons[w]["Norm Hit"] += int(name.char_define_abilities["STR"]["HIT"])
                            name.char_melee_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])
        else:
            if not name.char_melee_weapons[w]["Type"] == 'Bow' and not \
                    name.char_melee_weapons[w]["Type"] == 'Crossbow':
                name.char_melee_weapons[w]["Norm Hit"] += name.char_weapon_prof_penalty
                name.char_melee_weapons[w]["Norm Hit"] += int(name.char_define_abilities["STR"]["HIT"])
                name.char_melee_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])

    for w in name.char_ranged_weapons:
        if w in name.char_weapon_prof:
            for p in name.char_weapon_prof:
                if w == p:
                    slots = [s for s in plist if s == p]
                    if len(slots) == 3 and name.char_ranged_weapons[w]["Type"] == "Bow":
                        name.char_ranged_weapons[w]["Norm Hit"] += 1
                        name.char_ranged_weapons[w]["Norm Dmg"] += 2
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: Point Blank Range 6\'-30\', Double Damage, +2 TH/+2 DMG."
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: Short Range (30\' to weapon Min(, +1 TH/+1 DMG."
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: If combat ready, can attack before initiative."
                        name.char_ranged_weapons[w]["Norm Hit"] += int(name.char_define_abilities["DEX"]["Missile To Hit"])
                    elif len(slots) == 2 and name.char_ranged_weapons[w]["Type"] == "Crossbow":
                        name.char_ranged_weapons[w]["Norm Hit"] += 1
                        name.char_ranged_weapons[w]["Norm Dmg"] += 2
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: Point Blank Range 6\'-60\', Double Damage, +2 TH/+2 DMG."
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: Short Range +1 TH/+1 DMG."
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: Medium Range +1 TH."
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: If combat ready, can attack before initiative."
                        name.char_ranged_weapons[w]["Norm Hit"] += int(name.char_define_abilities["DEX"]["Missile To Hit"])
                    elif len(slots) == 2:
                        name.char_ranged_weapons[w]["Norm Hit"] += 1
                        name.char_ranged_weapons[w]["Norm Dmg"] += 2
                        name.char_ranged_weapons[w]["Notes"] += "SPEC: Attack 3/2 rounds."
                        name.char_ranged_weapons[w]["Norm Hit"] += int(name.char_define_abilities["DEX"]["Missile To Hit"])
                        if not "Monk" in name.char_class:
                            name.char_ranged_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])
                    elif len(slots) == 1 and not name.char_ranged_weapons[w]["Type"] == "Bow" and \
                            len(slots) == 1 and not name.char_ranged_weapons[w]["Type"] == "Crossbow":
                        name.char_ranged_weapons[w]["Norm Hit"] += int(name.char_define_abilities["DEX"]["Missile To Hit"])
                        if not "Monk" in name.char_class:
                            name.char_ranged_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])
                    else:
                        name.char_ranged_weapons[w]["Norm Hit"] += int(name.char_define_abilities["DEX"]["Missile To Hit"])

        else:
            if name.char_ranged_weapons[w]["Type"] == "Crossbow" or name.char_ranged_weapons[w]["Type"] == "Bow":
                name.char_ranged_weapons[w]["Norm Hit"] += name.char_weapon_prof_penalty
                name.char_ranged_weapons[w]["Norm Hit"] += int(name.char_define_abilities["DEX"]["Missile To Hit"])
            else:
                name.char_ranged_weapons[w]["Norm Hit"] += name.char_weapon_prof_penalty
                name.char_ranged_weapons[w]["Norm Hit"] += int(name.char_define_abilities["DEX"]["Missile To Hit"])
                if not "Monk" in name.char_class:
                    name.char_ranged_weapons[w]["Norm Dmg"] += int(name.char_define_abilities["STR"]["DMG"])
    return name