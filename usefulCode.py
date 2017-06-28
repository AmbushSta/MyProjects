"""
Contains small, but very useful code.
"""

#Find the most frequent letter in a string using the max() function
test_string = "x x y  "
most_common = max(test_string, key = lambda x : test_string.split(" ").count(x))
print(most_common)
