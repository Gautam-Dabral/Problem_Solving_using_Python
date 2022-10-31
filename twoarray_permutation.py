
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
# It return 'YES' if there exits a permutation of arrays A & B, such that A[i] + B[i] >= k for all values of i, else it returns 'NO' .


def twoarrays (k, A, B):
    A , B = sorted(A) , sorted(B)

    print(A,B)

    for i in range(len(A)):
        for j in range(i, len(B)):
            if ( k - A[i] <= B[j] ):
                (B[i] , B[j]) = (B[j] , B[i])
                break
        else :
            return ('NO')
    
    return ('YES')

def main ():
    k = int(input('Enter the value of k : '))

    str1 = list(input('Enter array A : ').split(','))
    A = []
    for i in range(len(str1)):
        A.append(int(str1[i]))

    str2 = list(input('Enter array B : ').split(','))
    B = []
    for i in range(len(str2)):
        B.append(int(str2[i]))
    
    print(A, B)

    print(twoarrays(k, A, B))

main()