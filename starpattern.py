
def star (s , n):

    if s == 'left-inverted':
        for i in range(1, n+1):
            for j in range(n+1-i):
                print('*', end='')
            print('')
    
    elif s == 'left':
        for i in range(n, 0, -1):
            for j in range(n+1-i):
                print('*', end='')
            print('')

    elif s == 'right-inverted':
        for i in range(1, n+1):
            for j in range(n+1-i):
                print('', end='*')
            print('')

    elif s == 'right':
        for i in range(n, 0, -1):
            for j in range(n+1-i):
                print('', end='*')
            print('')

    elif s == 'center-inverted':
        for i in range(n):
            for j in range(i):
                print(' ', end='')
            for k in range(n-i):
                print('*', end=' ')
            print('')
    
    elif s == 'center':
        for i in range(n):
            for j in range(n-i):
                print(' ', end='')
            for k in range(i+1):
                print('*',end=' ')
            print('')


        



#star('left-inverted', 5)
#star('left', 5)
#star('right-inverted', 5)
#star('right', 5)
star('center', 5)
print('')
star('center-inverted', 5)