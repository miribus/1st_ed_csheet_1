import dice

def psionic_check(name):
    base = 100
    if name.char_class_abilities['INT'] > 15:
        for i in range(16, name.name.char_class_abilities['INT']+1):
            base-=3
    if name.char_class_abilities['WIS'] > 15:
        for i in range(16, name.name.char_class_abilities['INT']+1):
            base-=2
    if dice.normal(100, 1) >=  base:
        name.psionic = True
