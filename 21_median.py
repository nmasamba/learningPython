

"""

Author: Nyasha Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is an example of modularity, encapsulation and algorithmic thinking.
It is simply a function that takes in a list of integers. It will then find the median
of the list. The median is the middle number in a sorted sequence of numbers. Finding the 
median of [7,12,3,1,6] would first consist of sorting the sequence and then locating the 
middle value. If you are given a sequence with an even number of elements, you must 
average the two elements surrounding the middle. We sort the input sequence using 
the sorted() function

Example input and output:
median([7,3,1,4]) is 3.5   

"""


def median(numbers):
    numbers = sorted(numbers)
    print numbers
    if len(numbers) % 2 == 0:
        l = len(numbers)/2
        h = (len(numbers)/2) - 1
        med = (numbers[l] + numbers[h])/2.0
    else:
        h = int(round(len(numbers)/2))
        med = numbers[h]
    return med