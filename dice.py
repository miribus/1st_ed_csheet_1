import random

def ability_roller(sides, qty):
    sides = sides+1
    qty = qty+1
    bests = []
    for i in range(1, qty):
        num = random.randrange(1, sides)
        #print(num)
        bests.append(num)
    bests.sort()
    result = bests[-1]+bests[-2]+bests[-3]

    print(result)
    return result

def soclass():
    result = random.randrange(1, 101)
    return result