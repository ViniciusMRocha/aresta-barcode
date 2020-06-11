# Adds a "0" to a 2 digit number
def addZero_twoDigits(check):
    if check <= 9:
        check = '0' + str(check)
    else:
        # Force to be string by adding ''
        check = '' + str(check)
    return check

# Adds "00" to a 1 digit number or "0" to a 2 digit number
def addZero_threeDigits(check):
    if check <= 9:
        check = '00' + str(check)
    elif check <= 99:
        check = '0' + str(check)
    else:
        #Force to be string by adding ''
        check = '' + str(check)
    return check