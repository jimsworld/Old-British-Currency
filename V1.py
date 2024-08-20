current = float(input("How much do you have on you?: £"))
unit = input("How should we convert it? (s)hilling, (d)pence or (f)farthing: ")
if unit.upper() == "S":
    conversion = current / 0.05
    print("You currently have: " + str(conversion) + " shillings")
elif unit.upper() == "D":
    conversion = current / 0.00416
    print("You currently have: " + str(conversion) + " pence")
elif unit.upper() == "F":
    conversion = current / 0.00104
    print("You currently would have: " + str(conversion) + " farthings")
