"""
Link to useful cheatsheet:
https://github.com/tartley/python-regex-cheatsheet/blob/master/cheatsheet.rst
"""

import re

pattern1 = "The quick brown fox jump over the lazy dog"
pattern2 = "12 3 1444 56 777 88 a bbbb cc ?? a sentence"
pattern3 = "Hello my name is x and I x will be repeating my name twice"

#Using sub
print(re.sub("x","Michael Cowie",pattern3)) #Hello my name is Michael Cowie and I Michael Cowie will be repeating my name twice

#using search
print(re.search(".*1", pattern2).group())   #12 3 1
print(re.search("^[a-zA-Z\s]*$", pattern1)) #The entire string

#using findall
print(re.findall("\d{2}", pattern2))        #['12', '14', '44', '56', '77', '88']

#using split
print(re.split(".*the", pattern1))          #['', ' lazy dog']
