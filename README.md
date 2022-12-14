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