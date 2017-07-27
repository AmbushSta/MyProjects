"""
Given a 2D graph, counts the occurence of the word "WIN".
All directions.

Author: Michael Cowie
"""

directions = [('N' , -1, 0), ('NE', -1, 1),
              ('E' ,  0, 1), ('SE',  1, 1),
              ('S' ,  1, 0), ('SW',  1, -1),
              ('W' ,  0, -1), ('NW', -1, -1)]


def countWinOccurence(user_map):
    occurences = 0
    twoDArray = user_map.split("\n")
    for row in range(len(twoDArray)):
        for col in range(len(twoDArray[row])):
            if twoDArray[row][col] == "W":
                occurences += countOccurencesFrom(row, col, twoDArray)
    return occurences

def countOccurencesFrom(row, col, user_map, goal_string = "IN"):
    if goal_string == "":
        return 1
    occurences = 0
    for _, row_add, col_add in directions:
        new_row = row + row_add
        new_col = col + col_add        
        if user_map[new_row][new_col] == goal_string[0]:
            occurences += countOccurencesFrom(new_row, new_col, user_map, goal_string[1:])
    return occurences

my_map = """
+------------+
|xxxxWxxxxxxx|
|xxxNIIxxxxxx|
|xxxxNxNxxxxx|
|xxxxxxxxxxxx|
+------------+
"""


occurence = countWinOccurence(my_map)
print(occurence) #3--Incomplete
