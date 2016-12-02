

"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes two arguments - sequence and item. It will then return the
number of times the item occurs in the list. There is a list method in Python that you can use 
for this, but you should do it the long way for practice. The function should return an integer.
The item you input may be an integer, string, float, or even another list!

Example input and output:
count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).                                                                                                                                                                                                                                                                   

"""


def count(sequence, item):
    found = 0
    for i in sequence:
        if i == item:
            found += 1
    return found