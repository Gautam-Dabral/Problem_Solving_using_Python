
# Selecting the minimum value from the list and swap with the element at the first index
# Repeat the steps for all the indices in the list

from time import time

def selection_sort (l):
    
    for index in range(len(l)):

        minpos = index

        for i in range(index,len(l)):

            if l[i] < l[minpos]:

                minpos = i

        l[minpos] , l[index ]= l[index] , l[minpos]
    


l = list(range(1000,0,-1))

s_time = time()

selection_sort(l)

e_time = time()

print(l)
print('Time taken :', e_time - s_time)