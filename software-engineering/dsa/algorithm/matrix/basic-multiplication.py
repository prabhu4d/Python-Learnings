"""
   the number of columns in the first matrix must be equal to the number of rows in the second matrix.

"""

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
    
B = [[9,8,7,1],
     [6,5,4,1],
     [3,2,1,1]]

C = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

    
print(C)