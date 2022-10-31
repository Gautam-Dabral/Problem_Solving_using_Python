from time import time

fibtable ,fibtable_d = {} , {}

def fibo(n):                          # recursive implementation
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_memoized(n):                  # recursive implementation using memory table / Memoized

    if n in fibtable.keys():
        return fibtable[n]
    elif n==0 or n==1:
        value = 1
    else:
        value = fibo_memoized(n-1)+fibo_memoized(n-2)
    
    fibtable[n] = value

    return fibtable[n]

def fibo_dynamic(n):                     # dynamic programming
                                            
    fibtable_d[0] = 0
    fibtable_d[1] = 1

    for i in range(2,n+1):
        fibtable_d[i] = fibtable_d[i-1] + fibtable_d[i-2]

    return fibtable_d[n]

    


start = time()
print(fibo(30))
end = time()
print('Time taken : ', end-start)

start = time()
print(fibo_memoized(300))
end = time()
print('Time taken : ', end-start)

start = time()
print(fibo_dynamic(300))
end =time()
print('Time taken : ', end-start)