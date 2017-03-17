
"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an introduction to inheritance. If you think of classes
as blueprints for things, and objects as the actual things; it may be the case that
we may wish to create a new blueprint with the attributes of an existing class.
We can use inheritance to create a new class with the qualities of the existing class.
The new class is called the child class, and the existing class is known as the parent
class. 

On the flip side, sometimes you'll be working with a derived class (or subclass) and 
realize that you've overwritten a method or attribute defined in that class' base class 
(also called a parent or superclass) that you actually need. Have no fear! You can 
directly access the attributes or methods of a superclass with Python's built-in 
super call.

The syntax looks like this:

class Derived(Base):
   def m(self):
       return super(Derived, self).m()
Where m() is a method from the base class.

"""

# Base class
class Employee(object):
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Derived class
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
        
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
        
# Instance of PartTimeEmployee class (object of type PartTimeEmployee)
milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)