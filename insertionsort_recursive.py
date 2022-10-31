
def insertionsort (l):
    isort (l, len(l))

def isort (l, k):
    
    if k > 1:
        isort(l, k-1)          # isort l from 0 to k-2 and recursive
        insert(l, k-1)         # insert k-1 element in l

def insert (l, k):

    pos = k
    while pos > 0 and l[pos] < l[pos-1]:
        l[pos] , l[pos-1] = l[pos-1] , l[pos]
        pos -= 1



l = list(range(500,0,-1))

insertionsort(l)

print(l)