
"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an introduction to classes and the world of 
object oriented programming. Classes and objects are often used to model real-world 
objects. The code below is a simple yet realistic demonstration of the kind of 
classes and objects you might find in commercial software. Here we have a basic 
ShoppingCart class for creating shopping cart objects for website customers; 
though basic, it's similar to what you'd see in a real program. Note that a 
class is a blueprint for an object. The object is an instance of the class,
so think of it as 'the actual thing' created from the blueprint.

"""


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of a fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Nash William")
my_cart.add_item("Matemba", 3.50)