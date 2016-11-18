
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a number x as input. It will then evaluate that number
and return that number's factorial. To calculate the factorial of a non-negative integer x, 
just multiply all the integers from 1 through x. 

Example input and output:
factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.                                                                                                                                                                                                                                                                                   

"""


def factorial(x):
    if x == 1:
        print 1
    else:
        print x * factorial(x-1)