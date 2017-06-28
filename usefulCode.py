"""
Contains small, but very useful code.
"""

#Finds the most frequent occurence of words in a given string seperated by spaces.
test_string = "x x y  "
most_common = max(test_string, key = lambda x : test_string.split(" ").count(x))
print(most_common)
