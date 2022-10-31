
def transpose (l):

    transpose = []

    for i in range(len(l[0])):
        
        temp = []

        for j in l:
            temp.append(j[i])

        transpose.append(temp)

    return transpose

l = [ [1,2,3,4] , [5,6,7,8] , [9,10,11,12]]

print(transpose(l))