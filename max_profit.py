def maxprofit (k , profits):
    n = len(profits)

    profits_sorted = sorted(profits)
    sum , i = 0 , 1
    while k > 0 and profits_sorted[n-i] > 0 :
        sum+=profits_sorted[n-i]
        k , i = k-1 , i+1
    
    return sum

def main():
    lst = input('Enter the profits :\n').split(',')
    profits = []
    for i in range(len(lst)):
        profits.append(int(lst[i]))

    k = int(input('Enter the max no. of shares to buy : \n'))    
    
    print('Maximum profit is : ',maxprofit(k, profits))

main()

        

