import time

def isprime(a):
    if a<=1:
        return False  
    else:
        for i in range (2, int(a**(1/2))+1):
            if a%i==0:
                return False
        return True

def upto(n):
    start_time = time.time()
    for i in range (2,n+1):
        if i%2!=0:
            if isprime(i):
                print(i)
        elif i==2:
            print(i)
    end_time = time.time()
    print(f'time taken to check {n} numbers : ', end_time-start_time)
    print("********************")

def nprime(n):
    while n>0:
        i=0
        if(isprime(i)):
            print(i)
            print("\t")
            (n,i)=((n-1),(i+1))
        else:
            i+=1
    print("********************")

def menu ():
    print("\n********** Welcome **********")
    print("\nChoose an option : \n1. Check whether a no. is a prime no. or not\n2. Find prime nos. upto n\n3. Find first n prime nos.\n0. Exit")
   
    input_value = int(input())
    
    while 1>0 :
        if(input_value==0):
              break
        elif(input_value==1):
              a=int(input('\nEnter a no. : '))
              isprime(a)
        elif(input_value==2):
              a=int(input('\nEnter the no. upto which prime numbers are required : '))
              upto(a)
        elif(input_value==3):
              a=int(input('\nEnter the no. of prime numbers to be printed : '))
              nprime(a)
        else:
              print("\nError Encountered!, Enter a no between 0 and 3\n")
              menu()

menu()
        

