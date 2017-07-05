"""
Problem: Given the numbers 1 to 9 in ascending order, add a "+", "-" or empty string
between two numbers, so that the numbers can sum to 100. Find the solution
with the minimal numbers of "+" and "-" symbols.
"""
query = "123456789"

def rec(string, new_string = "", index = 0):
    new_string += string[index]
    if index == len(string) - 1:
        yield new_string
    else:
        for operand in ["+", "-", ""]:
            yield from rec(string, new_string + operand, index + 1)
    
solutions = (x for x in rec(query) if eval(x) == 100)
optimal = min(solutions, key = lambda x : x.count("+") + x.count("-")) #'123-45-67+89'
