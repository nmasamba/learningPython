

"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes two strings - text and word. It will return the 
text with the word you chose replaced with asterisks. In other words, the text is printed
with the specified word censored.

Example input:
censor("bloody word is gone", "bloody")                                                                                                                                                                                                                                                                    

Example output:
****** word is gone  

"""


def censor(text, word):
    wordlist = text.split()
    for i in range(0, len(wordlist)):
        if wordlist[i] == word:
            wordlist[i] = "*" * len(word)
    print " ".join(wordlist)
    
