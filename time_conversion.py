

def timeConversion(s):
    # Write your code here
    new =s[0:2]
    if 'P' in s:
        s=s[0:8]
        new=int(new)
        if new < 12:
            new+=12
            new=str(new)
            return(new+s[2:])
        else:
            return(s)
    else:
        s=s[0:8]
        if new=='12':
            new='00'
            return(new+s[2:])
        else:
            return(s)            

        
if __name__ == '__main__':
    s = input('\nEnter the time in format hh:mm:ssAM/PM\n')
    print(timeConversion(s))
