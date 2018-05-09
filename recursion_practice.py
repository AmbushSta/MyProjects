'''
Displays all the combinations of the given input.
e.g 
    Input: 123
    Output: 123
            12 3
            1 23
            1 2 3
'''
def digitCombinations(us):
    if len(us) < 2:
        print(us)
    rec(us, us[0])
    
def rec(us, cs, index=1):
    if len(us) == index:
        print(cs)
    else:
        rec(us, cs + us[index], index + 1)
        rec(us, cs + " " + us[index], index + 1)
    
digitCombinations("123")

'''
Computes the binary combinations of numbers up of length n
'''
def bc(ui, current_string = 0, stack=[]):
    if current_string < ui:
        for i in [str(x) for x in ["0", "1"]]:
            new_stack = stack + [i]
            bc(ui, current_string + 1, new_stack)
    else:
        print("".join(stack))
bc(4)

'''
Displays the combinations of the input digits
'''



'''
Computes x^n in O(log n) time
'''

def power(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power(x, n / 2) ** 2
    else:
        return power(x, n - 1) * x
