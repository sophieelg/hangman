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
- In order to validate that the user has only entered a single letter, an if statement checks the lengh of the input is equal to 1 and an alphabet.

```python
if len(guess) ==1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
```
