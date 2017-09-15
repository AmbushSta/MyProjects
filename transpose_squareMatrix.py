"""
Given a square matrix, returns its transpose.
Author: Michael Cowie
"""

def transpose(a_list):
    row_count = len(a_list)
    col_count = len(a_list[row_count - 1]) #Assuming square matrix
        
    temp = [[0 for _ in range(col_count)] for _ in range(row_count)]
    for rowIndex, row in enumerate(temp):
        for colIndex, col in enumerate(row):
            temp[colIndex][rowIndex] = a_list[rowIndex][colIndex]
    return temp
        

transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
