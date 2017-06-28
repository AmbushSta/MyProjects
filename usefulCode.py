"""
Contains small, but very useful code.
"""

#Find the most frequent occruence of words in a single string seperated by a space.
test_string = "x x y  "
most_common = max(test_string, key = lambda x : test_string.split(" ").count(x))
print(most_common)  #1

#Tuple sorting by 2nd index
tuple_list = [(10,9),(8,7),(6,5),(4,3),(2,1)]
print(sorted(tuple_list, key = lambda x : x[1]))  #[(2, 1), (4, 3), (6, 5), (8, 7), (10, 9)]

#Fill up someones ram ;)
x = [x for x in range(-2**62, 2**62)]
