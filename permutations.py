"""
Given a list it will return the maximum permutations of the given list
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

print(sorted(perms([5,6,7])))
