#Lab Assignment 5.2: filter out a given word/str's vowels and return both them and the total count
__author__ = 'Jenny Hamer'

def count_vowels(myStr):
    index = 0
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    myStr = myStr.lower()
    myVowels = [] #empty array to collect the inputted word's vowels
    for c in myStr:
        if c in vowels:
            myVowels.append(c)
            count += 1            
        index += 1
    print("Your word had these vowels!", myVowels)    
    print("That adds up to", count, "vowels!")

"""
Example output:
count_vowels("Generic Example")
Your word had these vowels!  ['e', 'e', 'i', 'e', 'a', 'e']
That adds up to 6 vowels!    
count_vowels("Banana")
['a', 'a', 'a']
That word/sentence has 3 vowels!
"""
