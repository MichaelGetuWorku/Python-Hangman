import random
import hangman_art
import hangman_words


print(hangman_art.logo)
print('Welcome to the Hang Man!')
# Randomly choose a word from the wordList and assign it to a variable calles chosen_word
chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)
# or
# chosen_word = random.randint(0, len(hangman_words.word_list) - 1)
# loopWord = word_list[chosen_word]

lives = 6
display = []

for _ in range(0, len(chosen_word)):
    display += '_'

end_of_game = False
while not end_of_game:
    guess = input('Guess the letter: ').lower()
    if guess in display:
        print(f'You alredy guessed that {guess}!')
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    # Join all the elements in the list and turn it into a String.
    if guess not in chosen_word:
        print(
            f'You guessed {guess}, that is not in the choosen word!, you lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You Lost')
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print('You Won')
    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])

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
    # for position in range(len(chosen_word)):
    #     letter = chosen_word[position]
    #     if letter == guess:
    #         display[position] = letter
    # print(display)
