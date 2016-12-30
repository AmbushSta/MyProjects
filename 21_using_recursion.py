"""
Takes a sequence of numbers as input from the user and prints
all possible sequence of numbers that add to 21.
Author: Michael Cowie
"""

def twentyone(nums, stack = [], answer = set()):
    for index, num in enumerate(nums):
        new_stack = stack + [num]
        total = sum(new_stack)
        if total == 21:
            answer.add(tuple(new_stack))
        elif total < 21:
            twentyone(nums[index + 1:], new_stack, answer)
    return answer

user_input = input()
list_format = [int(x) for x in user_input.split()]
answer = twentyone(list_format)

if len(answer) == 0:
    print("No combination of numbers add to 21")
for solution in answer:
    print("The values ", end = "")
    for number in solution:
            print("{} ".format(number), end = "")
    print("add up to 21")
    
    
'''
Reccomended test:
"1 9 11 5 6" has the correct output and fixes my previous attempt not using backtracking
The values 1 9 11 add up to 21
The values 1 9 5 6 add up to 21
'''
