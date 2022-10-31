
def sublist (l1, l2):
  
    if l1 == []:
        return True
        
    for i in range(len(l2)):

        if l1[0] == l2[i]:
            pos = i
            
            for j in range(1 , len(l1)):
                
                if l1[j] == l2[pos+1]:
                    pos += 1
                
                else:
                    break
            else:
                return True
            
    return False
        



print( sublist([2],[2,2,3,4,5]) )
print(	sublist([2,3,4],[2,2,3,4,5]) )