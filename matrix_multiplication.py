
def Matrix_Mul (A , B):

    sum_t = 0
    C = [ [0 for i in range(len(B[0]))] for j in range(len(A)) ]

    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(B)):

                sum_t += A[i][k]*B[k][i]

            C[i][j] = sum_t
    
    return(C)

L1 = [[1,2,3],[4,5,6]]
L2 = [[7,8],[9,10],[11,12]]

print(Matrix_Mul(L1, L2))