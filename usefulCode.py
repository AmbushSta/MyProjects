"""
Contains useful tricks that are very useful when programming in python.
"""

#Find the most frequent occruence of words in a single string seperated by a space.
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
