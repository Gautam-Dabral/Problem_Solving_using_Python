# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs , sock_dict = 0 , {}
    
    for items in ar:
        if items not in sock_dict.keys():
            sock_dict[items] = 1
        else:
            sock_dict[items] += 1
            
    for keys in sock_dict.keys():
        pairs += sock_dict[keys]//2
        
    return pairs
            