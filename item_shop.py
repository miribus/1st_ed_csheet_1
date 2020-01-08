import os, csv, encumbrance, class_abilities

tables = str(os.getcwd()+"\\tables\\")
armor_csv = tables+"armors_csv.csv"
weapons_csv = tables+"weapons_csv.csv"
provisions_csv = tables+"provisions_csv.csv"
#

with open(armor_csv, 'r') as ACSV:
    acsv_write = csv.reader(ACSV, delimiter=",")
    armor_list = list(acsv_write)

with open(weapons_csv, 'r') as WCSV:
    wcsv_write = csv.reader(WCSV, delimiter = ",")
    weapons_list = list(wcsv_write)

with open(provisions_csv, 'r') as PCSV:
    pcsv_write = csv.reader(PCSV, delimiter = ",")
    provisions_list = list(pcsv_write)


def show_inv(name):
    stuff = []
    for w in name.char_melee_weapons:
        stuff.append([w, name.char_melee_weapons[w]])
    for w in name.char_ranged_weapons:
        stuff.append(["RANGED", w, name.char_ranged_weapons[w]])
    for a in name.char_armor:
        stuff.append(["Armor:", a, name.char_armor[a]])
    for s in name.char_shield:
        stuff.append(["Shield:", s, name.char_shield[s]])
    for i in name.char_inventory:
        stuff.append(["Inventory:", i, name.char_inventory[i]])
    print("Your inventory:\n")
    for s in stuff:
        print(s)
    print("+++++++++++++++ Ebd Inventory\n")
    print("Your Movement Rate & Encumbrance:")
    name = encumbrance.calculate_encumbrance(name)
    print("Move:", name.char_movement_rate)
    print("Weight Ranges:", name.char_encumbrance)
    print("***********")


