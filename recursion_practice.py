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
