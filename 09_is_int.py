
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes a number x as input. It will then evaluate the input
and print True if the number is an integer, otherwise it will print False. An integer is 
just a number without a decimal part (for instance, -17, 0, and 42 are all integers, 
but 98.6 is not). For the purpose of this lesson, we'll also say that a number with a 
decimal part that is all 0s is also an integer, such as 7.0. This means that, for this lesson, 
you can't just test the input to see if it's of type int. If the difference between a number 
and that same number rounded down is greater than zero, what does that say about that 
particular number?

Example input - output:
is_int(6) - True
is_int(56.0) - True
is_int(6.54764) - False                                                                                                                                                                                                                                                                                                  


"""

def is_int(x):
    if int(x) - round(x, 2) == 0:
        print True
    else:
        print False
        
