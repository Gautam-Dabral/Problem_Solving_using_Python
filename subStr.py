s = "hey tell me what is your name?"
x = 't is'

def subStr(x,s):
    for i in range(len(s)):
        if x[0] == s[i]:
            if x[1:] == s[i+1:i+len(x)]:
                return (i,i+len(x)-1)
    else : return -1

print(subStr(x, s))
