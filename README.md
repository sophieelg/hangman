# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1

- Set up of the dev environment.

## Milestone 2

- The list of possible words that will be guessed during the game has been defined.
- The random module has been used to return a random word which will be guessed from the defined list.

```python
word = random.choice(word_list)
print(word)
```

- The input function is used to direct the user to enter a single letter.
- In order to validate that the user has only entered a single letter, an if statement checks the length of the input is equal to 1 and an alphabet.

```python
if len(guess) ==1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
```

## Milestone 3

- New script created called 'milestone_3.py'.
- A while loop with the condition set to 'True' ensures the code runs continuously until the user inputs a valid guess.

```python
while True:
    guess = input('Guess a single letter')
    if len(guess) ==1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please enter a single alphabetical character.')
```

- An if statement checks if the guess is in the word.

```python
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
```

- To tidy up the code, the previous tasks were defined as functions called 'check_guess' and 'ask_for_input'.
- Within the 'ask_for_input' function, the 'check_guess' function is called, so calling the 'ask_for_input' will run both functions.

```python
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input('Guess a single letter')
        if len(guess) ==1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()
```

## Milestone 4

- New script created called 'milestone_4.py'.
- A class has been defined which includes the attributes and methods needed for the Hangman game.
- Inside the Hangman class an init method initialises the atrributes of the class.

```python
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list) # the word to be guessed
        self.word_guessed = len(self.word) * ['_'] # a list of the letters not yet guessed
        self.num_letters = len(set(self.word)) # the number of unique letters in the word that have not been guessed yet
        self.num_lives = num_lives # the number of lives the player has at the start of the game
        self.word_list = word_list # a list of words
        self.list_of_guesses = [] # a list of the guesses that have already been tried.
```

- The 'check_guess' & 'ask_for_input' functions from Milestone 3 have been added and expanded upon to create the methods defined inside the class.
- The 'check_guess' method coverts the guess to lower case. If the guess is in the word a for-loop replaces the underscores in the 'word_guessed' with the letter guessed by the user.
- If the guess is not in the word the 'num_lives' variable is reduced by 1 & messages are printed to communicate this to the user.
- Outside the for loop, the variable 'num_letters' is reduced by 1.

```python
def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for position, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[position] = guess
            self.num_letters -= 1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print (f"You have {self.num_lives} lives left.")
```

- The 'ask_for_input' method has a while loop which validates whether the user has entered a single alphabetical character and whether the user has entered this guess before.
- If the guess passes the validation, the guess will be added to the 'list_of_guesses'.

```python
def ask_for_input(self):
        while True:
            guess = input("Guess a single letter.")                      
            if len(guess) !=1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")        
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else: 
                self.list_of_guesses.append(guess)
                break        
        self.check_guess(guess)
```

