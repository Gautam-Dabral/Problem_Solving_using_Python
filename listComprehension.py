# If you want to create a 2 dimensional matrix and initialize it, make sure you initialize it in one
# shot using a nested range, and not in 2 copies like this, because these 2 copies will unintentionally
# combine 2 rows into copies of the same thing, and updates to one row will also
# update another row.

# and why is this happening; 
# well, that is because by making a single zerolist, and then making 4 copies of it, we
# have effectively created 4 names with the same list.

zerolist = [0 for i in range(3)] # [0, 0, 0]
l = [zerolist for j in range(4)]

l2 = [[0 for i in range(3)] for j in range(4)] # the right way

print(l) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(l2) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
l[1][1] = 7
l2[1][1] = 7
print(l) # [[0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0]]
print(l2) # [[0, 0, 0], [0, 7, 0], [0, 0, 0], [0, 0, 0]]
