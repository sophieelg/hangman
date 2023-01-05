# %%
import random

# define possible words

word_list = ['Banana', 'Apple', 'Orange', 'Strawberry', 'Grape',]
print(word_list)
# %%

# print random word from list

word = random.choice(word_list)
print(word)
# %%

# ask the user for an input

guess = input('Enter a single letter')

# check the input is a single character

if len(guess) ==1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')