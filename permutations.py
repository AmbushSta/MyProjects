import sys

"""
Given a sequence of numbers fromm the user input, prints all permutations of the sequence
Author: Michael Cowie
"""

def perms(s_List = [], index = 0, s_Length = None, answer = set()):
    if s_Length == None:
        s_Length = len(s_List)
    if index == s_Length:
        answer.add(tuple(s_List))    
    for i in range(index, s_Length):
        s_List[index], s_List[i] = s_List[i], s_List[index]
        perms(s_List, index + 1, s_Length,answer) 
        s_List[index] , s_List[i] = s_List[i], s_List[index]
    return answer

user_input = input()
if len(user_input.strip()) == 0:
    print("Please provide a sequence of space seperated numbers\n")
    sys.exit()
list_format = [int(x) for x in user_input.split()]

answer = perms(list_format)
if len(answer) == 0:
    print("No possible permutations")
else:
    print("The following combinations are all permutations from the input \"{}\"".format(" ".join(str(x) for x in list_format)))
    for solution in answer:
        print("{}".format(" ".join(str(x) for x in solution)))
""""
Example:
Input "5 6 7" should output:
The following combinations are all permutations from the input "5 6 7"
5 7 6
5 6 7
6 5 7
6 7 5
7 5 6
7 6 5
"""
