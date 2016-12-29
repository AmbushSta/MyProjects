'''
Computes x^n in O(log n) time
Author: Michael Cowie
'''

def power(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power(x, n / 2) ** 2
    else:
        return power(x, n - 1) * x
