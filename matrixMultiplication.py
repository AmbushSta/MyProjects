"""
    Multiplies two matricies, else returns 0.
    Self Notes:
        Two matrix a x b and c x d will only be valid if b = c. The resulting
        matrix will have dimensions a x d.
    Author: Michael Cowie
"""

def matrixMultiplier(A, B):
    
    try:
        if len(A[0]) != len(B):
            return 0
    except: #Exception used when index out of range error
        return 0
    
    answer = [
        [sum(x * y for x, y in zip(col, row)) for col in zip(*B)] for row in A
    ]
    
    return answer
    
    

matrix1 = [[1,2],
           [3,4]]

matrix2 = [[1,2],
           [3,4]]

result = matrixMultiplier(matrix1, matrix2)
print(result) #[[7, 10], [15, 22]]