def buy_weapons(name):
    m_weapons = {}
    r_weapons = {}
    mweapons = []
    mweapons.append("")
    rweapons = []
    rweapons.append("")
    show_weapons = {}
    classlist = name.char_class
    for i in range(1, 75):
        char_list = class_abilities.class_equipment_checker(name)

        for c in char_list:
            if c in str(weapons_list[int(i)][35]):
                match = True
        if match:
            if weapons_list[int(i)][1] not in mweapons:
                mweapons.append(weapons_list[int(i)][1])
            if weapons_list[int(i)][1] not in rweapons:
                rweapons.append(weapons_list[int(i)][1])
            m_weapons[weapons_list[int(i)][1]] = {}
            r_weapons[weapons_list[int(i)][1]] = {}
            m_weapons[weapons_list[int(i)][1]]["Damage S-M"] = str(weapons_list[int(i)][3])
            m_weapons[weapons_list[int(i)][1]]["Damage L"] = str(weapons_list[int(i)][4])
            m_weapons[weapons_list[int(i)][1]]["Length"] = str(weapons_list[int(i)][9])
            m_weapons[weapons_list[int(i)][1]]["Space"] = str(weapons_list[int(i)][10])
            m_weapons[weapons_list[int(i)][1]]["Speed"] = str(weapons_list[int(i)][11])
            m_weapons[weapons_list[int(i)][1]]["Notes"] = str(weapons_list[int(i)][6]).replace("\n", " ")
            m_weapons[weapons_list[int(i)][1]]["Encumbrance"] = str(weapons_list[int(i)][8])
            m_weapons[weapons_list[int(i)][1]]["Type"] = str(weapons_list[int(i)][2])
            m_weapons[weapons_list[int(i)][1]]["Cost"] = str(weapons_list[int(i)][7])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][12]))] = str(weapons_list[int(i)][12])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][13]))] = str(weapons_list[int(i)][13])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][14]))] = str(weapons_list[int(i)][14])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][15]))] = str(weapons_list[int(i)][15])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][16]))] = str(weapons_list[int(i)][16])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][17]))] = str(weapons_list[int(i)][17])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][18]))] = str(weapons_list[int(i)][18])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][19]))] = str(weapons_list[int(i)][19])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][20]))] = str(weapons_list[int(i)][20])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][21]))] = str(weapons_list[int(i)][21])
            m_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][22]))] = str(weapons_list[int(i)][22])
            m_weapons[weapons_list[int(i)][1]]["Norm Hit"] = 0
            m_weapons[weapons_list[int(i)][1]]["Norm Dmg"] = 0
            if "Missile" in str(weapons_list[int(i)][2]) or "Bow" in str(weapons_list[int(i)][2]) or \
                "Thrown" in str(weapons_list[int(i)][2]) or "Crossbow" in str(weapons_list[int(i)][2]):

                r_weapons[weapons_list[int(i)][1]]["Damage S-M"] = str(weapons_list[int(i)][3])
                r_weapons[weapons_list[int(i)][1]]["Damage L"] = str(weapons_list[int(i)][4])
                r_weapons[weapons_list[int(i)][1]]["Length"] = str(weapons_list[int(i)][9])
                r_weapons[weapons_list[int(i)][1]]["Space"] = str(weapons_list[int(i)][10])
                r_weapons[weapons_list[int(i)][1]]["Speed"] = str(weapons_list[int(i)][11])
                r_weapons[weapons_list[int(i)][1]]["Notes"] = str(weapons_list[int(i)][6]).replace("\n", " ")
                r_weapons[weapons_list[int(i)][1]]["Encumbrance"] = str(weapons_list[int(i)][8])
                r_weapons[weapons_list[int(i)][1]]["Type"] = str(weapons_list[int(i)][2])
                r_weapons[weapons_list[int(i)][1]]["Cost"] = str(weapons_list[int(i)][7])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][23]))] = str(weapons_list[int(i)][23])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][24]))] = str(weapons_list[int(i)][24])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][25]))] = str(weapons_list[int(i)][25])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][26]))] = str(weapons_list[int(i)][26])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][27]))] = str(weapons_list[int(i)][27])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][28]))] = str(weapons_list[int(i)][28])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][29]))] = str(weapons_list[int(i)][29])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][30]))] = str(weapons_list[int(i)][30])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][31]))] = str(weapons_list[int(i)][31])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][32]))] = str(weapons_list[int(i)][32])
                r_weapons[weapons_list[int(i)][1]]["THACADJ {}".format(str(weapons_list[0][33]))] = str(weapons_list[int(i)][33])
                r_weapons[weapons_list[int(i)][1]]["Normal Rate of Fire"] = str(weapons_list[int(i)][5])
                r_weapons[weapons_list[int(i)][1]]["Norm Hit"] = 0
                r_weapons[weapons_list[int(i)][1]]["Norm Dmg"] = 0
                if "Cavalier" in name.char_class and "Short Composite Bow" != str(r_weapons[weapons_list[int(i)][1]]):
                    if str(name.char_race) != "Elf":
                        del r_weapons[weapons_list[int(i)][1]]
                    else:
                        del r_weapons[weapons_list[int(i)][1]]
                else:
                    del r_weapons[weapons_list[int(i)][1]]
            else:
                del r_weapons[weapons_list[int(i)][1]]

            show_weapons[i] = [ weapons_list[int(i)][1],
                  "                 Cost: {}".format(weapons_list[int(i)][7]),
                  "     Classes: {}".format(weapons_list[int(i)][34]),
                  "     DMG S-M: {}".format(weapons_list[int(i)][3]),
                  "     DMG L: {}".format(weapons_list[int(i)][4]),
                  "     Note: {}".format(weapons_list[int(i)][6]),
                  "     Encumbrance: {}".format(weapons_list[int(i)][8])]
        else:
            show_weapons[i] = 0
            mweapons.append(0)
            rweapons.append(0)
    ind = 1
    #for w in show_weapons:
    sw = [w for w in show_weapons if show_weapons[w]]
    for w in sw:
        print(w, show_weapons[w])
        #show_weapons[ind] = show_weapons[w]
        ind+=1
    print("Select a NUMBER to buy, you have: ", name.char_money, " in cash.")

    result = False
    while not result:
        print("---------ITEM SHOP---------")
        display_inv = show_inv(name)

        choice = input("Choose a NUMBER to purchase an item, or Q to quit:")
        if str(choice).upper() == "q".upper():
            result = True
            return name, result
        if choice.isdigit():
            #if int(choice) in range(1, 75) and int(choice) in show_weapons:
            if int(choice) in show_weapons and show_weapons[int(choice)]:
                player_gold = int(name.char_money["gp"])
                item_cost = str(weapons_list[int(choice)][7])
                item_cost = item_cost.replace("gp", "")
                item_cost = int(item_cost)
                if player_gold >= item_cost:
                    name.char_money["gp"] = player_gold - item_cost
                    if mweapons[int(choice)] in name.char_melee_weapons:
                        indx = 0
                        for i in name.char_melee_weapons:
                            if mweapons[int(choice)] in i:
                                indx += 1
                        indx += 1
                        name.char_melee_weapons[mweapons[int(choice)]+"_"+str(indx)] = m_weapons[mweapons[int(choice)]]
                    else:
                        name.char_melee_weapons[mweapons[int(choice)]] = m_weapons[
                            mweapons[int(choice)]]

                    if rweapons[int(choice)] in name.char_ranged_weapons:
                        indx = 0
                        for i in name.char_ranged_weapons:
                            if rweapons[int(choice)] in i:
                                indx += 1
                        indx += 1
                        name.char_ranged_weapons[rweapons[int(choice)]+"_"+str(indx)] = r_weapons[rweapons[int(choice)]]
                    else:
                        try:
                            name.char_ranged_weapons[rweapons[int(choice)]] = r_weapons[
                                rweapons[int(choice)]]
                        except KeyError:
                            # don't need to look at this, it isn't a ranged weapon
                            pass
                    choice = input("Are you done? Y or N:")
                    if str(choice).upper() == "y".upper():
                        result = True
                    return name, result
                else:
                    print("Not enough gold...")
                    choice = input("Are you done? Y or N:")
                    if str(choice).upper() == "y".upper():
                        result = True
                    return name, result
            else:
                return name, False
        else:
            return name, False


