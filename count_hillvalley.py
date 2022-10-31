def counthv(l):
    hc,vc=0,0
    for i in range (1, len(l)-1):
        if((l[i]>l[i-1]) and (l[i]>l[i+1])):
            hc+=1
        if((l[i]<l[i-1]) and (l[i]<l[i+1])):
            vc+=1
    
    list1=[hc, vc]
    return list1

def main():
    #input_str = input('Enter a list of intergers seperated by ","\n')
    
   # new_list=input_str.split(',')
   # for i in range (len(new_list)):
   #     new_list[i] = int(new_list[i])

    new_list=[]              #enter a list of integers in code
    print(counthv(new_list))

main()