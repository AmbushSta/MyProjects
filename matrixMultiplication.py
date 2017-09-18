"""
    Self Notes:
        Two matrix a x b and c x d will only be valid if b = c. The resulting
        matrix will have dimensions a x d.
    Author: Michael Cowie
"""

def multiply_matricies(A, B):
    if len(A[0]) != len(B):
        raise Exception("Mate you can't multiply these")
    
    return [
        [sum(x * y for x, y in zip(col, row)) for col in zip(*B)] for row in A
    ]
    
    

matrix1 = [[1,2],
           [3,4]]

matrix2 = [[1,2],
           [3,4]]

result = multiply_matricies(matrix1, matrix2)
print(result) #[[7, 10], [15, 22]]
