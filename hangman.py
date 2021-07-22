# Step 1

import random
word_list = ['ardvark', 'baboon', 'camel']

# TODO:1 Randomly choose a word from the wordList and assign it to a variable calles chosen_word
chosen_word = random.randint(0, len(word_list) - 1)
loopWord = word_list[chosen_word]

# TODO:2 Ask the user to guess letter and assign thire answer to a variable called gusse. make guess lowercase.
guess = input('Guess the mistry letter: ').lower()

# TODO:3 check if the letter the user gussed is one of the letters in the chosen_word

for look_letter in loopWord:
    if guess == look_letter:
        print('Right')
    else:
      print('Wrong')
