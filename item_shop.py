import os, csv, dice

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
    provisions_csv = list(pcsv_write)

def cavalier_start(name):
    if name.social_class == "UUC":
        for a in armor_list:
            if "15" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Weight"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])
    elif name.social_class == "MUC":
        for a in armor_list:
            if "14" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Weight"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])
    elif name.social_class == "LUC":
        for a in armor_list:
            if "13" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Weight"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])
    elif name.social_class == "UMC":
        for a in armor_list:
            if "8" == str(a[0]):
                name.char_armor[str(a[1])] = {}
                name.char_armor[str(a[1])]["Armor Class"] = str(a[3])
                name.char_armor[str(a[1])]["Reduction"] = str(a[2])
                name.char_armor[str(a[1])]["Weight"] = str(a[5])
                name.char_armor[str(a[1])]["Bulk"] = str(a[7])

    result = False
    while not result:
        for i in range(1, 3):
            print(armor_list[i][0], armor_list[i][1])
        choice = input("Pick NUMBER for your shield:")
        if str(choice).isdigit():
            if int(choice) in range(1, 3):
                name.char_shield[armor_list[int(choice)][1]] = {}
                name.char_shield[armor_list[int(choice)][1]]["Armor Class"] = str(armor_list[int(choice)][3])
                name.char_shield[armor_list[int(choice)][1]]["Reduction"] = str(armor_list[int(choice)][2])
                name.char_shield[armor_list[int(choice)][1]]["Weight"] = str(armor_list[int(choice)][5])
                name.char_shield[armor_list[int(choice)][1]]["Bulk"] = str(armor_list[int(choice)][7])
                result = True

    result = False
    while not result:
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
                name.char_melee_weapons[weapons_list[int(choice)][1]]["Notes"] = str(weapons_list[int(choice)][6])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][12]))]\
                    = str(weapons_list[int(choice)][12])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][13]))]\
                    = str(weapons_list[int(choice)][13])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][14]))]\
                    = str(weapons_list[int(choice)][14])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][15]))]\
                    = str(weapons_list[int(choice)][15])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][16]))]\
                    = str(weapons_list[int(choice)][16])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][17]))]\
                    = str(weapons_list[int(choice)][17])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][18]))]\
                    = str(weapons_list[int(choice)][18])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][19]))]\
                    = str(weapons_list[int(choice)][19])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][20]))]\
                    = str(weapons_list[int(choice)][20])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][21]))]\
                    = str(weapons_list[int(choice)][21])
                name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][22]))]\
                    = str(weapons_list[int(choice)][22])
                result = True
    if name.social_class in ["UMC", "LUC", "MUC", "UUC"]:
        result = False
        while not result:
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
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["Notes"] = str(weapons_list[int(choice)][6])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][12]))] \
                        = str(weapons_list[int(choice)][12])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][13]))] \
                        = str(weapons_list[int(choice)][13])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][14]))] \
                        = str(weapons_list[int(choice)][14])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][15]))] \
                        = str(weapons_list[int(choice)][15])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][16]))] \
                        = str(weapons_list[int(choice)][16])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][17]))] \
                        = str(weapons_list[int(choice)][17])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][18]))] \
                        = str(weapons_list[int(choice)][18])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][19]))] \
                        = str(weapons_list[int(choice)][19])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][20]))] \
                        = str(weapons_list[int(choice)][20])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][21]))] \
                        = str(weapons_list[int(choice)][21])
                    name.char_melee_weapons[weapons_list[int(choice)][1]]["THACDJ: {}".format(str(weapons_list[0][22]))] \
                        = str(weapons_list[int(choice)][22])
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
        name.char_melee_weapons[weapons_list[20][1]]["Notes"] = str(weapons_list[20][6])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][12]))] \
            = str(weapons_list[20][12])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][13]))] \
            = str(weapons_list[20][13])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][14]))] \
            = str(weapons_list[20][14])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][15]))] \
            = str(weapons_list[20][15])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][16]))] \
            = str(weapons_list[20][16])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][17]))] \
            = str(weapons_list[20][17])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][18]))] \
            = str(weapons_list[20][18])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][19]))] \
            = str(weapons_list[20][19])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][20]))] \
            = str(weapons_list[20][20])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][21]))] \
            = str(weapons_list[20][21])
        name.char_melee_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][22]))] \
            = str(weapons_list[20][22])

        name.char_ranged_weapons[weapons_list[20][1]] = {}
        name.char_ranged_weapons[weapons_list[20][1]]["Damage S-M"] = str(
            weapons_list[20][3])
        name.char_ranged_weapons[weapons_list[20][1]]["Damage L"] = str(
            weapons_list[20][4])
        name.char_ranged_weapons[weapons_list[20][1]]["Length"] = str(weapons_list[20][9])
        name.char_ranged_weapons[weapons_list[20][1]]["Space"] = str(weapons_list[20][10])
        name.char_ranged_weapons[weapons_list[20][1]]["Speed"] = str(weapons_list[20][11])
        name.char_ranged_weapons[weapons_list[20][1]]["Notes"] = str(weapons_list[20][6])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][23]))] \
            = str(weapons_list[20][12])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][24]))] \
            = str(weapons_list[20][13])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][25]))] \
            = str(weapons_list[20][14])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][26]))] \
            = str(weapons_list[20][15])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][27]))] \
            = str(weapons_list[20][16])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][28]))] \
            = str(weapons_list[20][17])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][29]))] \
            = str(weapons_list[20][18])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][30]))] \
            = str(weapons_list[20][19])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][31]))] \
            = str(weapons_list[20][20])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][32]))] \
            = str(weapons_list[20][21])
        name.char_ranged_weapons[weapons_list[20][1]]["THACDJ: {}".format(str(weapons_list[0][33]))] \
            = str(weapons_list[20][22])
        name.char_ranged_weapons[weapons_list[20][1]]["Rate of Fire"] = str(weapons_list[20][5])
        if name.social_class in ["UUC"]:
            name.char_melee_weapons[weapons_list[44][1]] = {}
            name.char_melee_weapons[weapons_list[44][1]]["Damage S-M"] = str(
                weapons_list[44][3])
            name.char_melee_weapons[weapons_list[44][1]]["Damage L"] = str(
                weapons_list[44][4])
            name.char_melee_weapons[weapons_list[44][1]]["Length"] = str(weapons_list[44][9])
            name.char_melee_weapons[weapons_list[44][1]]["Space"] = str(weapons_list[44][10])
            name.char_melee_weapons[weapons_list[44][1]]["Speed"] = str(weapons_list[44][11])
            name.char_melee_weapons[weapons_list[44][1]]["Notes"] = str(weapons_list[44][6])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][12]))] \
                = str(weapons_list[44][12])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][13]))] \
                = str(weapons_list[44][13])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][14]))] \
                = str(weapons_list[44][14])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][15]))] \
                = str(weapons_list[44][15])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][16]))] \
                = str(weapons_list[44][16])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][17]))] \
                = str(weapons_list[44][17])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][18]))] \
                = str(weapons_list[44][18])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][19]))] \
                = str(weapons_list[44][19])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][20]))] \
                = str(weapons_list[44][20])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][21]))] \
                = str(weapons_list[44][21])
            name.char_melee_weapons[weapons_list[44][1]]["THACDJ: {}".format(str(weapons_list[0][22]))] \
                = str(weapons_list[44][22])

    return name