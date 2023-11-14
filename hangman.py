import random
import os

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Step 1 Create Word List
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(chosen_word)

# Create list with to represent chosen word
word_display = []
guessed_letters = []
for space in range(0, word_length):
    word_display.append('_')
print(word_display)

while word_display.count('_') > 0 and lives > 0:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input('What letter do you guess? ').lower()
    if guess in guessed_letters:
        print(f'You alread guessed {guess}')
        continue
    guessed_letters.append(guess)
    if guess not in chosen_word:
        lives -= 1
    else:
        # Add guessed letter to word_display in correct spot
        for index in range(0, word_length):
            if guess == chosen_word[index]:
                word_display[index] = guess
    os.system('clear')
    print(stages[lives])
    print(word_display)
    print(f"\nYou have guessed the following letters: \n {guessed_letters}\n")
    print(f"you have {lives} lives left\n")

if lives == 0:
    print("You Loose")
else:
    print('Congratulations, You Win !!!!')
