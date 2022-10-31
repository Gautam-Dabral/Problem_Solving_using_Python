# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
''' It returns an array showing the corresponding number of occurences 
for each element of the array "queries" when found in the array "strings" '''


def matchingStrings(strings, queries):
    # Write your code here
    result=[]
    
    for i in range (len(queries)):
        counter=0
        for j in range (len(strings)):
            if strings[j] == queries[i]:
                counter+=1
        
        result.append(counter)
        
    return result
            
            