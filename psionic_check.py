import dice


def psionic_check(name):
    print("###############################")
    print("#Rolling psionics....#")
    print("###############################")
    base = 100
    if name.char_abilities['INT'] > 15:
        for i in range(16, name.char_class_abilities['INT']+1):
            base-=3
    if name.char_abilities['WIS'] > 15:
        for i in range(16, name.char_class_abilities['WIS']+1):
            base-=2
    if name.char_abilities['CHA'] == 16:
        base-=1
    elif name.char_abilities['CHA'] == 18:
        base-=2
    if name.char_race == "GrayDwarf":
        base = base*2
    if dice.normal(100, 1) >=  base:
        name.psionic = True

    if name.psionic:
        print("###############################")
        print("#Holy shit... you're psionic!#")
        print("#Holy shit... you're psionic!#")
        print("#Holy shit... you're psionic!#")
        print("#Holy shit... you're psionic!#")
        print("###############################")
    else:
        print("Nope, not psionic.")