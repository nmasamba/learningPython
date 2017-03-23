
"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of good I/O practice when reading and writing files.
Programming is all about getting the computer to do the work. Is there a way to get 
Python to automatically close our files for us? Of course there is. This is Python.

File objects contain a special pair of built-in methods: __enter__() and __exit__(). 
The details aren't important, but what is important is that when a file object's __exit__() 
method is invoked, it automatically closes the file. How do we invoke this method? 
With with and as.

The syntax looks like this:

with open("file", "mode") as variable:
    # Read or write to the file

Check out the example below. Note that we don't explicitly close() our file, and 
remember that if we don't close a file, our data will get stuck in the buffer. 
Here the file closing is done implicitly.

"""

with open("text.txt", "w") as my_file:
    my_file.write("Python Done. Case Closed.")