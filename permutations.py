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
list_format = [int(x) for x in user_input.split()]
answer = perms(list_format)
if len(answer) == 0:
    print("You have given a list of length zero")
else:
    print("The following sequence are all permutations from the input sequence {}".format("".join(str(x) for x in list_format)))
    for solution in answer:
        print("{}".format("".join(str(x) for x in solution)))
