"""
Takes a sequence of tuples seperated by space and an integer at the end indicating
which index to sort the tuples by
e.g.
input: (1,2) (3,4) (5,6) 1
output: ['(1,2)', '(3,4)', '(5,6)']
"""

x = input()
tuples = x.split(" ")
index = int(tuples.pop())

result = sorted(tuples, key = lambda x : x[index])
print(result)
