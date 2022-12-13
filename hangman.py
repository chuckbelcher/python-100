import random
# Step 1 Create Word List
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Create list with to represent chosen word
word_display = []

for space in range(0, len(chosen_word)):
    word_display.append('_')
print(word_display)

#  Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('What letter do you guess? ').lower()

#  Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for index in range(0, len(chosen_word)):
    if guess == chosen_word[index]:
        word_display[index] = guess

print(word_display)

while word_display.count('_') > 0:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input('What letter do you guess? ').lower()

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for index in range(0, len(chosen_word)):
        if guess == chosen_word[index]:
            word_display[index] = guess

    print(word_display)

print('Congratulations, You Win !!!!')

