"""Given a list it will return the maximum permutations of the given list"""

def perms(s, index = 0, sLength = None, answer = set()):
    if sLength == None:
        sLength = len(s)
    if index == sLength:
        answer.add(tuple(s))    
    s_List = list(s)
    for i in range(index,sLength):
        s_List[index],s_List[i] = s_List[i],s_List[index]
        perms(s_List,index + 1,sLength,answer) 
        s_List[index],s_List[i] = s_List[i],s_List[index]
    return answer

print(sorted(perms([5,6,7,10,11])))
