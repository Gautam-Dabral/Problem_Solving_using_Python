# l1 and l2 have same no of elements


def domino (l1, l2):                         # Memoized Recursive 

    dominotable , sum = [] , 0

    dominotable[0] == 0:                         # Empty list / Base Case
    dominotable[1] == abs(l1[0]-l2[0])

    elif len(l1) == 2:                       # 1 element left in both lists, hence only vertical arrangement possible
        return abs( l1[0]-l2[0] )  
    
    else:
        #whichever is maximum ( vertical elements + rest of the list    or      2 horizontal elements + rest of the list )
        value     =     max (abs(l1[0]-l2[0]) + domino(l1[1:], l2[1:]) , abs(l1[0]-l1[1]) + abs(l2[0]-l2[1]) + domino(l1[2:], l2[2:]))
        
    dominotable[(l1[0],l2[0])] = value        # adding value to table
           

    return max(dominotable.values())          # returns maximum value in the memory table 



def main():

    n = eval(input())                         # No of elements in l1 and l2
    
    l1 = input().split()                      # n elements of l1 seperated by blank space, hit enter
    l2 = input().split()                      # n elements of l2 seperated by blank space, hit enter

    for i in range(n):
        # Converting to int
        l1[i] = int(l1[i])
        l2[i] = int(l2[i])

    print(domino(l1,l2))

main()