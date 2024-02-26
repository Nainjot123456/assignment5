import random

def rol():
    return random.randint(1, 6)

r = 0
while r != 6:
    r = rol()
    print("Yourolled a",r)