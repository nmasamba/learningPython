
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a number x as input. It will then evaluate that number
and determine if it's a prime number. A prime number is a positive integer greater than 1 
that has no positive divisors other than 1 and itself. In other words, if you want to 
test if a number in a variable x is prime, then no other number should go into x evenly 
besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not. If there 
is a number between 1 and x that goes in evenly, then x is not prime.

Example input and output:
is_prime(2) would return True
is_prime(18) would return False                                                                                                                                                                                                                                                                                 

"""


def is_prime(x):
    if x < 2 :
        return False
    elif x == 3 or x == 2:
        return True
    else:
        for i in range(2, x-1):
            if x % i == 0 :
                return False
        else:
            return True