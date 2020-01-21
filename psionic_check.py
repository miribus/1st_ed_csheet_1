import dice


def psionic_check(name):
    print("###############################")
    print("#Rolling psionics....#")
    print("###############################")
    base = 1000
    if name.char_abilities['INT'] > 16:
        for i in range(17, name.char_abilities['INT']+1):
            base-=25
    if name.char_abilities['WIS'] > 16:
        for i in range(17, name.char_abilities['WIS']+1):
            base-=15
    if name.char_abilities['CHA'] > 16:
        for i in range(17, name.char_abilities["CHA"]+1):
            base-=5
    if name.char_race == "GrayDwarf":
        base = base*2
    roll = dice.normal(1000, 1)
    if roll >=  base:
        name.psionic = True
    print(roll, base)
    if name.psionic:
        print("###############################")
        print("#Holy shit... you're psionic!#")
        print("#Holy shit... you're psionic!#")
        print("#Holy shit... you're psionic!#")
        print("#Holy shit... you're psionic!#")
        print("###############################")
    else:
        print("Nope, not psionic.")