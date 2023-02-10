# input : ghftd:1246 , output : ftdgh
# input : rhdt:246 , output : trhd
# explanation : if the sum of the squares of the digits of the number after the : 
# is even , rotate the string 1 step to the right 
# else rotate 2 steps to the left
# print the rotated string

def sumOfSquares(l):
    return sum(map(lambda x: x*x , l))

s,l = input().split(':')
l = list(map(int, list(l)))
if sumOfSquares(l)%2 == 0:
    s = s[-1] + s[:len(s)-1]
else :
    s = s[2:] + s[:2]
print(s)