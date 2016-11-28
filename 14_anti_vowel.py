

"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a string text as input. It will then return that string
without any vowels. Note that it does not count Y as a vowel.

Example input and output:
anti_vowel("Hey You!") should return "Hy Y!"                                                                                                                                                                                                                                                                        

"""


def anti_vowel(text):
    no_vowels = []
    
    for l in text:
        if l not in "aeiouAEIOU":
            no_vowels.append(l)
    return "".join(no_vowels)