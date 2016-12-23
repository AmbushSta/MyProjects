'''
Prime generator, made to practice and learn generators and the yield keyword
'''
#Given an upper limit, prints all primes up to and including the given limit

import math

def all_primes(upper_limit):
    if upper_limit < 3:
        return
    current_number = 3
    for a_prime in get_primes(current_number):
        if a_prime > upper_limit:
            return
        print(a_prime)
        
def get_primes(current_number):
    while True:
        if is_prime(current_number):
            yield current_number
        current_number += 1
        
def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True