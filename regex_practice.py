"""
Link to useful cheatsheet:
https://github.com/tartley/python-regex-cheatsheet/blob/master/cheatsheet.rst

or

import re
help(re) 

For visual learning, https://regexr.com/
"""
import re

pattern1 = "The quick brown fox jump over the lazy dog"
pattern2 = "12 3 1444 56 777 88 a bbbb cc ?? a sentence"
pattern3 = "Hello my name is x and I x will be repeating my name twice"
space_split = "a    b c      d"
abc123 = "abc123"
string_with_newlines = """something
someotherthing"""

#Using sub
print(re.sub("x","Michael Cowie",pattern3)) #Hello my name is Michael Cowie and I Michael Cowie will be repeating my name twice

#using search      Attempts to match regex, allowing for substrings
print(re.search(".*1", pattern2).group())   #12 3 1
print(re.search("^[a-zA-Z\s]*$", pattern1)) #The entire string

#using match       Attempts to match from the beginning of the string
print(re.match("[a-zA-Z\d]{3}", abc123)) #abc
print(re.match("bc123", abc123)) #fails
print(re.match("a(a|b)c",abc123)) #abc, not to be confused with "aa|bc"

#using findall
print(re.findall("\d{2}", pattern2))        #['12', '14', '44', '56', '77', '88']

#using split
print(re.split(".*the", pattern1))          #['', ' lazy dog']
print(re.split("\s+", space_split)) #['a', 'b', 'c', 'd']


# greedy vs non-greedy
# greedy = matches the longest string possible
# non-greedy = matches the shortest string possible

x = "<em>Hello World</em>"
print(re.match("<.+?>", x).group(0)) # non-greedy. Matches "<em>"
print(re.match("<.+>", x).group(0)) #greedy. Matches "<em>Hello World</em>"
