# %%
import random

# define possible words

word_list = ['Banana', 'Apple', 'Orange', 'Strawberry', 'Grape']
print(word_list)
# %%

# select random word from list

word = random.choice(word_list)
print(word)
# %%

# while loop until user enters a single character

while True:
    guess = input('Guess a single letter.')
    if len(guess) == 1:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
# %%
