d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

l = list(input())
val = 0

# XXXX => 40, L => 50, XL => 40, LX => 60, X => 10, IX => 9, XI => 11
for i in range(len(l)):
    l[i] = d[l[i]]

for i in range(len(l)):
    if i == len(l)-1:
        val += l[i]
    elif l[i] >= l[i+1]:
        val += l[i]
    else :
        val -= l[i]
    
print(val)

