'''
Eventually, prints "Hello World"
'''
import time
import random

current = ""
i = 0
hw = 'Hello World'
while i < len(hw):
    letter = random.randint(ord(' '), ord('z') + 1)
    new_string = current + chr(letter)
    
    if chr(letter) == hw[i]:
        current += chr(letter)
        i += 1
        
    print(new_string, end='\r')
    time.sleep(0.01)
