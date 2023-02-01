from functools import wraps
from time import time

# speed testing decorator
def speed_test (fn):
    @wraps(fn)
    def wrapper (*args, **kwargs):
        start_time = time()
        res = fn (*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed : {end_time-start_time}")
        return res
    return wrapper




@speed_test
def even_fibo_sum(x):
    t = []
    t.append(1)
    t.append(2)
    n = 2
    while True:
        n = t[-1] + t[-2]
        if n<x: t.append(n)
        else: break
    return sum(x for x in t if x%2==0)

print(even_fibo_sum(1000))
        
        