def buy_armor(name):
    char_list = class_abilities.class_equipment_checker(name)
    show_shields = {}
    if len(name.char_shield) == 0:
        result = False
        while not result:
            display_inv = show_inv(name)
            for i in range(1, 6):
                for c in char_list:
                    if str(c) in str(armor_list[int(i)][9]):
                        show_shields[armor_list[i][0]] = [ armor_list[i][1],
                              "     Classes: {}".format(armor_list[i][8]),
                              "Cost: {}".format(armor_list[i][4]),
                              "Encumbrance: {}".format(armor_list[i][5]),
                              "Bulk: {}".format(armor_list[i][7]) ]

            for s in show_shields:
                print(s, show_shields[s])
            print("You have: ", name.char_money, " in cash.")
            if len(show_shields) == 0:
                print("You cannot use a shield, you should just quit")
            choice = input("Pick NUMBER for your shield, or Q to quit:")
            if str(choice).upper() == "q".upper():
                result = True
            if str(choice).isdigit():
                if int(choice) in range(1, 6):
                    name.char_shield[armor_list[int(choice)][1]] = {}
                    name.char_shield[armor_list[int(choice)][1]]["Armor Class"] = str(armor_list[int(choice)][3])
                    name.char_shield[armor_list[int(choice)][1]]["Reduction"] = str(armor_list[int(choice)][2])
                    name.char_shield[armor_list[int(choice)][1]]["Encumbrance"] = str(armor_list[int(choice)][5])
                    name.char_shield[armor_list[int(choice)][1]]["Bulk"] = str(armor_list[int(choice)][7])
                    player_gold = int(name.char_money["gp"])
                    item_cost = str(armor_list[int(choice)][4])
                    item_cost = item_cost.replace("gp", "")
                    item_cost = int(item_cost)
                    if player_gold >= item_cost:
                        name.char_money["gp"] = player_gold - item_cost
                        result = True
                    else:
                        print("Not enough gold...")
                        choice = input("Are you done? Y or N:")
                        if str(choice).upper() == "y".upper():
                            result = True
    else:
        print("You have been provisioned a shield")
        result = True

    if len(name.char_armor) == 0:
        show_armor = {}
        result = False
        while not result:
            display_inv = show_inv(name)
            for i in range(6, 19):
                for c in char_list:
                    if str(c) in str(armor_list[int(i)][9]):
                        show_armor[armor_list[i][0]] = [ armor_list[i][1],
                              "     Classes: {}".format(armor_list[i][8]),
                              "Cost: {}".format(armor_list[i][4]),
                              "Encumbrance: {}".format(armor_list[i][5]),
                              "Bulk: {}".format(armor_list[i][7]) ]

            for a in show_armor:
                print(a, show_armor[a])
            if len(show_armor) == 0:
                print("You cannot use armor, you should just quit")
            print("You have: ", name.char_money, " in cash.")
            choice = input("Pick NUMBER for your Armor, or Q to quit::")
            if str(choice).upper() == "q".upper():
                result = True
                return name, result
            if str(choice).isdigit():
                if int(choice) in range(6, 19):
                    name.char_armor[armor_list[int(choice)][1]] = {}
                    name.char_armor[armor_list[int(choice)][1]]["Armor Class"] = str(armor_list[int(choice)][3])
                    name.char_armor[armor_list[int(choice)][1]]["Reduction"] = str(armor_list[int(choice)][2])
                    name.char_armor[armor_list[int(choice)][1]]["Encumbrance"] = str(armor_list[int(choice)][5])
                    name.char_armor[armor_list[int(choice)][1]]["Bulk"] = str(armor_list[int(choice)][7])
                    player_gold = int(name.char_money["gp"])
                    item_cost = str(armor_list[int(choice)][4])
                    item_cost = item_cost.replace("gp", "")
                    item_cost = int(item_cost)
                    if player_gold >= item_cost:
                        name.char_money["gp"] = player_gold - item_cost
                        result = True
                    else:
                        print("Not enough gold...")
                        choice = input("Are you done? Y or N:")
                        if str(choice).upper() == "y".upper():
                            result = True
    else:
        print("You have been provisioned Armor")
        result = True

    return name, result

