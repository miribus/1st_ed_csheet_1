import dice

def class_details(name):
    for c in name.char_class:
        if "Cleric" == str(c):
            if name.char_abilities["WIS"] > 15:
                name.char_class_xpBonus.append("+10%")
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
            if name.char_abilities["WIS"] > 15 and name.char_abilities["CHA"] > 15:
                name.char_class_xpBonus.append("+10%")
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(8, 1, name, 5)+int(HPadj)
            name.char_HP += HP

        elif "Fighter" == str(c):
            if name.char_abilities["STR"] > 15:
                name.char_class_xpBonus.append("+10%")
            if "Fighter" not in name.char_class_abilities:
                name.char_class_abilities["Fighter"] = {}
            name.char_class_abilities["Fighter"]["Specialization (UA) 1"] = "2x WP Slots for Spec, 3x WP Slots for Double Spec;" \
                                                                     "+1/+2 (Single) +3/+3 (Double Spec: no missile, polearm," \
                                                                     "or 2h sword). Damage Bonus only at \'point blank\' range"
            name.char_class_abilities["Fighter"]["Specialization (UA) 2"] = "Atk/Rnd: Melee: 3/2, Bow: 2/1, LxB: 1/1, " \
                                                                    "HxB: 1/2, Lasso/SSling: 1/1, Thrown Dagger: 3/1, " \
                                                                    "Thrown Dart: 4/1, Other: 3/2"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(10, 1, name, 6)+int(HPadj)
            name.char_HP += HP
        elif "Paladin" == str(c) and "UAPaladin" not in str(c):
            if name.char_abilities["STR"] > 15 and name.char_abilities["WIS"] > 15:
                name.char_class_xpBonus.append("+10%")
            if "Paladin" not in name.char_class_abilities:
                name.char_class_abilities["Paladin"] = {}
                name.char_class_abilities["Paladin"]["Special"] = {}
                name.char_class_abilities["Paladin"]["Save Bonus"] = {}
                name.char_class_abilitiee["Paladin"]["Immunity"] = "Disease, Fear"
            name.char_class_abilities["Paladin"]["Save Bonus"] = "+2 all Saving Throws"
            name.char_class_abilities["Paladin"]["Special"]["Lay on Hands"] = "+2 per level/day"
            name.char_class_abilities["Paladin"]["Special"]["Cure Disease"] = "1/wk per 5 levels"
            name.char_class_abilities["Paladin"]["Special"]["Protection from Evil"] = '1\" radius all 24/7'
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(10, 1, name, 6)+int(HPadj)
            name.char_HP += HP
        elif "Ranger" == str(c):
            if name.char_abilities["STR"] > 15 and name.char_abilities["WIS"] > 15 and name.char_abilities["INT"] > 15:
                name.char_class_xpBonus.append("+10%")
            if "Ranger" not in name.char_class_abilities:
                name.char_class_abilities["Ranger"] = {}
                name.char_class_abilities["Ranger"]["Special"] = {}
            name.char_class_abilities["Ranger"]["Combat Bonus"] = "+1 Dmg/Lvl against: Bugbear, Ettin, Giant,"\
                                                                  "Gnoll, Goblin, Hobgoblin, Kobold, Ogre,"\
                                                                  "Ogre Magi, Orc, Troll"

            name.char_class_abilities["Ranger"]["Surprise"] = "1-3/d6 Surprise if alone, w/Elves." \
                                                              " 1/d6 to be Surprised if alone, w/Elves"
            name.char_class_abilities["Ranger"]["Special"]["Tracking"] = "Tracking PHB Pg: 24"
            name.char_class_abilities["Ranger"]["Special"]["Cure Disease"] = "1/wk per 5 levels"
            name.char_class_abilities["Ranger"]["Special"]["Protection from Evil"] = '1\" radius all 24/7'
            name.char_class_abilities["Ranger"][
                "Specialization (UA) 1"] = "2x WP Slots for Spec, 3x WP Slots for Double Spec;" \
                                                                     "+1/+2 (Single) +3/+3 (Double Spec: no missile, polearm," \
                                                                     "or 2h sword). Damage Bonus only at \'point blank\' range"
            name.char_class_abilities["Ranger"]["Specialization (UA) 2"] = "Atk/Rnd: Melee: 3/2, Bow: 2/1, LxB: 1/1, " \
                                                                            "HxB: 1/2, Lasso/SSling: 1/1, Thrown Dagger: 3/1, " \
                                                                            "Thrown Dart: 4/1, Other: 3/2"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(8, 2, name, 9) + int(HPadj) + int(HPadj)
            name.char_HP += HP
        elif "MagicUser" == str(c):
            if name.char_abilities["INT"] > 15:
                name.char_class_xpBonus.append("+10%")
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(4, 1, name, 3) + int(HPadj)
            name.char_HP += HP
        elif "Illusionist" == str(c):
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(4, 1, name, 3) + int(HPadj)
            name.char_HP += HP
        elif "Thief" == str(c):
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
            if "Assassin" not in name.char_class_abilities:
                name.char_class_abilities["Assassin"] = {}
            name.char_class_abilities["Assassin"]["Assassinate"] = ["~50% to Assassinate: Victim 0L: 50gp, Victim 1-2L: "
                                                                    "100gp, Victim 3-4L: 150gp, Victim 5-6L: 200gp, "
                                                                    "Victim 7-9L: 250gp"]
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(6, 1, name, 4) + int(HPadj)
            name.char_HP += HP
        elif "Monk" == str(c):
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
            if "Cavalier" not in name.char_class_abilities:
                name.char_class_abilities["Cavalier"] = {}
            name.char_class_abilities["Cavalier"]["Honor"] = ["Cannot run from combat", "Must wear metal armor"]
            name.char_define_abilities["Cavalier"]["Lance"] = "Lance Proficiency Required, +1 DMG per Lvl when Mounted," \
                                                              "+1 DMG when dismounted."
            name.char_define_abilities["Cavalier"][
                "Parry"] = "Unearthed Arcana Pg 15, reduce Attacker To hit by your bonus"
            name.char_define_abilities["Cavalier"]["Immununity"] = "Fear"
            name.char_define_abilities["Cavalier"]["Horsemanship"] = "Attacks from Horseback as +1 Level (UA Pg 15)"
            name.char_define_abilities["Cavalier"]["Horsemanship2"] = "-85% thrown from saddle, or injured +1% per level"
            name.char_define_abilities["Cavalier"]["Horsemanship3"] = "+2HP per hit die for horse, determine best quality HP steed"
            name.char_define_abilities["Cavalier"]["Resistances"] = "Mind Affecting spells 90% failure"
            name.char_define_abilities["Cavalier"]["Good Aligned"] = "Radiate Protection from Fear 1\" radius"
            name.char_define_abilities["Cavalier"]["STR Training"] = dice.exceptional_strength()
            name.char_define_abilities["Cavalier"]["DEX Training"] = dice.exceptional_strength()
            name.char_define_abilities["Cavalier"]["CON Training"] = dice.exceptional_strength()


            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            if name.char_social_class in ["MMC", "UMC", "LUC", "MUC", "UUC"]:

                HP = dice.HP(10, 1, name, 6) + int(HPadj) + 3
            else:
                HP = dice.HP(4, 1, name, 3) + int(HPadj) + 1
            name.char_HP += HP
        elif "UAPaladin" == str(c):
            if "UAPaladin" not in name.char_class_abilities:
                name.char_class_abilities["UAPaladin"] = {}
                name.char_class_abilities["UAPaladin"]["Special"] = {}
                name.char_class_abilities["UAPaladin"]["Save Bonus"] = {}
                name.char_class_abilitiee["UAPaladin"]["Immunity"] = "Disease, Fear"
            name.char_class_abilities["UAPaladin"]["Save Bonus"] = "+2 all Saving Throws"
            name.char_class_abilities["UAPaladin"]["Special"]["Lay on Hands"] = "+2 per level/day"
            name.char_class_abilities["UAPaladin"]["Special"]["Cure Disease"] = "1/wk per 5 levels"
            name.char_class_abilities["UAPaladin"]["Special"]["Protection from Evil"] = '1\" radius all 24/7'
            name.char_class_abilities["UAPaladin"]["Honor"] = ["Cannot run from combat", "Must wear metal armor"]
            name.char_class_abilities["UAPaladin"]["Honor"] = ["Cannot run from combat", "Must wear metal armor"]
            name.char_define_abilities["UAPaladin"]["Lance"] = "Lance Proficiency Required, +1 DMG per Lvl when Mounted," \
                                                              "+1 DMG when dismounted."
            name.char_define_abilities["UAPaladin"][
                "Parry"] = "Unearthed Arcana Pg 15, reduce Attacker To hit by your bonus"
            name.char_define_abilities["UAPaladin"]["Immununity"] = "Fear"
            name.char_define_abilities["UAPaladin"]["Horsemanship"] = "Attacks from Horseback as +1 Level (UA Pg 15)"
            name.char_define_abilities["UAPaladin"][
                "Horsemanship2"] = "-85% thrown from saddle, or injured +1% per level"
            name.char_define_abilities["UAPaladin"][
                "Horsemanship3"] = "+2HP per hit die for horse, determine best quality HP steed"
            name.char_define_abilities["UAPaladin"]["Resistances"] = "Mind Affecting spells 90% failure"
            name.char_define_abilities["UAPaladin"]["Good Aligned"] = "Radiate Protection from Fear 1\" radius"
            name.char_define_abilities["UAPaladin"]["STR Training"] = dice.exceptional_strength()
            name.char_define_abilities["UAPaladin"]["DEX Training"] = dice.exceptional_strength()
            name.char_define_abilities["UAPaladin"]["CON Training"] = dice.exceptional_strength()
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            if name.char_social_class in ["MMC", "UMC", "LUC", "MUC", "UUC"]:
                HP = dice.HP(10, 1, name, 6) + int(HPadj) + 3
            else:
                HP = dice.HP(4, 1, name, 3) + int(HPadj) + 1
            name.char_HP += HP
        elif "Barbarian" == str(c):
            if "Barbarian" not in name.char_class_abilities:
                name.char_class_abilities["Barbarian"] = {}
                name.char_class_abilities["Barbarian"]["Special"] = {}
            name.char_class_abilitiess["Barbarian"]["AC Bonus"] = ["If AC < 14: +2/pt AC Not Bulky, +1 AC if Bulky"
                                                                   " per point over 14"]
            name.char_class_abilitiess["Barbarian"]["Movement"] = ["Base Movement Rate of 15\""]
            name.char_class_abilitiess["Barbarian"]["Weapons"] = ["Initial weapons must include: Hand Axe, Knife and Spear"]
            name.char_class_abilitiess["Barbarian"]["Restrictions"] = [
                "Cannot use magic weapons or armor, will destroy it for XP"]
            name.char_class_abilities["Barbarian"]["Special"]["Climb Cliffs and Trees"] = ["Unearthed Arcana Pg 20"]
            name.char_class_abilities["Barbarian"]["Special"]["Hide In Natural Surroundings"] = ["Unearthed Arcana Pg 20"]
            name.char_class_abilities["Barbarian"]["Surprise"] = "1-3/d6 Surprise or 1-4/d6 in familiar terrain." \
                                                                "10% to be surprised, 5% if in familiar terrain"
            name.char_class_abilities["Barbarian"]["Defense"] = "5% per level to avoid backstab, can get free attack vs." \
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
            print("Choose One:")
            choice = False
            while not choice.isdigit() and int(choice) in range(0, 8):
                print("0 Animal Handling",
                      "1 Horsemanship",
                      "2 Long Distance Running",
                      "3 Running",
                      "4 Small Paddled Craft",
                      "5 Small Rowed Craft",
                      "6 Imitate Sound",
                      "7 Snare Building")
                choice = input("Choose a Number")
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
            elif choice == "6":
                name.char_class_abilities["Barbarian"]["Native"] = "Snare Building (UA, Pg20)"
            HPadj = name.char_define_abilities["CON"]["HP Adj"]
            HP = dice.HP(12, 1, name, 7) + int(HPadj)
            name.char_HP += HP

    name.char_HP = round(name.char_HP/len(name.char_class))
    return name