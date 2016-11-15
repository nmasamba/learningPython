
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a number n as input. It will then stringify that 
number and add up its digits then print the result. It does this by traversing through
the number, taking each digit in turn and adding it to the previously found total. When
all numbers have been added, the function returns a grand total.

Example input:
print digit_sum(25)

Example output:
7                                                                                                                                                                                                                                                                                                  

"""


def digit_sum(n):
    total = 0
    user_input = str(n)
    for num in user_input:
        num = int(num)
        total = num + total
    return total
    
print digit_sum(25)