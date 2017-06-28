"""
Very useful tricks that can be performed in python
"""

#Find the most frequent occruence of words in a single string seperated by a space using the max() function
test_string = "x x y z Michael-Cowie"
most_common = max(test_string, key = lambda x : test_string.split(" ").count(x))
print(most_common)  #1


#Tuple sorting by 2nd index.
tuple_list = [(10,9),(8,7),(6,5),(4,3),(2,1)]
print(sorted(tuple_list, key = lambda x : x[1]))  #[(2, 1), (4, 3), (6, 5), (8, 7), (10, 9)]


#Fill up someones ram ;)
x = [n for n in range(-2**62, 2**62)]


#Doubley nested dictionaries, made easy.
depth = 5
nested_dict = {x : dict() for x in range(depth)}
nested_dict[0][1] = 5 #Example
print(nested_dict[0][1]) #5


#How to represent a map, in the form of a x,y plane.
map_str = """\
+------------+                       #To traverse the graph, use the following list.
|    S       |                       #directions = [('N' , -1, 0), ('NE', -1, 1),
|            |                       #              ('E' ,  0, 1), ('SE',  1, 1),
|            |                       #              ('S' ,  1, 0), ('SW',  1, -1),
| G          |                       #              ('W' ,  0, -1), ('NW', -1, -1)]
|            |
+------------+
"""

map_str = map_str.split("\n") #alternatively you can use the method splitlines()
#Now index, row by column.
row = 1
column = 5
print(map_str[row][column]) #S
