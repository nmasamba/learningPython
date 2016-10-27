
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is a divergence from the quintessential 'hello world' first
program.

It utilises variables and mathematical operands to calculate the tip after a 
meal, then it prints that value back to the user.

"""

# variables to be used for calculations
meal = 44.50
tax = 0.0675
tip = 0.15

# expressions carrying out calculations
meal = meal + meal * tax
total = meal + (meal * tip)

# print the result to the user
print("%.2f" % total)