def buy_provisions(name):
    provisions = {}
    prov = []
    prov.append("")
    for i in range(1, 106):
        prov.append(provisions_list[int(i)][1])
        provisions[provisions_list[int(i)][1]] = {}
        provisions[provisions_list[int(i)][1]]["Cost"] = str(provisions_list[int(i)][2])
        provisions[provisions_list[int(i)][1]]["Encumbrance"] = str(provisions_list[int(i)][3])
        if 'Cleric' in name.char_class:
            components = provisions_list[int(i)][4]
        elif 'Druid' in name.char_class:
            components = provisions_list[int(i)][5]
        elif 'MagicUser' in name.char_class:
            components = provisions_list[int(i)][6]
        elif 'Illusionist' in name.char_class:
            components = provisions_list[int(i)][7]
        else:
            components = ""

        print(i, provisions_list[int(i)][1],
              "                 Cost:", provisions_list[int(i)][2],
              "     Weight/Encumbrance:", provisions_list[int(i)][3],
              "     Component Use:", components)

    result = False
    while not result:
        display_inv = show_inv(name)
        print("You have: ", name.char_money, " in cash.")
        choice = input("Choose a NUMBER to purchase an item, or Q to quit:")
        if str(choice).upper() == "q".upper():
            result = True
            return name, result
        if choice.isdigit():
            if int(choice) in range(1, 106):
                player_gold = int(name.char_money["gp"])
                item_cost = str(provisions_list[int(choice)][2])
                item_cost = item_cost.replace("gp", "")
                item_cost = int(item_cost)
                if player_gold >= item_cost:
                    name.char_money["gp"] = player_gold - item_cost
                    if prov[int(choice)] in name.char_inventory:
                        indx = 0
                        for i in name.char_inventory:
                            if prov[int(choice)] in i:
                                indx += 1
                        indx += 1
                        name.char_inventory[prov[int(choice)] + "_" + str(indx)] = provisions[
                            prov[int(choice)]]
                    else:
                        name.char_inventory[prov[int(choice)]] = provisions[
                            prov[int(choice)]]
                    choice = input("Are you done? Y or N:")
                    if str(choice).upper() == "y".upper():
                        result = True
                    return name, result
                else:
                    print("Not enough gold...")
                    choice = input("Are you done? Y or N:")
                    if str(choice).upper() == "y".upper():
                        result = True
                    return name, result


