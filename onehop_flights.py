
def find_onehop (f):
    keys = list(sorted(f.keys()))
    pairs=()
    onehoppairs = [pairs]
    for keys in f:
        

def onehop (l):
    f = {}
    for i in range(len(l)):
        
        if(l[i][0] not in f):
            f[l[i][0]] = [l[i][1]]
        else:
            f[l[i][0]].append(l[i][1])

    find_onehop(f)
    return f
    

      
def main ():
    lstr=[(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]
    print(onehop(lstr))

main()
