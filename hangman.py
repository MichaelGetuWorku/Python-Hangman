# Step 1

import random
word_list = ['ardvark', 'baboon', 'camel']

# TODO:1 Randomly choose a word from the wordList and assign it to a variable calles chosen_word
chosen_word = random.choice(word_list)
# or
# chosen_word = random.randint(0, len(word_list) - 1)
# loopWord = word_list[chosen_word]

# TODO:4 so if the chosen_word was appel display should be "_" with 5 "_" reperesenting each letters to gusse
print(chosen_word)
hash_word = []
for replace in range(0, len(chosen_word)):
    hash_word += '_'
print(hash_word)

# TODO:2 Ask the user to guess letter and assign thire answer to a variable called gusse. make guess lowercase.
guess = input('Guess the mistry letter: ').lower()

# TODO:3 check if the letter the user gussed is one of the letters in the chosen_word

# TODO:5 if the user guessed "p" and the choosen word was apple the display should be ["_","p","p","_","_"]
secret_word = []
final_word = []
print('-----')
for letter in chosen_word:
    if guess == letter:
      hash_word = guess
    else:
      hash_word = '_'
    secret_word = hash_word
    final_word.extend(secret_word)
print(final_word)
