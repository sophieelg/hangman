# %%

while True:
    guess = input('Guess a single letter')
    if len(guess) ==1 and guess.isalpha():
        break
    else:
        print('Invalid letter. Please enter a single alphabetical character.')
# %%