def cavalier_start(name):
    if name.social_class == "UUC":
        for a in armor_list:
            if "18" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Encumbrance"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])
    elif name.social_class == "MUC":
        for a in armor_list:
            if "17" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Encumbrance"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])
    elif name.social_class == "LUC":
        for a in armor_list:
            if "16" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Encumbrance"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])
    elif name.social_class == "UMC":
        for a in armor_list:
            if "11" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Encumbrance"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])

    result = False
    while not result:
        display_inv = show_inv(name)
        for i in range(1, 3):
            print(armor_list[i][0], armor_list[i][1])
        choice = input("Pick NUMBER for your shield:")
        if str(choice).isdigit():
            if int(choice) in range(1, 3):
                name.char_shield[armor_list[int(choice)][1]] = {}
                name.char_shield[armor_list[int(choice)][1]]["Armor Class"] = str(armor_list[int(choice)][3])
                name.char_shield[armor_list[int(choice)][1]]["Reduction"] = str(armor_list[int(choice)][2])
                name.char_shield[armor_list[int(choice)][1]]["Encumbrance"] = str(armor_list[int(choice)][5])
                name.char_shield[armor_list[int(choice)][1]]["Bulk"] = str(armor_list[int(choice)][7])
                result = True

    result = False
    while not result:
        display_inv = show_inv(name)
        print("\n")
        print(weapons_list[66][0], weapons_list[66][1])
        print(weapons_list[69][0], weapons_list[69][1])
        choice = input("Pick NUMBER for your Sword:")
        if str(choice).isdigit():
            if int(choice) in range(66, 70) and int(choice) not in range(67,69):
                name.char_melee_weapons[weapons_list[int(choice)][1]] = {}
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Damage S-M"] = str(weapons_list[int(choice)][3])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Damage L"] = str(weapons_list[int(choice)][4])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Length"] = str(weapons_list[int(choice)][9])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Space"] = str(weapons_list[int(choice)][10])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Speed"] = str(weapons_list[int(choice)][11])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Notes"] = str(weapons_list[int(choice)][6]) \
                    .replace("\n", " ")
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Encumbrance"] = str(weapons_list[int(choice)][8])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Type"] = str(weapons_list[int(choice)][2])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][12]))]\
                    = str(weapons_list[int(choice)][12])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][13]))]\
                    = str(weapons_list[int(choice)][13])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][14]))]\
                    = str(weapons_list[int(choice)][14])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][15]))]\
                    = str(weapons_list[int(choice)][15])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][16]))]\
                    = str(weapons_list[int(choice)][16])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][17]))]\
                    = str(weapons_list[int(choice)][17])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][18]))]\
                    = str(weapons_list[int(choice)][18])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][19]))]\
                    = str(weapons_list[int(choice)][19])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][20]))]\
                    = str(weapons_list[int(choice)][20])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][21]))]\
                    = str(weapons_list[int(choice)][21])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][22]))]\
                    = str(weapons_list[int(choice)][22])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Norm Hit"] = 0
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Norm Dmg"] = 0
                result = True
    if name.social_class in ["UMC", "LUC", "MUC", "UUC"]:
        result = False
        while not result:
            display_inv = show_inv(name)
            for i in range(39, 42):
                print(weapons_list[i][0], weapons_list[i][1])
            choice = input("Pick NUMBER for your Lance:")
            print("\n")
            if str(choice).isdigit():
                if int(choice) in range(39, 42):
                    name.char_melee_weapons[weapons_list[int(choice)][1]] = {}
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Damage S-M"] = str(
                        weapons_list[int(choice)][3])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Damage L"] = str(
                        weapons_list[int(choice)][4])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Length"] = str(weapons_list[int(choice)][9])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Space"] = str(weapons_list[int(choice)][10])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Speed"] = str(weapons_list[int(choice)][11])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Notes"] = str(weapons_list[int(choice)][6]) \
                        .replace("\n", " ")
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Encumbrance"] = str(weapons_list[int(choice)][8])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Type"] = str(
                        weapons_list[int(choice)][2])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][12]))] \
                        = str(weapons_list[int(choice)][12])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][13]))] \
                        = str(weapons_list[int(choice)][13])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][14]))] \
                        = str(weapons_list[int(choice)][14])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][15]))] \
                        = str(weapons_list[int(choice)][15])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][16]))] \
                        = str(weapons_list[int(choice)][16])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][17]))] \
                        = str(weapons_list[int(choice)][17])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][18]))] \
                        = str(weapons_list[int(choice)][18])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][19]))] \
                        = str(weapons_list[int(choice)][19])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][20]))] \
                        = str(weapons_list[int(choice)][20])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][21]))] \
                        = str(weapons_list[int(choice)][21])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACADJ {}".format(str(weapons_list[0][22]))] \
                        = str(weapons_list[int(choice)][22])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Norm Hit"] = 0
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Norm Dmg"] = 0
                    result = True
    if name.social_class in ["LUC", "MUC", "UUC"]:
        name.char_melee_weapons[weapons_list[20][1]] = {}
        name.char_melee_weapons[weapons_list[20][1]]["Damage S-M"] = str(
            weapons_list[20][3])
        name.char_melee_weapons[weapons_list[20][1]]["Damage L"] = str(
            weapons_list[20][4])
        name.char_melee_weapons[weapons_list[20][1]]["Length"] = str(weapons_list[20][9])
        name.char_melee_weapons[weapons_list[20][1]]["Space"] = str(weapons_list[20][10])
        name.char_melee_weapons[weapons_list[20][1]]["Speed"] = str(weapons_list[20][11])
        name.char_melee_weapons[weapons_list[20][1]]["Notes"] = str(weapons_list[20][6]).replace("\n", " ")
        name.char_melee_weapons[weapons_list[20][1]]["Encumbrance"] = str(weapons_list[20][8])
        name.char_melee_weapons[weapons_list[20][1]]["Type"] = str(weapons_list[20][2])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][12]))] \
            = str(weapons_list[20][12])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][13]))] \
            = str(weapons_list[20][13])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][14]))] \
            = str(weapons_list[20][14])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][15]))] \
            = str(weapons_list[20][15])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][16]))] \
            = str(weapons_list[20][16])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][17]))] \
            = str(weapons_list[20][17])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][18]))] \
            = str(weapons_list[20][18])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][19]))] \
            = str(weapons_list[20][19])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][20]))] \
            = str(weapons_list[20][20])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][21]))] \
            = str(weapons_list[20][21])
        name.char_melee_weapons[weapons_list[20][1]]["THACADJ {}".format(str(weapons_list[0][22]))] \
            = str(weapons_list[20][22])
        name.char_melee_weapons[weapons_list[20][1]]["Norm Hit"] = 0
        name.char_melee_weapons[weapons_list[20][1]]["Norm Dmg"] = 0

        #name.char_ranged_weapons[weapons_list[20][1]] = {}
        #name.char_ranged_weapons[weapons_list[20][1]]["Damage S-M"] = str(
        #    weapons_list[20][3])
        #name.char_ranged_weapons[weapons_list[20][1]]["Damage L"] = str(
        #    weapons_list[20][4])
        #name.char_ranged_weapons[weapons_list[20][1]]["Length"] = str(weapons_list[20][9])
        #name.char_ranged_weapons[weapons_list[20][1]]["Space"] = str(weapons_list[20][10])
        #name.char_ranged_weapons[weapons_list[20][1]]["Speed"] = str(weapons_list[20][11])
        #name.char_ranged_weapons[weapons_list[20][1]]["Notes"] = str(weapons_list[20][6]).replace("\n", " ")
        #name.char_ranged_weapons[weapons_list[20][1]]["Encumbrance"] = str(weapons_list[20][8])
        #name.char_ranged_weapons[weapons_list[20][1]]["Type"] = str(weapons_list[20][2])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][23]))] \
        #    = str(weapons_list[20][23])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][24]))] \
        #    = str(weapons_list[20][24])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][25]))] \
        #    = str(weapons_list[20][25])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][26]))] \
        #    = str(weapons_list[20][26])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][27]))] \
        #    = str(weapons_list[20][27])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][28]))] \
        #    = str(weapons_list[20][28])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][29]))] \
        #    = str(weapons_list[20][29])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][30]))] \
        #    = str(weapons_list[20][30])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][31]))] \
        #    = str(weapons_list[20][31])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][32]))] \
        #    = str(weapons_list[20][32])
        #name.char_ranged_weapons[weapons_list[20][1]]["THACADJ: {}".format(str(weapons_list[0][33]))] \
        #    = str(weapons_list[20][33])
        #name.char_ranged_weapons[weapons_list[20][1]]["Rate of Fire"] = str(weapons_list[20][5])
        #name.char_ranged_weapons[weapons_list[20][1]]["Norm Hit"] = 0
        #name.char_ranged_weapons[weapons_list[20][1]]["Norm Dmg"] = 0
        if name.social_class in ["UUC"]:
            name.char_melee_weapons[weapons_list[44][1]] = {}
            name.char_melee_weapons[weapons_list[44][1]]["Damage S-M"] = str(
                weapons_list[44][3])
            name.char_melee_weapons[weapons_list[44][1]]["Damage L"] = str(
                weapons_list[44][4])
            name.char_melee_weapons[weapons_list[44][1]]["Length"] = str(weapons_list[44][9])
            name.char_melee_weapons[weapons_list[44][1]]["Space"] = str(weapons_list[44][10])
            name.char_melee_weapons[weapons_list[44][1]]["Speed"] = str(weapons_list[44][11])
            name.char_melee_weapons[weapons_list[44][1]]["Notes"] = str(weapons_list[44][6]).replace("\n", " ")
            name.char_melee_weapons[weapons_list[44][1]]["Encumbrance"] = str(weapons_list[44][8])
            name.char_melee_weapons[weapons_list[44][1]]["Type"] = str(weapons_list[44][2])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][12]))] \
                = str(weapons_list[44][12])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][13]))] \
                = str(weapons_list[44][13])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][14]))] \
                = str(weapons_list[44][14])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][15]))] \
                = str(weapons_list[44][15])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][16]))] \
                = str(weapons_list[44][16])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][17]))] \
                = str(weapons_list[44][17])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][18]))] \
                = str(weapons_list[44][18])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][19]))] \
                = str(weapons_list[44][19])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][20]))] \
                = str(weapons_list[44][20])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][21]))] \
                = str(weapons_list[44][21])
            name.char_melee_weapons[weapons_list[44][1]]["THACADJ {}".format(str(weapons_list[0][22]))] \
                = str(weapons_list[44][22])
            name.char_melee_weapons[weapons_list[44][1]]["Norm Hit"] = 0
            name.char_melee_weapons[weapons_list[44][1]]["Norm Dmg"] = 0

    return name