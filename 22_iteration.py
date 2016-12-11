
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program shows a way to iterate over tuples, dictionaries and strings.
Python includes a special keyword: in. You can use in very intuitively, like below.
In the example, first we create and iterate through a range, printing out 0 1 2 3 4.
Next, we create a dictionary and iterate through, printing out age 26 name Eric.
Dictionaries have no specific order. Finally, we iterate through the letters of a 
string, printing out E r i c.

Example output:
0 1 2 3 4 age 26 name Eric E r i c                                                                                                                                                                                                                                                                  

"""

for number in range(5):
    print number,

d = { "name": "Eric", "age": 26 }
for key in d:
    print key, d[key],

for letter in "Eric":
    print letter,  # note the comma!
 #Note that the trailing comma ensures that we keep printing on the same line.
 


