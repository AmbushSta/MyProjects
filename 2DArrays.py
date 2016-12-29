'''Creates a 2DArray from input variables'''

column = int(input())
row = int(input())
matrix = [[0 for y in range(column)] for x in range(row)]
print(matrix)

'''
Notes:
2D matricies are created by column, and then row but are indexed
matrix[x][y] row by column
'''
