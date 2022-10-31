def gcd(m):

    i=min(m)
    print('i is ', i)

    while i>0:
        for j in range (len(m)):
            if(m[j]%i!=0):
                i=m[j]%i
                print('Now, i is ', i)
                break
        else:
            return i
    return 1
        
        
def main():
    lst=[]
    for i in range(2):
        lst.append(int(input('Enter number :')))
    print(lst)
    print('\ngcd is ', gcd(lst))

main()

