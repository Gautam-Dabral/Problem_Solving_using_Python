
def sec_min (l):
    mini , sec_mini = 100 , 100
    for items in l:
        if items[1] < mini:
            mini , sec_mini = items[1] , mini
        elif items[1] < sec_mini and items[1] > mini:
            sec_mini = items[1]
            
    return sec_mini
            

def main():
    n , l = int(input()) , []
    for i in range(n):
        name = input()
        score = float(input())
        temp = [name,score]
        l.append(temp)

    minimum2 = sec_min(l)
    
    for items in sorted(l):
        if items[1] == minimum2:
            print(items[0])

main()
        
        