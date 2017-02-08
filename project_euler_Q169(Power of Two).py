'''
Project Euler question 169
Define f(0) = 1 and f(n) to be the number of ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.
For example f(10) = 5 since there are five ways to express 10:
1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8
what is (n) for a given n
'''
import math

x = int(input())
highest_power = math.floor(math.log(x,2))
recursion_list = []

for power in range(highest_power + 1):
    for _ in range(2):
        recursion_list.append(2 ** power)

def euler169(nums, current_stack = [], answer = set()):
    for index, num in enumerate(nums):
        new_stack = current_stack + [num]
        total = sum(new_stack)
        if total == x:
            answer.add(tuple(new_stack))
            #return
        elif total < x:
            euler169(nums[index +1:], new_stack, answer)
    return answer
answer = euler169(recursion_list)
print(len(answer))
