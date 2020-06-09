def getArrow(isle):
    total = isle/4
    totalNoRemainder = isle//4
    check = total-totalNoRemainder
    # print (check)
    if check == 0.25 or check == 0.5:
        print(">> ",isle,check)
    elif check == 0.75 or check == 0.0:
        print("<< ",isle,check)

getArrow(16)