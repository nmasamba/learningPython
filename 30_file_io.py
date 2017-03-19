
"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of working with external input and output sources.
   
Until now, the Python code you've been writing comes from one source and only goes 
to one place: you type it in at the keyboard and its results are displayed in the console. 
But what if you want to read information from a file on your computer, and/or write that 
information to another file? This process is called file I/O 
(the "I/O" stands for "input/output"), and Python has a number of built-in functions 
that handle this for you.

Check out the below. Note that you need an empty output.txt in the same root as your Python
code. Although that file is empty, that's all about to change!
   
"""

# Generates a list of squares of the numbers 1 - 10
my_list = [i**2 for i in range(1,11)]

# Open output.txt file for writing
my_file = open("output.txt", "w")

# Write to text file
for item in my_list:
    my_file.write(str(item) + "\n")

# IMPORTANT: make sure to close the file and I/O stream after operating on it
my_file.close()

