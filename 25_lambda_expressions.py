
"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is introduces lambda expressions in Python. A lambda expression 
is simply an anonymous function. In Python, anonymous function is a function that is 
defined without a name. While normal functions are defined using the def keyword, 
in Python anonymous functions are defined using the lambda keyword. Hence, anonymous 
functions are also called lambda functions. They are typically used in situations
where encapsulated behaviour is required but without the need to write a named function
as the anonymous function won't be called or re-used again.
Create a list, squares, that consists of the squares of the numbers 1 to 10. A list 
comprehension could be useful here! Use filter() and a lambda expression to print out 
only the squares that are between 30 and 70 (inclusive).
  
"""

squares = [x**2 for x in range(1,11)]
print filter(lambda x: x >= 30 and x <= 70, squares)