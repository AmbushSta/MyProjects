"""
Very useful tricks that can be performed in python
"""

#Find the most frequent occruence of words in a single string seperated by a space using the max() function
test_string = "x x y z Michael-Cowie"
most_common = max(test_string, key=lambda x: test_string.split(" ").count(x))
print(most_common)  #x


#Tuple sorting by 2nd index.
tuple_list = [(10,9),(8,7),(6,5),(4,3),(2,1)]
print(sorted(tuple_list, key=lambda x: x[1]))  #[(2, 1), (4, 3), (6, 5), (8, 7), (10, 9)]


#Fill up someones ram ;)
x = [n for n in range(-2**62, 2**62)]


#Doubley nested dictionaries, made easy.
requirements = ["x", "y", "z"]
nested_dict = {x : dict() for x in requirements}
nested_dict["x"][1] = 5 #Example
print(nested_dict["x"][1]) #5


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



#getting from standard input like a cool kid
x, y = [i for i in input().split()]



#Knowing when a generator is being returned.
def test1():
    return (x for x in range(10))
  
def test2():
    return [x for x in range(10)]
print(type(test1())) #<class 'generator'>
temp = test2()
print(type(temp))   #<class 'list'>



#Using a generator instead of list comprehension
generator = (x for x in range(3))
for x in generator:
    print(x) #0 1 2

    
#Understanding * and **
def x(**argv):
    print(argv) #{'variable': 'x'}
x(variable = "x")

def x(*argv):
    print(argv) #('x', 'y', 'z')
x("x","y","z")
