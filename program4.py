import random

def rol(num):
    return random.randint(1, num)

num = int(input("enter faces would you like your die to have? "))
r = 0

while r != num:
    r = rol(num)
    print("Yourolled a",r)