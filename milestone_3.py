# %%

# while loop checks if input is valid guess

while True:
    guess = input('Guess a single letter')
    if len(guess) ==1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please enter a single alphabetical character.')

# checks whether the guess is in the word

# %%
word_list = ['Banana', 'Apple', 'Orange', 'Strawberry', 'Grape',]
print(word_list)

# %%
