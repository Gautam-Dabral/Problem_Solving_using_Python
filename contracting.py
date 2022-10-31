def contracting (l):
    absdiff = max(l)-min(l)     # max diff possible in the given list
    for i in range (len(l)-1):
        if( abs(l[i]-l[i+1]) < absdiff):
            absdiff = abs(l[i]-l[i+1])
        else:
            return False
    return True

        
def main():
    a=[10,7,4,1]
    print(contracting(a))

main()
        