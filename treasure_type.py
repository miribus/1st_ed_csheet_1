import dice, os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_jewelry(jewels):
    dividers = [8, 4, 4, 2 ,2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    multipliers = [8, 4, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    if jewels > 0:
        jewels_base_val = [{'jewels_val': dice.normal(10, 1)*100, 'desc':'Ivory or Wrought Silver'},
                           {'jewels_val': dice.normal(6, 2)*100, 'desc':'Wrought Silver and Gold'},
                           {'jewels_val': dice.normal(6, 3)*100, 'desc':'Wrought Gold'},
                           {'jewels_val': dice.normal(6, 5)*100, 'desc':'Jade, Coral, or Wrought Platinum'},
                           {'jewels_val': dice.normal(6, 1)*1000, 'desc':'Silver with gems'},
                           {'jewels_val': dice.normal(4, 2)*1000, 'desc':'Gold with gems'},
                           {'jewels_val': dice.normal(6, 2)*1000, 'desc':'Platinum with gems'}]
        jewels_loot = {}
        for j in range(1, jewels+1):
            divider = dividers[dice.normal(len(dividers), 1)-1]
            multi = multipliers[dice.normal(len(multipliers), 1) - 1]
            jewels_loot[j] = jewels_base_val[dice.normal(len(jewels_base_val), 1)-1]
            jewels_loot[j] = [round(jewels_loot[j]["jewels_val"] / divider), jewels_loot[j]["desc"]]
        #print(jewels_loot)
        for j in jewels_loot:
            print(j, jewels_loot[j])
    else:
        pass



def calculate_gems(gems):
    gem_base_val = [{'gem_val': 10, 'gam_size': 'very small', 'gem_type':"", 'amount':gems},
                    {'gem_val': 50, 'gam_size': 'mall', 'gem_type':"", 'amount':gems},
                    {'gem_val': 100, 'gam_size': 'large', 'gem_type': "", 'amount':gems},
                    {'gem_val': 500, 'gam_size': 'average', 'gem_type':"", 'amount':gems},
                    {'gem_val': 1000, 'gam_size': 'large', 'gem_type':"", 'amount':gems},
                    {'gem_val': 5000, 'gam_size': 'very large', 'gem_type': "", 'amount':gems},
                    {'gem_val': 10000, 'gam_size': 'huge', 'gem_type': "", 'amount':gems},
                    {'gem_val': 25000, 'gam_size': 'huge', 'gem_type': "", 'amount':gems},
                    {'gem_val': 50000, 'gam_size': 'huge', 'gem_type': "", 'amount':gems},
                    {'gem_val': 100000, 'gam_size': 'huge', 'gem_type': "", 'amount':gems},
                    {'gem_val': 250000, 'gam_size': 'huge', 'gem_type': "", 'amount':gems},
                    {'gem_val': 500000, 'gam_size': 'huge', 'gem_type': "", 'amount':gems},
                    {'gem_val': 1000000, 'gam_size': 'huge', 'gem_type': "", 'amount':gems}]
    gem_val_idx = 0
    if dice.normal(100, 1) in range(1, 26):
        gem_val_idx += 0
    elif dice.normal(100, 1) in range(25, 52):
        gem_val_idx += 1
    elif dice.normal(100, 1) in range(51, 71):
        gem_val_idx += 2
    elif dice.normal(100, 1) in range(71, 92):
        gem_val_idx += 3
    elif dice.normal(100, 1) in range(91, 100):
        gem_val_idx += 4
    elif dice.normal(100, 1) in range(100, 101):
        gem_val_idx += 5

    if dice.normal(100, 1) in range(1, 11):
        if dice.normal(100, 1) in range(1, 6):
            gem_val_idx += 5
        elif dice.normal(100, 1) in range(5, 16):
            gem_val_idx += 4
        elif dice.normal(100, 1) in range(15, 31):
            gem_val_idx += 3
        elif dice.normal(100, 1) in range(30, 51):
            gem_val_idx += 2
        elif dice.normal(100, 1) in range(51, 100):
            gem_val_idx += 1
        elif dice.normal(100, 1) in range(100, 101):
            gem_val_idx += 6
    if dice.normal(100, 1) in range(10, 21):
        gems_loot = gem_base_val[gem_val_idx]
        gems_loot["gem_val"] = gems_loot["gem_val"]*2
    elif dice.normal(10, 1) in range(30, 41):
        gems_loot = gem_base_val[gem_val_idx]
        gems_loot["gem_val"] = gems_loot["gem_val"]*dice.normal(6,1)
    elif dice.normal(10, 1) in range(90, 101):
        gems_loot = gem_base_val[gem_val_idx]
        gems_loot["gem_val"] = gems_loot["gem_val"]/2
    else:
        gems_loot = gem_base_val[gem_val_idx]

    if gem_val_idx == 0:
        types = ["Azurite",
                 "Banded Agate",
                 "Blue Quartz",
                 "Eye Agate",
                 "Hematite",
                 "Lapis Lazuli",
                 "Malachite",
                 "Moss Agate",
                 "Obsidian",
                 "Rhodocroshite",
                 "Tiger Eye",
                 "Turquoise"]
    if gem_val_idx == 1:
        types = ["Bloodstone",
                 "Cernelian",
                 "Chalcedony",
                 "Chrysoprase",
                 "Citrine",
                 "Jasper",
                 "Moonstone",
                 "Onyx",
                 "Rock Crystal",
                 "Sardonyx",
                 "Smoky Quartz",
                 "Star Rose Quartz",
                 "Zircon"]
    if gem_val_idx == 2 or gem_val_idx == 3:
        types = ["Amber",
                 "Alexandrite",
                 "Amethyst",
                 "Aquamerine",
                 "Chrysoberyl",
                 "Coral",
                 "Garnet",
                 "Jade",
                 "Jet",
                 "Pearl",
                 "Peridot",
                 "Spinel",
                 "Topaz",
                 "Tourmaline"]
    if gem_val_idx >= 4:
        types = ["Black Opal",
                 "Black Sapphire",
                 "Diamond",
                 "Emerald",
                 "Fire Opal",
                 "Jacinth",
                 "Opal",
                 "Oriental Amethyst",
                 "Oriental Emerald",
                 "Oriental Topas",
                 "Ruby",
                 "Sapphire",
                 "Star Ruby",
                 "Star Sapphire"]
    gems_loot["gem_type"] = types[dice.normal(len(types), 1)-1]
    return gems_loot


done = False
while not done:
    loot_list = []

    copper = 0
    silver = 0
    electrum = 0
    gold = 0
    platinum = 0
    gems = 0
    jewels = 0
    magic = ""
    treasure_type = "A35k"
    while len(treasure_type) != 1 and not treasure_type.isalpha():
        treasure_type = input("Type treasure type letter:")
    treasure_type = treasure_type.upper()

    creature_count = "1"
    while not creature_count.isdigit():
        creature_count = input("Number of treasure types to roll:")
    creature_count = int(creature_count)
    creature_count += 1

    for c in range(1, creature_count):
        if treasure_type == "A":
            if dice.normal(100, 1) <= 25:
                copper += dice.normal(6, 1)*1000
            if dice.normal(100, 1) <= 30:
                silver += dice.normal(6, 1)*1000
            if dice.normal(100, 1) <= 35:
                electrum += dice.normal(6, 1)*1000
            if dice.normal(100, 1) <= 40:
                gold += dice.normal(10, 1)*1000
            if dice.normal(100, 1) <= 25:
                platinum += dice.normal(4, 1)*100
            if dice.normal(100, 1) <= 60:
                gems += dice.normal(4, 10)
            if dice.normal(100, 1) <= 50:
                jewels += dice.normal(3, 10)
            if dice.normal(100, 1) <= 30:
                magic = "A: Any 3 Magic Items\n"
        elif treasure_type == "B":
            if dice.normal(100, 1) <= 50:
                copper += dice.normal(8, 1)*1000
            if dice.normal(100, 1) <= 25:
                silver += dice.normal(6, 1)*1000
            if dice.normal(100, 1) <= 25:
                electrum += dice.normal(4, 1)*1000
            if dice.normal(100, 1) <= 25:
                gold += dice.normal(3, 1)*1000
            platinum = 0
            if dice.normal(100, 1) <= 30:
                gems += dice.normal(8, 1)
            if dice.normal(100, 1) <= 20:
                jewels += dice.normal(4, 1)
            if dice.normal(100, 1) <= 10:
                magic = "B: Magic Sword, Armor or Misc Weapo\n"
        elif treasure_type == "C":
            if dice.normal(100, 1) <= 20:
                copper += dice.normal(12, 1)*1000
            if dice.normal(100, 1) <= 30:
                silver += dice.normal(6, 1)*1000
            if dice.normal(100, 1) <= 10:
                electrum += dice.normal(4, 1)*1000
            gold = 0
            platinum = 0
            if dice.normal(100, 1) <= 25:
                gems += dice.normal(6, 1)
            if dice.normal(100, 1) <= 20:
                jewels += dice.normal(3, 1)
            if dice.normal(100, 1) <= 10:
                magic = "C: Any 2 Magic Items\n"
        elif treasure_type == "D":
            if dice.normal(100, 1) <= 10:
                copper += dice.normal(8, 1)*1000
            if dice.normal(100, 1) <= 15:
                silver += dice.normal(12, 1)*1000
            if dice.normal(100, 1) <= 15:
                electrum += dice.normal(8, 1)*1000
            if dice.normal(100, 1) <= 50:
                gold += dice.normal(6, 1) * 1000
            platinum = 0
            if dice.normal(100, 1) <= 30:
                gems += dice.normal(10, 1)
            if dice.normal(100, 1) <= 25:
                jewels += dice.normal(6, 1)
            if dice.normal(100, 1) <= 15:
                magic = "D: Any 2 Magic Items plus 1 potion\n"
        elif treasure_type == "E":
            if dice.normal(100, 1) <= 5:
                copper += dice.normal(10, 1)*1000
            if dice.normal(100, 1) <= 25:
                silver += dice.normal(12, 1)*1000
            if dice.normal(100, 1) <= 25:
                electrum += dice.normal(6, 1)*1000
            if dice.normal(100, 1) <= 25:
                gold += dice.normal(8, 1) * 1000
            platinum = 0
            if dice.normal(100, 1) <= 15:
                gems += dice.normal(12, 1)
            if dice.normal(100, 1) <= 10:
                jewels += dice.normal(10, 1)
            if dice.normal(100, 1) <= 25:
                magic = "E: Any 3 Magic Items plus 1 scroll\n"
        elif treasure_type == "F":
            copper += 0
            if dice.normal(100, 1) <= 10:
                silver += dice.normal(20, 1)*1000
            if dice.normal(100, 1) <= 15:
                electrum += dice.normal(12, 1)*1000
            if dice.normal(100, 1) <= 40:
                gold += dice.normal(10, 1) * 1000
            if dice.normal(100, 1) <= 35:
                platinum += dice.normal(8, 1) * 100
            if dice.normal(100, 1) <= 20:
                gems += dice.normal(3, 10)
            if dice.normal(3, 10) <= 10:
                jewels += dice.normal(10, 1)
            if dice.normal(100, 1) <= 30:
                magic = "F: Any 3 EXCEPT Sword/Misc Weapons, plus 1 potion & 1 scroll\n"
        elif treasure_type == "G":
            copper += 0
            silver += 0
            electrum += 0
            if dice.normal(100, 1) <= 50:
                gold += dice.normal(4, 10) * 1000
            if dice.normal(100, 1) <= 50:
                platinum += dice.normal(20, 1) * 100
            if dice.normal(100, 1) <= 30:
                gems += dice.normal(20, 5)
            if dice.normal(100, 1) <= 25:
                jewels += dice.normal(10, 1)
            if dice.normal(100, 1) <= 30:
                magic = "G: Any 4 Magic Items plus 1 scroll\n"
        elif treasure_type == "H":
            if dice.normal(100, 1) <= 25:
                copper += dice.normal(6, 5)*1000
            if dice.normal(100, 1) <= 40:
                silver += dice.normal(100, 1)*1000
            if dice.normal(100, 1) <= 40:
                electrum += dice.normal(4, 10)*1000
            if dice.normal(100, 1) <= 55:
                gold += dice.normal(6, 10)*1000
            if dice.normal(100, 1) <= 25:
                platinum += dice.normal(10, 5)*100
            if dice.normal(100, 1) <= 50:
                gems += dice.normal(100, 1)
            if dice.normal(100, 1) <= 50:
                jewels += dice.normal(4, 10)
            if dice.normal(100, 1) <= 15:
                magic = "H: Any 4 Magic Items plus 1 potion & 1 scroll\n"
        elif treasure_type == "I":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            if dice.normal(100, 1) <= 30:
                platinum += dice.normal(6, 3)*100
            if dice.normal(100, 1) <= 55:
                gems += dice.normal(20, 2)
            if dice.normal(100, 1) <= 50:
                jewels += dice.normal(12, 1)
            if dice.normal(100, 1) <= 15:
                magic = "I: Any 1 Magic Item\n"
        elif treasure_type == "J":
            if dice.normal(100, 1) <= 30:
                copper += dice.normal(20, 5)
            silver += 0
            electrum += 0
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            magic = "J: Nothing\n"
        elif treasure_type == "K":
            copper += 0
            if dice.normal(100, 1) <= 30:
                silver += dice.normal(20, 5)
            electrum += 0
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            magic = "K: Nothing\n"
        elif treasure_type == "L":
            copper += 0
            silver += 0
            if dice.normal(100, 1) <= 30:
                electrum += dice.normal(20, 4)
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            magic = "L: Nothing\n"
        elif treasure_type == "M":
            copper += 0
            silver += 0
            electrum += 0
            if dice.normal(100, 1) <= 30:
                gold += dice.normal(20, 3)
            platinum += 0
            gems += 0
            jewels += 0
            magic = "M: Nothing\n"
        elif treasure_type == "N":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            if dice.normal(100, 1) <= 30:
                platinum += dice.normal(20, 2)
            gems += 0
            jewels += 0
            magic = "N: Nothing\n"
        elif treasure_type == "0":
            if dice.normal(100, 1) <= 25:
                copper += dice.normal(4, 1)*1000
            if dice.normal(100, 1) <= 20:
                silver += dice.normal(3, 1)*1000
            electrum += 0
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            magic = "O: Nothing\n"
        elif treasure_type == "P":
            copper += dice.normal(6, 5)*1000
            if dice.normal(100, 1) <= 30:
                silver += dice.normal(6, 1)*1000
            if dice.normal(100, 1) <= 25:
                electrum += dice.normal(2, 1)*1000
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            magic = "P: Nothing\n"
        elif treasure_type == "Q":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            platinum += 0
            if dice.normal(100, 1) <= 50:
                gems += dice.normal(4, 1)
            jewels += 0
            magic = "Q: Nothing\n"
        elif treasure_type == "R":
            copper += 0
            silver += 0
            electrum += 0
            if dice.normal(100, 1) <= 40:
                gold += dice.normal(4, 2)*1000
            if dice.normal(100, 1) <= 50:
                platinum += dice.normal(10, 6)*100
            if dice.normal(100, 1) <= 55:
                gems += dice.normal(8, 4)
            if dice.normal(100, 1) <= 45:
                jewels += dice.normal(12, 1)
            if dice.normal(100, 1) <= 15:
                magic = "R: Nothing\n"
        elif treasure_type == "S":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            if dice.normal(100, 1) <= 40:
                magic = "S: 2-8 Potions\n"
        elif treasure_type == "T":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            if dice.normal(100, 1) <= 50:
                magic = "T: 1-4 Scrolls\n"
        elif treasure_type == "U":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            platinum += 0
            if dice.normal(100, 1) <= 900:
                gems += dice.normal(8, 10)
            if dice.normal(100, 1) <= 80:
                jewels += dice.normal(6, 5)
            if dice.normal(100, 1) <= 70:
                magic = "U: One of each Magic Type excluding Potions and Scrolls\n"
        elif treasure_type == "V":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            if dice.normal(100, 1) <= 85:
                magic = "V: 2 if each Magic Type excluding Potions and Scrolls\n"
        elif treasure_type == "W":
            copper += 0
            silver += 0
            electrum += 0
            if dice.normal(100, 1) <= 60:
                gold += dice.normal(6, 5)*1000
            if dice.normal(100, 1) <= 15:
                platinum += dice.normal(8, 1)*100
            if dice.normal(100, 1) <= 60:
                gems += dice.normal(8, 10)
            if dice.normal(100, 1) <= 50:
                jewels += dice.normal(8, 5)
            if dice.normal(100, 1) <= 55:
                magic = "W: 1 Map\n"
        elif treasure_type == "X":
            copper += 0
            silver += 0
            electrum += 0
            gold += 0
            platinum += 0
            gems += 0
            jewels += 0
            if dice.normal(100, 1) <= 60:
                magic = "X: 1 misc. magic item plus 1 Potion\n"
        elif treasure_type == "Y":
            copper += 0
            silver += 0
            electrum += 0
            if dice.normal(100, 1) <= 70:
                gold += dice.normal(6, 2)*1000
            platinum += 0
            gems += 0
            jewels += 0
            magic = "Y: Nothing\n"
        elif treasure_type == "Z":
            if dice.normal(100, 1) <= 20:
                copper += dice.normal(3, 1)*1000
            if dice.normal(100, 1) <= 25:
                silver += dice.normal(4, 1)*1000
            if dice.normal(100, 1) <= 25:
                electrum += dice.normal(4, 1)*1000
            if dice.normal(100, 1) <= 30:
                gold += dice.normal(4, 1)*1000
            if dice.normal(100, 1) <= 30:
                platinum += dice.normal(6, 1)*100
            if dice.normal(100, 1) <= 55:
                gems += dice.normal(6, 10)
            if dice.normal(100, 1) <= 50:
                jewels += dice.normal(6, 5)
            if dice.normal(100, 1) <= 50:
                magic = "Z: Any 3 Magic Items\n"
        loot_list.append(magic)
        if gems > 0:
            gems_loot = {gems:calculate_gems(gems)}
        else:
            gems_loot = ""



    print("Total Treasure:\n")
    print("PLATINUM :", platinum)
    print("GOLD :", gold)
    print("ELECTRUM :", electrum)
    print("SILVER :", silver)
    print("COPPER :", copper)
    print("GEMS :", gems_loot)
    print("JEWELS :", jewels)
    print("MAGIC :", loot_list)
    if jewels > 0:
        calculate_jewelry(jewels)
    #gems_loot = calculate_gems(gems)
    done = input("Enter to go again...")
    done = False
    clear_screen()