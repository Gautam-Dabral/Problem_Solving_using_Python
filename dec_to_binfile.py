
f = open('input_file.txt','r')
lst = f.read().splitlines()

d = {}
d['bintodec'] = []
d['dectobin'] = []

for i in range (len(lst)):

    if lst[i] == 'binary' or lst[i] == 'decimal':
        pass
    else:
        lst[i] = int(lst[i])

for i in range(len(lst)):
    if lst[i] == 'binary':
        for j in range(i+1, len(lst)):
            if type(lst[j]) == int :
                d['bintodec'].append ( str( int(str(lst[j]),2) ) )
            else:
                break
    elif lst[i] == 'decimal' :
        for j in range(i+1, len(lst)):
            if type(lst[j]) == int :
                d['dectobin'].append ( str( bin(lst[j]) )[2:])
            else:
                break

f.close()

f = open('output_file.txt', 'w')

for items in lst:
    f.write(str(items))
    f.write('\n')

f.write(20*'#')
f.write('\n')

for keys in d.keys():

    if keys == 'dectobin':
        f.write('decimal to binary')
        f.write('\n')
        for i in range(len(d['dectobin'])):
            f.write(d['dectobin'][i])
            f.write('\n')
    elif keys == 'bintodec':
        f.write('binary to decimal')
        f.write('\n')
        for i in range(len(d['bintodec'])):
            f.write(d['bintodec'][i])
            f.write('\n')
        

f.close()

        

