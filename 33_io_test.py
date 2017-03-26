
"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of good I/O practice when reading and writing files.
We'll want a way to test whether a file we've opened is closed. Sometimes we'll have 
a lot of file objects open, and if we're not careful, they won't all be closed. How 
can we test this?

f = open("bg.txt")
f.closed outputs False

f.close()
f.closed outputs True

Python file objects have a .closed attribute which is True when the file is closed and 
False otherwise. By checking file_object.closed, we'll know whether our file is closed 
and can call close() on it if it's still open.

Below,check if the file is not .closed.
If that's the case, call .close() on it.
(You don't need an else here, since your if statement should do nothing if .closed is True.)
After your if statement, print out the value of my_file.closed to make sure your file is really closed.

"""

with open("text.txt", "w") as my_file:
    my_file.write("Python Done. Case Closed.")
    
if my_file.closed == False:
    my_file.close()
    
print my_file.closed