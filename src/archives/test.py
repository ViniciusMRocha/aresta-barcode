def getArrow(column):
    total = column/4
    totalNoRemainder = column//4
    check = total-totalNoRemainder
    # print (check)
    if check == 0.25 or check == 0.5:
        print(">> ",column,check)
    elif check == 0.75 or check == 0.0:
        print("<< ",column,check)

getArrow(16)