"""Lab Assignment 3: user input (numerical grade values)
   and conditionals to determine letter grades earned"""
__author__ = 'Jenny Hamer'

def grading():
    no_of_grades = 5
    while no_of_grades > 0:
        grade_value = input('Please enter the numeric grade received in the course.\n>>> ')
        grade_value = int(grade_value)
        if grade_value >= 90:
            print('letter grade is A')
        elif grade_value < 90 and grade_value >= 80:
            print('letter grade is B')
        elif grade_value < 80 and grade_value >= 70:
            print('letter grade is C')
        elif grade_value < 70 and grade_value >= 60:
            print('letter grade is D')
        else:
            print('letter grade is F')
        no_of_grades -= 1

grading()
