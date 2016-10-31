"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program takes input from a user and prints our a pyglatin version of
that word. It introduces the following concepts:
- Using raw_input() to get input from the user
- Concatenation of strings using the '+' symbol
- String slicing using square brackets and indices to select subsections of strings
- Logical checking of size and alphanumeric (.isalpha()) state
- Use of methods such as .lower() to convert strings between upper and lower case

Example input:
HELLO

Example output:
ellohay 

"""




pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print "Your word: " + original
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    print "Pig Latin: " + new_word
else:
    print 'Sorry that word has not been recognised.'