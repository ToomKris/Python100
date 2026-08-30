import random 

hangman = ['''
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
 / I  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|I  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|I  |
 / I  |
      |
=========''']

lives = 6
placeholder = ""
game_over = False
letters = []
guessed = []

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

chose_word = random.choice(word_list)

for things in chose_word:
    letters.append(things)

for empty in range(len(letters)): 
    placeholder += "_"

print(placeholder)

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in letters:
        if letter == guess:
            display += letter
            guessed.append(letter)
        elif letter in guessed:
            display += letter
        else:
            display += "_"

    if guess not in letters:
        lives -= 1

    print(display)
    print (hangman[6 - lives])

    if "_" not in display:
        print("You win!")
        game_over = True

    elif lives == 0:
        game_over = True
        print("You lose! The word was: " + chose_word)
