# Import the time module for a slight delay effect
import time

# Welcome the user
name = input("What is your name? ")
print(f"Hello, {name}! It's time to play Hangman!")

# Wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# Set the secret word (you can choose any word)
word = "secret"

# Initialize an empty string to store guessed letters
guesses = ""

# Set the maximum number of turns
turns = 10

# Create a while loop to keep the game running
while turns > 0:
    # Initialize a counter for incorrect guesses
    failed = 0

    # Check each character in the secret word
    for char in word:
        # If the character is already guessed, print it
        if char in guesses:
            print(char, end="")
        else:
            # If not found, print a dash
            print("_", end="")

            # Increase the failed counter
            failed += 1

    # If all characters are guessed correctly, the player wins
    if failed == 0:
        print("\nYou won!")
        break

    # Ask the user to guess a character
    guess = input("\nGuess a character: ")

    # Add the guess to the list of guesses
    guesses += guess

    # If the guess is not in the secret word
    if guess not in word:
        # Decrease the turns counter
        turns -= 1
        print("Wrong!")

        # Display how many turns are left
        print(f"You have {turns} more guesses.")

    # If the turns are exhausted, the player loses
    if turns == 0:
        print("You Lose! The secret word was:", word)
