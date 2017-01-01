'''
This was the beginning of a hackerrank question, although I cannot find
where the second half is.

So far, my code takes a user input of one number and prints all combinations
of a "+","-" or empty string between each consecutive number using backtracking.
'''

def plus_minus_empty(string, new_string = '', index = 0, answer = []):
    new_string += string[index]
    if index == len(string) - 1:
        answer.append(new_string)
        return
    for operator in ['+','-','']:
        plus_minus_empty(string, new_string + operator, index + 1, answer)
    return answer

user_input = input()
answer = plus_minus_empty(user_input)
for x in answer:
    print(x)
    
    
'''
Example: 
user_input = "123"
Output:
1+2+3
1+2-3
1+23
1-2+3
1-2-3
1-23
12+3
12-3
123
'''
