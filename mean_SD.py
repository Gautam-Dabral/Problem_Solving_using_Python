
t = ( ('a',5), ('b',3), ('c',6), ('d',2), ('e',8), ('f',-5), ('g',10) )

def mean(t):
    sum_t = 0
    for items in t:
        sum_t += items[1]
    return round((sum_t/len(t)) , 2)

def std_dev (t):
    m , sum_t = mean(t) , 0

    for items in t:
        sum_t += ( items[1] - m )**2

    return round( (sum_t/(len(t)-1))**(1/2) , 2)

print(mean(t) , std_dev(t))