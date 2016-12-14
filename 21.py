"""Given a list returns all possible combinations of numbers that add to
21, prints into shell"""

def twentyone(seq):
    answer = []
    current_path = []
    
    for index, seq_number in enumerate(seq):
        for subSetIndex in range(index + 1,len(seq)):
            current_path = [seq_number]
            for added_num in seq[subSetIndex:]:
                current_path.append(added_num)
                if(sum(current_path)) == 21:
                    answer.append(current_path)
                    break
                elif (sum(current_path)) > 21:
                    break
                
    if len(answer) > 0:
        for anAnswer in answer:
            print("The values ", end = "")
            for value in anAnswer:
                print("{} ".format(value), end = "")
            print("add up to 21")

#Example
seq = [5, 6, 7,10,11,7,3]
twentyone(seq)
