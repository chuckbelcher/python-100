import random
# Step 1 Create Word List
word_list = ["aardvark", "baboon", "camel"]


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# Create list with to represent chosen word
word_display = []

for space in range(0, len(chosen_word)):
    word_display.append('-')
print(word_display)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('What letter do you guess? ').lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for index in range(0, len(chosen_word)):
    if guess == chosen_word[index]:
        word_display[index] = guess
    else:
        print('Wrong')

# TODO -4: - Loop through each position in the chosen_word;
# TODO - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
print(word_display)

# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
