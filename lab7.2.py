"""CS 3A: Object-oriented Python
Lab Assignment 7.2: student_scores - tuples """
__author__ = 'Jenny Hamer'
def student_scores():
    possible_scores = (1, 2, 3, 4, 5)
    print("The lowest possible score is ", possible_scores[0], "and the highest possible score is ", possible_scores[4])
    i = 0
    while i in range(len(possible_scores)):
        print("A student can get ", possible_scores[i], " points.")
        i += 1

def main():
    student_scores()

main()