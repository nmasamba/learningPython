"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program calculates the cost of a shopping bill. It takes into account
the required quantity and multiplies it by the price. The main functionality
is encapsulated in a function as introduced in previous lessons.
 The concepts introduced include:
- Lists in Python, which are data structures that store objects of the same data type
- Python dictionaries, which are data structures that store info as key/value pairs
- Using FOR loops (iteration) with lists and dictionaries
- Updating data in response to changes in the environment (for instance, decreasing the number of bananas in stock by 1 when you sell one).

What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?

Example input:
trip_cost("Los Angeles", 5, 600)

Example output:
1955 

"""


# this is how to create a list
shopping_list = ["banana", "orange", "apple"]

# this is a dictionary, made up of key:value pairs
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your main code below!
def compute_bill(food):
    total = 0
    
    for i in food:
        if stock[i] > 0:
            total += prices[i]
            stock[i] -= 1
    return total
    
    