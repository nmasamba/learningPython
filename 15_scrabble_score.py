

"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a string word as input. It will then return the
equivalent scrabble score for that word. The assumption is that the input is only one
word containing no spaces or punctuation, and it will only work when given non-empty strings.

Example input and output:
scrabble_score("magnanimous") should print a score of 16                                                                                                                                                                                                                                                                      

"""


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    total = 0
    for l in word:
        total += score[l.lower()]
    print total