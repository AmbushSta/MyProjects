'''
Eventually, prints "Hello World"
'''
import time
import random

current = ""
index = 0
hw = 'Hello World'
while index < len(hw):
    i = random.randint(ord(' '), ord('z') + 1)
    new_string = current + chr(i)
    print(new_string, end='\r')
    time.sleep(0.01)
    if chr(i) == hw[index]:
        current += chr(i)
        index += 1
