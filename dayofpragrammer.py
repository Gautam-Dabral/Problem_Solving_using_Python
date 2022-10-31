
def julian (y):
    
    if y%4 == 0:
        return ('12.09.'+ str(y))
    else:
        return ('13.09.'+ str(y))

def gregorian (y):

    if y%400==0 or (y%4==0 and y%100 != 0):
        return ('12.09.'+ str(y))
    else:
        return ('13.09.'+ str(y))


def dayofprogrammer (year):

    if year < 1918 :
        date = julian (year)

    elif year == 1918:
        return '26.09.1918'

    else:
        date = gregorian (year)

    return date
        

print(dayofprogrammer(1984))