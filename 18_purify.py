

"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes in a list of numbers. It will then return another list
with all odd numbers in the list, and returns the result. Do not directly modify the list 
you are given as input; instead, return a new list with only the even numbers.

Example input and output:
purify([1,2,3]) should return [2].                                                                                                                                                                                                                                                                   

"""


def purify(lst):
    purified = []
    for i in lst:
        if i % 2 == 0:
            purified.append(i)
    return purified