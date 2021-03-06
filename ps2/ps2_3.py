# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:32:02 2017

@author: Marianna
"""

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise\
    '''
    g_let = [] # the empty list in which we will put letters_guessed which are in secret_word
    secret_list = list(secret_word) # make list from string
    for char in secret_list:
        if char in letters_guessed:
            g_let.append(char) # make list with guessed letters
    if len(secret_list) == len(g_let):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
    represents which letters in secret_word have been guessed so far.
    '''
    part_secret_word = ''.join([char if char in letters_guessed else ' _ ' for char in secret_word]) # secret_word with '_'
    return part_secret_word
                              


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which
    letters have not
    yet been guessed.
    '''
    all_letters = list(string.ascii_lowercase[:])
    '''
    The lowercase letters'abcdefghijklmnopqrstuvwxyz'
    '''
    available_letters = all_letters[:] # Make copy of all_letters
    for char in letters_guessed:
        available_letters.remove(char)
    return ''.join(available_letters)


def warnings_remaining (warnings, number_of_guesses):
    '''
    The number of warnings the user has left.
    '''     
    if warnings > 0:
        warnings -= 1
        print("You have", str(warnings), "warnings left:", get_guessed_word(secret_word, letters_guessed))
        print("\n--------------------------------\n")
        return warnings, number_of_guesses
    elif warnings == 0:
        warnings = 0
        number_of_guesses -= 1
        print("You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))          
        print("\n--------------------------------\n")
        return warnings, number_of_guesses
    


def guesses_remaining (number_of_guesses, vowels, input_letter):
    '''
    The number of guesses the user has left
    '''
    if input_letter in vowels:
       number_of_guesses -= 2
    else:   
        number_of_guesses -= 1
    return number_of_guesses
        
                

def score (secret_word, number_of_guesses):
    '''
    Compute Total score
    '''
    unique_letters = []
    for char in secret_word:
        if char not in unique_letters:
            unique_letters.append(char)
    number_unique_letters = len(unique_letters)
    total_score = number_of_guesses * number_unique_letters
    return total_score
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
     
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    
    number_of_guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    print(secret_word)
    print("Welcome to the game Hangman!")
    print("You have", str(warnings), "warnings left.")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("\n--------------------------------\n")

    while number_of_guesses > 0:
        print("You have", str(number_of_guesses), "guesses left.")
        print("Available letters:: ", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ")
        input_letter = str.lower(guess)
        if len(input_letter) == 1:
            if str.isalpha(input_letter) is True:
                if input_letter not in letters_guessed:
                    letters_guessed.append(input_letter)
                    if input_letter in secret_word:
                        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                        print("\n--------------------------------\n")
                    else:
                        number_of_guesses = guesses_remaining(number_of_guesses, vowels, input_letter)
                        print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                        print("\n--------------------------------\n")
                else:
                    print("You've already tried this letter, choose another")
                    (warnings, number_of_guesses) = warnings_remaining(warnings, number_of_guesses)
            elif str.isalpha(input_letter) is False:
                print("Oops! That is not a valid letter.")
                (warnings, number_of_guesses) = warnings_remaining(warnings, number_of_guesses)
        elif len(input_letter) > 1:
            print("Please, only one character at a time")
            (warnings, number_of_guesses) = warnings_remaining(warnings, number_of_guesses)
          
        if is_word_guessed(secret_word, letters_guessed) is True:
            break
    
    if is_word_guessed(secret_word, letters_guessed) is True:
        print("Congratulations, you won!")
        print("Your total score for this game is:", score(secret_word, number_of_guesses))
    else:
        print("Sorry, you ran out of guesses. Game over!")
        print("The word was", secret_word)
        
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


if __name__ == "__main__": 
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    letters_guessed = []
    hangman(secret_word)