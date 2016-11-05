
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program calculates implements a grade book for a set of students, allowing you
to become the teacher for the day. The concepts introduced include:
- Using dictionaries as variables that store related information (records)
- Passing a list of dictionaries as an argument to a function 
- The importance of encapsulating functionality in separate modules which can later be called

Example input:
print get_class_average(students)
print get_letter_grade(get_class_average(students))

Example output:
83.8666666667
B 

"""


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# create a list of dictionaries for passing to functions
students = [lloyd, alice, tyler]

# Add your function below!
def average(numbers):
    total = 0
    total = float(sum(numbers))
    return total/len(numbers)
    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (0.1*homework) + (0.3*quizzes) + (0.6*tests)
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"
        
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
        

print get_class_average(students)
print get_letter_grade(get_class_average(students))