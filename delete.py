import math

def all_primes(upper_limit):
    if upper_limit < 3:
        return
    for a_prime in get_primes(upper_limit):
        print(a_prime)
        
def get_primes(upper_limit):
    current_number = 3
    if current_number > upper_limit:
        return
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
