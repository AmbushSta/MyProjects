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
print(re.match("a(a|b)c", abc123)) #abc, not to be confused with "aa|bc"

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

# Search and replace using capturing groups can be very useful when given a known data structure for a lot of data that needs to be transferred to something new.
# Take an example where you're given a large file with two seperated key values by a space and need to pass them into a new function.
keys = """key1 key2
key2 key3
key4 key5
"""

for key_group in keys.split('\n'):
    print(re.sub('(\w*) (\w*)', 'generic_function_name(\'\g<1>\', \'\g<2>\'),', key_group))

# will output
# generic_function_name('key1', 'key2'),
# generic_function_name('key2', 'key3'),
# generic_function_name('key4', 'key5'),


