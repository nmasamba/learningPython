"""
Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program calculates the cost of a holiday trip taking the destination
city, number of days and spending money as input. The concepts introduced include:
- Function definition using the def keyword
- Creating functions with parameters to receive passed arguments
- IF/ELSE logic to control the flow of a Python program
- Passing functions as arguments to other functions (functional programming)
- Reusing code, enabled by functions as modules (modularity)

What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?

Example input:
trip_cost("Los Angeles", 5, 600)

Example output:
1955 

"""



def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    if days >= 7:
        return (40*days) - 50
    elif days >= 3 and days < 7:
        return (40*days) - 20
    else:
        return 40 * days
        
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
print trip_cost("Los Angeles", 5, 600)