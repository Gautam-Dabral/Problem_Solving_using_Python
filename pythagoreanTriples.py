
def isValidTriple(t):
    return t[0]**2 + t[1]**2 == t[2]**2

def myJoin(l):
    for i in range(len(l)):
        l[i] = str(l[i])
    return ','.join(l)

def mySplit(s):
    s = s.split(',')
    return list(map(int, s))

def pythagoreanTriples(n):
    l = ((i,j,k) for i in range(1,n+1) for j in range(1,n+1) for k in range(1,n+1))

    l_unique = list( map( mySplit, set( map( myJoin, map( sorted, l ) ) ) ) )
    
    return tuple(filter(isValidTriple, l_unique))


print(pythagoreanTriples(25))