# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # creating the frequency array
    freq = [0]*k
    for i in range(len(s)):
        freq[s[i]%k] += 1
        
    maxlen = min(freq[0], 1)
    
    for i in range(1, k//2+1):
        if (i != k-i):
            maxlen += max(freq[i], freq[k-i])
        else:
            maxlen += min(freq[k//2], 1)
    return maxlen