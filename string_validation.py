if __name__ == '__main__':
    s = input()
    ans = [0,0,0,0,0]
    for char in s:
        if char.isalpha() or char.isdigit():
            ans[0] = 1
            break
    for char in s:
        if char.isalpha():
            ans[1] = 1
            break
    for char in s:
        if char.isdigit():
            ans[2] = 1
    for char in s:
        if char.islower():
            ans[3] = 1
    for char in s:
        if char.isupper():
            ans[4] = 1
            
    for items in ans:
        if items == 1:
            print(True)
        else:
            print(False)
            