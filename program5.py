def convert(gal):
    lit = gal * 3.78541
    return lit


while True:
    g = float(input("gallons of gasoline do you have? (press a negative value to exit): "))

    if g < 0:
        print("End program")
        break

    liter = convert(g)
    print("You have", liter, "liters of gasoline.")