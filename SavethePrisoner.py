'''
n = no. of prisoners
m = no. of candies
s = starting chair
last candy is poisonous

'''

def prisoners (n,m,s):

    candyleft = None

    if n > m or n == m:
        candyleft = m
    else:
        candyleft = m%n

    #print(candyleft)

    if ((s -1 + candyleft) % n ) == 0:
        return n
    else:
        return ((s -1 + candyleft) % n )



print(prisoners(3, 7, 3))
