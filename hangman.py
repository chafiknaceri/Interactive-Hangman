# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):

    stringI = ""
    for char in secretWord:
        if char in lettersGuessed:
            stringI+=char+" "
        else:
            stringI+=" _ "

    return stringI




def getAvailableLetters(lettersGuessed):

    allletters = string.ascii_lowercase
    stringer = ""
    for letters in allletters:
        if letters not in lettersGuessed:
            stringer+= letters
    return stringer




def hangman(secretWord):



    secretWordlength = len(secretWord)
    # allowing user to make 8 guesses when they guess wrong
    numOfGuesses = 8
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    print("Welcome To the HangMan Interactive Game")
    print("The Word I am thinking of has {} letters.".format(secretWordlength))
    print("---------------")

    while True:
        print("You Have",numOfGuesses,"Left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters:",availableLetters)
        guesser = input("Please Guess a Letter: ")
        guess = guesser.lower()

        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print("Good Guess : ",getGuessedWord(secretWord, lettersGuessed))

        elif guess not in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            numOfGuesses -=1
            print("Sorry that letter is not in my word")
        elif guess  in lettersGuessed:

            print("Sorry but you have already Guessed that letter try Again")



        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratz You Won the word is ",secretWord)
            return
        if numOfGuesses <=1 :
            print("Sorry, you ran out of guesses. The word was",secretWord)
            return
        print("  ")



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
