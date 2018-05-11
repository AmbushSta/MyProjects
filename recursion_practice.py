'''
Given a chocolate bar of size r * c, where r = the height and c = the width, Calculates the minimum amount of snaps
it will take for the chocolate be to of all one size.
'''
def rec(r, c):
    if r == 1:
        return c - 1
    elif c == 1:
        return r - 1
   
    if r % 2 == 0 and c % 2 == 0:
        return 1 + rec(r, c//2) + rec(r, c//2)
    elif r  % 2 == 0 and c % 2 != 0:
        return 1 + rec(r//2, c) + rec(r//2, c)
    elif r % 2 != 0 and c % 2 == 0:
        return 1 + rec(r, c//2) + rec(r, c//2)
    else:
        return 1 + rec(r, c//2) + rec(r, c - c//2)
           
print(rec(20,30))

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
MergeSort
'''

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(array):
    if len(array) < 2:
        return array
    pivot = len(array)//2
    left = mergesort(array[:pivot])
    right = mergesort(array[pivot:])
    return merge(left, right)
    
print(mergesort([3,2,1]))


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
