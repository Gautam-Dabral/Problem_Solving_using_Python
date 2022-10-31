import time

def isprime_eratosthenes(a):
    if a<=1:
        return False  
    else:
        for i in range (2, int(a**(1/2))+1):
            if a%i==0:
                return False
        return True


def upto_nprime(n):
    start_time = time.time()
    for i in range (2,n+1):
        if i%2!=0:
            if isprime_eratosthenes(i):
                print(i)
        elif i==2:
            print(i)

    end_time = time.time()
    print(f'time taken to check {n} numbers : ', end_time-start_time)


def main ():
    n = int(input('Enter the no upto which, prime nos are required : '))
    upto_nprime(n)

main()


