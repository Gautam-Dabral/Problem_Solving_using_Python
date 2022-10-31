def matched (list):
    counter=0
    for i in range (0, len(list)):
        if (list[i]=='('):
            #list=list[i+1:]
            counter+=1
        elif (list[i]==')'):
            counter-=1
    if(counter==0):
        return(True)
    else:
        return(False)


def main ():
    list=input()
    print(matched(list))

main()