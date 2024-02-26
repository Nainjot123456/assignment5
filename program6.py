def rm(n):
    even = []
    for nm in n:
        if nm % 2 == 0:
            even.append(nm)
    return even

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = rm(number)

print("Original list:", number)
print("Cut-down list:",c)