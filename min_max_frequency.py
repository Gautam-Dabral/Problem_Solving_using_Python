
def max_freq (l):
    max_freq=0
    for i in range(len(l)):
        if l[i]==max(set(l), key = l.count):
            max_freq+=1
    return max_freq

def min_freq (l):
    min_freq=0
    for i in range(len(l)):
        if l[i]==min(set(l), key = l.count):
            min_freq+=1
    return min_freq

def freq (l,v):
    count = 0
    for i in range(len(l)):
        if (l[i]==v):
            count+=1
    return count

def frequency (l):
    max_f=max_freq(l)
    min_f=min_freq(l)
    (max,min)=([],[])

    for i in range(len(l)):
        if (max_f == freq(l, l[i]) and (l[i] not in max) ):
            max.append(l[i])
        elif (min_f == freq(l, l[i]) and (l[i] not in min) ):
            min.append(l[i])

    min.sort()
    max.sort()
    return ( min , max )

      
def main ():
    lstr=list(input('Enter the numbers seperated by ","\n').split(','))
    
    for i in range(len(lstr)):
        lstr[i]=int(lstr[i])

    print(frequency(lstr))

main()
