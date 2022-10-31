

def sum_arr (arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

def birthday (s, d, m):
    count=0
    for i in range(len(s)-(m-1)):
        if sum_arr(s[i : i+m]) == d:
            print(s[i : i+m])
            count += 1
    
    if len(s) == m and sum_arr(s) == d:
        return 1
    
    return count

def main ():
    str1 = list(input('Enter an array (s) : ').split(' '))
    s=[]
    for i in range(len(str1)):
        s.append(int(str1[i]))

    d = int(input('Enter the birth day (d) :'))
    m = int(input('Enter the birth month (m) :'))
    
    print(birthday(s, d, m))

main()