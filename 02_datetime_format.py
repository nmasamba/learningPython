"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program shows how to format strings in Python, using the %s operator
as a placeholder and then specifying which result to print in its place. The program
also introduces importing modules from libraries in order to extend the functionality
of Python programs. Note that the imported module is actually stored and used as a 
variable in the program below.

Typical output (depending on current system time): 
10/31/2016 18:28:32

"""

from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)