
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a string as input. It will then return that string in
reverse. Use of [::-1] to help with this is (in this case) not allowed. The string text
should also contain special characters (for example, !, @, or #).

Example input and output:
reverse("abcd") should return "dcba"
reverse("madam") should return "madam"                                                                                                                                                                                                                                                                           

"""


def reverse(text):
    reversed_text = ""
    for l in range(len(text)):
        reversed_text += text[len(text)-1-l]
    return reversed_text
    