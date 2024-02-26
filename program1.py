import random

nm = int(input("dice do you want to roll? "))
s = 0

for i in range(nm):
    w = random.randint(1, 6)
    s += w

print("sum of the numbers rolle is:",s)