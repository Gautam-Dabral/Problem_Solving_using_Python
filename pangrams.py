# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# It returns whether a string has all english alphabets or not (pangram)

def pangrams(s):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in alphabet:
        if i in s.lower():
            continue
        else :
            return('not pangram')
    
    return ('pangram')

def main():
    s = input('Enter a sentence : ')

    print(pangrams(s))

main()