import random
"""lab 9: hangman game implementation --> text version"""
__author__ = 'Jenny Hamer'


def hangman():
    turns = 0 #counter for wrong turns (letters) the player takes
    word_bank = dict()
    correct_letters = ""
    wrong_letters = ""    

    # opens the file of words for reading and assigns it to variable word_list
    with open('word_list.txt', 'r') as word_list:
        for line in word_list:
            entry_index = 1
            for word in line.split(): #assigns each word in the file to a key and adding it to the word_bank dictionary
                word = word.lower()
                word_bank[entry_index] = word
                entry_index += 1

    rand_answer = random.randint(1, len(word_bank)) # gets a random entry in the word bank and assigns it as the answer to guess
    #construct a string of dashes to represent the word to guess
    answer = word_bank[rand_answer]
    answer_rep = '-' * len(answer)
    print("Here is your word to guess\n", answer_rep)

    while turns < 6:
        player_guess = input("Enter a letter to guess:\n>>>")
        if not player_guess.isalpha():
            print("HmmBrrr... Does not compute. Please enter a letter:\n>>>")
        if player_guess.isalpha(): #if player's entry is alphanumeric
            player_guess.lower() #converts input to lower case --> game is case-sensitive
#            for i in range(len(answer)):
            if player_guess in answer and player_guess not in correct_letters:
                #find the index of the letter within the 'answer'
                for i in range(len(answer)):
                    if answer[i] in player_guess:
                        answer_rep = answer_rep[:i] + player_guess + answer_rep[i+1:]
                correct_letters += player_guess
                if answer_rep == answer:
                    print("Fantastic! You guessed correctly. The word is " + answer + ". Enter hangman() to play again.")
                    return
                print("Well done! The word is now...\n" + answer_rep)
                
            elif len(player_guess) != 1:
                print("Please enter a single letter at a time:\n>>>")
            elif player_guess not in answer:
                if player_guess not in wrong_letters:
                    wrong_letters += player_guess
                    turns += 1
                    if len(wrong_letters) < 6:
                        print("That letter isn't in the word... You have made", turns, "guesses. You've guessed: " + wrong_letters + " so far.\n>>>")
                    else:
                        print("Game over! You've tried your best, but to no avail. The word was...\n" + answer)
                        return
                else:
                    print("You already guessed that letter; try again...\n>>>")
            elif player_guess in wrong_letters or player_guess in correct_letters:
                print("Silly, you've already guessed that letter! Guess another...\n>>>")

def main(): #a call to main() or hangman() starts the game
    hangman()
