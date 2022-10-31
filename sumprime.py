def isprime(m):
    if(m>0 and m%2!=0):
      for i in range ((m+1//2), 3):
        if(m%(m+1//2)==0):
            return(False)
    else:
        if(m==2):
            return(True)
        else:
            return(False)
    return(True)

def listofprime(l):
    list2=[]
    j=0
    for i in range (len(l)):
        if (isprime(l[i])):
            list2.append(l[i])
            j+=1
    return (list2)

def sumprime(l2):
    sum=0

    for i in range (len(l2)):
        sum+=l2[i]

    return sum


def main ():

    str_1=input('Enter the nos seperated by ","\n')
    list1 = str_1.split(',')
    
    for i in range (len(list1)):
      list1[i]=int(list1[i])  

    print('Sum of prime nos is',sumprime(listofprime(list1)))

main()