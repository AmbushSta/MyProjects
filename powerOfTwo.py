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
x = int(input())

def highest_power(x):
    current_highest = 0
    while 2 ** current_highest <= x:
        current_highest += 1
    return current_highest - 1

current_highest = highest_power(x)

recursion_list = []

for power in range(current_highest + 1):
    recursion_list.append(2 ** power)
    recursion_list.append(2 ** power)

def euler169(user_input, current_stack = [], answer = set()):
    for index, num in enumerate(user_input):
        new_stack = current_stack + [num]
        if sum(new_stack) == 10:
            answer.add(tuple(new_stack))
            return
        elif sum(new_stack) < 10:
            euler169(user_input[index +1:], new_stack, answer)
    return answer

answer = euler169(recursion_list)
print(len(answer))
