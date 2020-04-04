# regular expressions

# import re for regular expressions
# create regex object with re.compile() function
# pass the object a string and it returns a match object
# match object has group() function that returns the actual matched text

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# group output using parenthesis
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

# matching multiple groups with pipe

# optional matching with ?

# matching 0 or more with *

# matching 1 or more with +

# matching specific repetitions with (){}

# return all occurrences of matches with .findall() function

# Character Classes:
# \d    digit from 0-9
# \D    any character not a digit from 0-9
# \w    any letter, digit, or the underscore character
# \W    any character that is not in \w
# \s    any space, tab, or newline character
# \S    any character that is not \s

# custom character classes using []

# ^ for beginning and $ for end

# wildcard character with .

# match anything with .*

# case insensitive matching

# substituting strings with .sub(,) method

# managing complex regexes

# re.IGNORECASE re.DOTALL re.VERBOSE
