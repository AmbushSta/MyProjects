"""Given a list returns all possible combinations of numbers that add to
21, prints into shell"""

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
                
    if len(answer) > 0:
        for an_answer in answer:
            print("The values ", end = "")
            for a_combination in an_answer:
                print("{} ".format(a_combination), end = "")
            print("add up to 21")

#Example
seq = [5, 6, 7,10,11,7,3]
twentyone(seq)
"""
Output
The values 10 11 add up to 21
The values 11 7 3 add up to 21
"""


#Fail case [1,9,11,5,6]
