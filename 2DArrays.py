'''Creates a 2DArray from input variables'''

x = int(input())
y = int(input())
column, row = x, y
matrix = [[0 for x in range(column)] for y in range(row)]
print(matrix)

'''
Note:
2D matricies are created by column, and then row but are indexed
matrix[x][y] row by column
'''
