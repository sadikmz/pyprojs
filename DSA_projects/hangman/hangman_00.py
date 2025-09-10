import random

def making_a_guess():
    x = 0
    global update_display
    correct_guesses = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guesses = True
        x += 1


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]

chosen_word = list(random.choice(word_list))

blank = "_" * len(chosen_word)
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

update_display = 0

#----------------------------------------------------------------------------------------------

print (HANGMANPICS[update_display])
guess = input(f"Welcome to hangnab.\n{blank}\nMake a guess? ")
making_a_guess()
print(HANGMANPICS[update_display])
print("".join(blank_list))
while update_display < 6:
    if blank_list == chosen_word:
        print("You won!")
        break
    guess = input("Make another guess? ")
    making_a_guess()
    print(HANGMANPICS[update_display])
    print("".join(blank_list))
if update_display == 6:
    print("Game Over!. Thank you for playing!")
