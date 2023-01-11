import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # a list of words
        self.num_lives = num_lives # the number of lives the player has at the start of the game

        self.word = random.choice(word_list) # the word to be guessed
        self.word_guessed = None # a list of the letters not yet guessed
        self.num_letters = None # the number of unique letters in the word that have not been guessed yet
        self.list_of_guesses = [] # a list of the guesses that have already been tried.

        word_list = ['Banana', 'Apple', 'Orange', 'Strawberry', 'Grape']

