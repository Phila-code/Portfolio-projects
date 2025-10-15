import random

word_list = ["apple", "banana", "grape", "orange", "lemon"]

#  Initialize game variables
word_to_guess = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

display_word = ["_" for _ in word_to_guess]

# Welcome message
print("Welcome to Hangman Game")
print("Guess the word, one letter at a time")
print("You have 6 incorrect guesses allowed")

# Main game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word", " ". join (display_word))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
       print("Please enter a single letter\n")
       continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You've already guessed that letter")
        continue

    # Add guess to guessed_letter
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word_to_guess:
        print("Good guess!\n")
        for i in range(len(word_to_guess)):
           if word_to_guess[i] == guess:
               display_word[i] == guess
    else:         # Handle incorrect guesses
        print("Wrong guess\n")
        incorrect_guesses += 1


