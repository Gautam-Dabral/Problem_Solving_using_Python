
# Grid Paths Problem using dynamic programming
# No. of possible paths from (0,0) to (m,n) with only right(->) and up (^) movement allowed
# zero (0) at any index (c,r) represents a hole (no path can pass from that point)
# 

gridtable = {}

def paths(m,n):

    for i in range(m+1):                               # creating the grid m x n
        for j in range(n+1):
            gridtable[(i,j)] = 0

    for r in range(n+1):
        for c in range(m+1):

            if  c==0 and r==0:                            # (0,0) is only 1 path, base case
                gridtable[(c,r)] = 1

            elif c==2 and r==4:                           # hole at (2,4)
                gridtable[(2,4)] = 0

            elif r==0:
                # lowest row, (no path below) only paths from left                                    
                gridtable[(c,r)] = gridtable[(c-1,r)]

            elif c==0:
                # left most column, (no path to the right) only paths from below                                   
                gridtable[(c,r)] = gridtable[(c,r-1)]
            else:
                # paths at (c,r) = paths from left(c-1,r) + paths from below(c,r-1)
                gridtable[(c,r)] = gridtable[(c-1,r)] + gridtable[(c, r-1)]       


def print_grid (m,n):
    for j in range(n,-1,-1):
        for i in range(m+1):
            print(gridtable[(i,j)], end=' ')
        print('')

paths(5,10)
print_grid(5,10)