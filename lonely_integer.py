
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
'''It returns an integer which only occurs once in the array 'a' '''

def lonelyinteger(a):
    # Write your code here
    for i in range(len(a)):
        counter=0
        for j in range (len(a)):
            if (a[i]==a[j]):
                if(counter <= 2):
                    counter+=1
                else:
                    break
        if(counter==1):
            return(a[i])        