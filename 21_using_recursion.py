def twentyone(nums, stack = [], answer = set()):
    for index, num in enumerate(nums):
        new_stack = stack + [num]
        total = sum(new_stack)
        if total == 21:
            answer.add(tuple(new_stack))
        elif total < 21:
            twentyone(nums[index + 1:], new_stack, answer)
    return answer

answer = twentyone([1,9,11,5,6])
print(answer)
