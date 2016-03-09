"""Lab Assignment 7.1: Create word dictionary to keep track of words and their definitions
three options on running"""
"""
    Option 1: user can see all words and meanings that have been entered so far. If user has not entered any words, print message "There's no word in the dictionary yet"
    Option 2: protmp user to enter a new word, then prompt user to enter the meaning.
        Your program must not allow duplicate entries.
        Your program should store all entered words and meanings into a dictionary data structure
    Option 3: allows user to search for a word. If the word exists in the dictionary, then display the meaning; otherwise print message "Word not found".
    Program should use loop or recursive function to keep prompt for user input, until user choose to exit. Program should provide option for user to exit, for example, enter 0, or enter "q"
"""
__author__ = 'Jenny Hamer'

def word_dictionary():
    while (True):
        user_prompt = int(input("""Select one of the following options by entering its corresponding number:
        Option 1: view all words and their definitions in the dictionary.
        Option 2: enter a new word and definition.
        Option 3: look-up a word
        Enter 0 to quit\n>>>"""))

        word_meanings = dict()
        word_meanings['Dobry den'] = 'Good day'
        word_meanings['chleb'] = 'bread'
        word_meanings['maslo'] = 'butter'


        if (user_prompt == 1):
            for word in word_meanings:
                print('The word', word, 'means', word_meanings[word], '\n')

        if (user_prompt == 2):
            word_entry = input('Enter the word you wish to define:\n>>>')
            definition_entry = input('Enter the word\'s new definition:\n>>>')
            #add the word_entry and definition_entry to the dictionary as a key/value pair
            if word_entry in word_meanings:
                print('That word is already defined in the dictionary! It means', word_meanings[word_entry], '.\n')
            elif word_entry not in word_meanings:
                word_meanings[word_entry] = [definition_entry]
                print('The word -', word_entry, '- means', word_meanings[word_entry], '.\n')

        if (user_prompt == 3):
            word_search = input('Enter the word you wish to search in the dictionary:\n>>>')
            #look-up word by key
            if word_search in word_meanings:
                print('That word -', word_search, '- means', word_meanings[word_search], '\n')
            else:
                print('The word -', word_search, '- does not yet exist in this dictionary. To add it, select Option 2.\n')

        if (user_prompt == 0):
            break

def main():
    word_dictionary()

main()