def getArrow(column):
    total = column/4
    totalNoRemainder = column//4
    check = total-totalNoRemainder
    if check == 0.0 or check == 0.75:
        print(">> ",column,check)
    elif check == 0.25 or check == 0.5:
        print("<< ",column,check)

for i in range(1,17):
    getArrow(i)