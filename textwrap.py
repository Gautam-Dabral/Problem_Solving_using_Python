import textwrap

def wrap(string, max_width):
    
    n  = len(string)
    m = max_width
    
    for i in range (n//m):
        
        string = string[:m] + '\n' + string[m:]
        m += ( max_width + 1)  
        
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)