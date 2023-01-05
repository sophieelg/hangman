# %%
import random

# define possible words

word_list = ['Banana', 'Apple', 'Orange', 'Strawberry', 'Grape']

# select random word from list

word = random.choice(word_list)

# while loop until user enters a single character

# %%

while True:
    guess = input('Guess a single letter')

    if len(guess) ==1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please enter a single alphabetical character.')

# checks whether the guess is in the word

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
# %%
