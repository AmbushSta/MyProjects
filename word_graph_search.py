"""
Given a 2D graph, counters the occurence of the keyword given.
All directions.
"""

directions = [('N' , -1, 0), ('NE', -1, 1),
              ('E' ,  0, 1), ('SE',  1, 1),
              ('S' ,  1, 0), ('SW',  1, -1),
              ('W' ,  0, -1), ('NW', -1, -1)]


def count_Keyword_Occurence(user_map, keyword):
    occurences = 0
    twoD_Array = user_map.split("\n")
    row_length = len(twoD_Array)
    for row in range(row_length):
        for col in range(len(twoD_Array[row])):
            if twoD_Array[row][col] == keyword[0]:
                occurences += count_Occurences_From(row, col, twoD_Array, keyword[1:])
    return occurences

def count_Occurences_From(cur_row, cur_col, twoD_Array, keyword):
    if keyword == "":
        return 1
    
    occurences = 0
    for direction, dir_row, dir_col in directions:
        new_row = cur_row + dir_row
        new_col = cur_col + dir_col
        if twoD_Array[new_row][new_col] == keyword[0]:
            occurences += count_Occurences_From(new_row, new_col, twoD_Array, keyword[1:])
            
    return occurences

my_map = """\
+------------+
|xxPYTHONxxxx|
|xxYxxxxxxxxx|
|xxTHONxxPYTH|
|xxxxxxxxxxNO|
+------------+
"""


occurence = count_Keyword_Occurence(my_map, "PYTHON")
print(occurence) #3













"""
Given a 2D graph, counts the occurence of the word "WIN".
All directions.
"""

directions = [('N' , -1, 0), ('NE', -1, 1),
              ('E' ,  0, 1), ('SE',  1, 1),
              ('S' ,  1, 0), ('SW',  1, -1),
              ('W' ,  0, -1), ('NW', -1, -1)]


def count_Win_Occurence(user_map):
    occurences = 0
    twoD_Array = user_map.split("\n")
    for row in range(len(twoD_Array)):
        for col in range(len(twoD_Array[row])):
            if twoD_Array[row][col] == "W":
                occurences += count_Occurences_From(row, col, twoD_Array)
    return occurences

def count_Occurences_From(row, col, user_map, goal_string = "IN", direction_list = []):
    if goal_string == "":
        print("Possible solution : " + " ".join(direction_list))
        return 1
    occurences = 0
    for direction, row_add, col_add in directions:
        new_row = row + row_add
        new_col = col + col_add        
        if user_map[new_row][new_col] == goal_string[0]:
            direction_stack = direction_list + [direction]
            occurences += count_Occurences_From(new_row, new_col, user_map, goal_string[1:], direction_stack)
    return occurences

my_map = """\
+------------+
|xxxxWxxxxxxx|
|xxxNIIxxxxxx|
|xxxxNxNxxxxx|
|xxxxxxxxxxxx|
+------------+
"""


occurence = count_Win_Occurence(my_map)
print(occurence) #4

"""
Possible solution : SE SE
Possible solution : SE SW
Possible solution : S S
Possible solution : S W
"""
