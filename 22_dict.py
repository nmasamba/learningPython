
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program shows an example of using the dictionary (dict) data structure.
It is useful to think of dictionaries as key:value pairs, so in that sense a dict
record can be indexed by its key. They are immutable data types.
                                                                                                                                                                                                                                                                 

"""



my_dict = {
    "name": "Hinde Moni",
    "ID": 344,
    "Saying": "Hail Mary!"
    }
    
print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key, my_dict[key]