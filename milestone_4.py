# %%
import random

# %%
word_list = ['Banana', 'Apple', 'Orange', 'Strawberry', 'Grape']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list) # the word to be guessed
        self.word_guessed = len(self.word) * ['_'] # a list of the letters not yet guessed
        self.num_letters = len(set(self.word)) # the number of unique letters in the word that have not been guessed yet
        self.num_lives = num_lives # the number of lives the player has at the start of the game
        self.word_list = word_list # a list of words
        self.list_of_guesses = [] # a list of the guesses that have already been tried.       
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
    
    def ask_for_input(self):
        while True:
            guess = input('Guess a single letter.')
            if len(guess) !=1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                break
        self.check_guess(guess)
                

game = Hangman(word_list)
game.ask_for_input()
# %%
