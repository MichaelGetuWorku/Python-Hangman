# Step 1

import random
word_list = ['ardvark', 'baboon', 'camel']
print('---------------------------------')
print('Welcome to the Hand Man!')
# TODO:1 Randomly choose a word from the wordList and assign it to a variable calles chosen_word
chosen_word = random.choice(word_list)
# or
# chosen_word = random.randint(0, len(word_list) - 1)
# loopWord = word_list[chosen_word]

# TODO:4 so if the chosen_word was appel display should be "_" with 5 "_" reperesenting each letters to gusse
# print(chosen_word)
# the _ is if we are not using the variable
display = []

for _ in range(0, len(chosen_word)):
    display += '_'
# print(display)

# TODO:2 Ask the user to guess letter and assign thire answer to a variable called gusse. make guess lowercase.
guess = input('Guess the mistry letter: ').lower()

# TODO:3 check if the letter the user gussed is one of the letters in the chosen_word

# TODO:5 if the user guessed "p" and the choosen word was apple the display should be ["_","p","p","_","_"]
# ! Mine
# secret_word = []
# final_word = []
# for letter in chosen_word:
#     if guess == letter:
#       display = guess
#     else:
#       display = '_'
#     secret_word = display
#     final_word.extend(secret_word)
# print(final_word)

# ! Angela
for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter
print(display)