
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a number x as input. It will then evaluate the input
and print True if the number is even, otherwise it will print False.

Example input:
is_even(463628)                                                                                                                                                                                                                                                                                                    

Example output:
True

"""


def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False