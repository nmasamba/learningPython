

"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes in a list of integers. It will then remove elements 
of the list that are the same.

Example input and output:
remove_duplicates([1,1,2,2]) should return [1,2].      

"""


def remove_duplicates(numbers):
    unduplicated = []
    for num in numbers:
        if num not in unduplicated:
            unduplicated.append(num)
    return unduplicated
            