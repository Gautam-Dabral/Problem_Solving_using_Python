
from time import time

def insertionsort (l):

    for i in range(len(l)):

        position = i

        while position > 0 and l[position] < l[position-1]:

            l[position] , l[position-1] = l[position-1] , l[position]
            position -= 1


l = list(range(3000,0,-1))

start = time()
insertionsort(l)
end = time()

print(l)

print('Time Taken :', end-start)
