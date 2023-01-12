import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(self.word_list) # the word to be guessed
        self.word_guessed = len(self.word) * ['_'] # a list of the letters not yet guessed
        self.num_letters = len(set(self.word)) # the number of unique letters in the word that have not been guessed yet
        self.num_lives = num_lives # the number of lives the player has at the start of the game
        self.word_list = ['Banana', 'Apple', 'Orange', 'Strawberry', 'Grape'] # a list of words
        self.list_of_guesses = [] # a list of the guesses that have already been tried.

