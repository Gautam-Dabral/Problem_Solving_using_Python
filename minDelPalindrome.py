
s1 = "abavaab" # => 2
s2 = "gaurav"  # => 3
s3 = "aba"     # => 0
s4 = "atlc"    # => 3
s5 = ""        # => 0


def minDel(s):
    if len(s) <= 1: return 0
    elif len(s) == 2: 
        if s[0] == s[1]: return 0
        else: return 1
    else:
        if s[0] != s[-1]:
            temp = s[:]
            temp.remove(s[-1])
            s.remove(s[0])
            return 1 + min(minDel(temp), minDel(s))
        else:
            return minDel(s[1:len(s)-1])

print(minDel(list(s1)))
print(minDel(list(s2)))
print(minDel(list(s3)))
print(minDel(list(s4)))
print(minDel(list(s5)))