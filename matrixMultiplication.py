"""
    Multiplies two matricies, else returns 0.
    Self Notes:
        Two matrix a x b and c x d will only be valid if b = c. The resulting
        matrix will have dimensions a x d.
    Author: Michael Cowie
"""

def multiply_two_matricies(A, B):
    
    try:
        if len(A[0]) != len(B):
            raise Exception("Mate you can't multiply these")
    except IndexError: #Exception used when index out of range error
        raise Exception("Mate you can't multiply these")
    
    answer = [
        [sum(x * y for x, y in zip(col, row)) for col in zip(*B)] for row in A
    ]
    
    return answer
    
    

matrix1 = []

matrix2 = [[1,2],
           [3,4]]

result = multiply_two_matricies(matrix1, matrix2)
print(result) #[[7, 10], [15, 22]]
