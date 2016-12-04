

"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes in a list of integers. It will then return the 
product of all of the elements in the list.

Example input and output:
product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).      

"""


def product(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total