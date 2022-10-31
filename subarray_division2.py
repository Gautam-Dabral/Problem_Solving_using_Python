

def pickingNumbers(a):

    a.sort()
    l =  0
    print(a)

    for i in range(len(a)):
            
        newl = 0

        for j in range(i,len(a)):
            
            if abs(a[i] - a[j]) <= 1:
                newl+=1

        if l <= newl :
            l = newl
    
    print(l)
         

def main():
    a = '7 12 13 19 17 7 3 18 9 18 13 12 3 13 7 9 18 9 18 9 13 18 13 13 18 18 17 17 13 3 12 13 19 17 19 12 18 13 7 3 3 12 7 13 7 3 17 9 13 13 13 12 18 18 9 7 19 17 13 18 19 9 18 18 18 19 17 7 12 3 13 19 12 3 9 17 13 19 12 18 13 18 18 18 17 13 3 18 19 7 12 9 18 3 13 13 9 7'
    
    b = a.split()

    c= []
    for items in b:
        c.append(int(items))
        
    #pickingNumbers([1,1,1,2,2,2,4,4,4,5,5,5,5,5,5,6,6,6,6,8,8,8,8,8,9,9,9])
    pickingNumbers(c)
main()