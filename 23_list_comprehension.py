

"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of Python's expressiveness. Less is more when it
comes to true Pythonic code, and list comprehensions prove that. A list comprehension
is an easy way of automatically creating a list in one line of code. In this example,
we use a list comprehension to create a list, cubes_by_four. The comprehension 
should consist of the cubes of the numbers 1 through 10 only if the cube is evenly 
divisible by four. Finally, we print that list to the console. Note that in this 
case, the cubed number should be evenly divisible by 4, not the original number.

Example output:
[8, 64, 216, 512, 1000]    

"""


cubes_by_four = [n**3 for n in range(1,11) if (n**3)%4 == 0]

print cubes_by_four