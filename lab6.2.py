"""Assignment 6.2: Counting the vowels in a string recursively"""
__author__ = 'Jenny Hamer'

def count_vowels(my_str):
    vowels = ["a", "e", "i", "o", "u"]
    my_str = my_str.lower()
    my_vowels = ""
    vowel_count = 0
    if not my_str:
        return 0
    if my_str[0] in vowels:
        my_vowels += my_str[0]
        vowel_count = 1
        print(my_vowels)
    elif not(my_str[0] in vowels):
        vowel_count = 0
    return vowel_count + count_vowels(my_str[1:])




    
"""
example output:    
print("There are ", count_vowels('banana'),"vowels in 'banana'.")
print("apples --> ", count_vowels('apples'))
print("peanut butter --> ", count_vowels('peanut butter'))

a
a
a
There are  3 vowels in 'banana'.
a
e
apples -->  2
e
a
u
u
e
peanut butter -->  5
"""
