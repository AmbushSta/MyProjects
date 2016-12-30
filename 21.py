"""
Takes a sequence of numbers as input from the user and prints
all possible sequence of numbers that add to 21.
Author: Michael Cowie
"""

def twentyone(seq):
    answer = []
    for index, seq_number in enumerate(seq):
        for subset_index in range(index + 1, len(seq)):
            current_path = [seq_number]
            for added_num in seq[subset_index:]:
                current_path.append(added_num)
                if sum(current_path) == 21:
                    answer.append(current_path)
                    break
                elif sum(current_path) > 21:
                    break
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


"""
Using Example numbers "5, 6, 7, 10, 11, 7, 3"
Output from example: 
The values 10 11 add up to 21
The values 11 7 3 add up to 21


Fail case [1,9,11,5,6] (missing 1 + 9 + 5 + 6), corrected using recursion method
"""
