import random
import re
import sys
import os


# Load the words from the file
def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(" ")
    secret_word = random.choice(words_list)
    return secret_word


# Check if a word has been fully guessed
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


# Get the guessed word so far
def get_guessed_word(secret_word, letters_guessed):
    secret_word_letters = [letter for letter in secret_word]

    word_so_far = ""
    for letter in secret_word_letters:
        if letter in letters_guessed:
            word_so_far += letter
        else:
            word_so_far += "_"
    return word_so_far


# Check if a guess is in the word
def is_guess_in_word(guess, secret_word):
    return guess in secret_word


# Main
def main():
    try:
        secret_word = load_word()
        letters_guessed = []

        max_incorrect = len(secret_word)
        incorrect_guesses = 0

        blank_word = re.sub(r".", "_", secret_word)
        print(f"The word is: {blank_word}")

        # Game loop
        while True:
            guess = input("Guess a letter!\n")
            os.system("clear")

            # Check for invalid guesses
            if len(guess) == 0 or guess.isnumeric():
                print("Invalid guess!")
                continue

            # Check if the user guessed multiple letters
            if len(guess) > 1:
                print("Please only guess one letter at a time!")
                continue

            # Check if the user already guessed that letter
            if guess in letters_guessed:
                print(f"You have already guessed \"{guess}\"!")
                continue

            letters_guessed.append(guess)

            # Check if guess is in the word
            if is_guess_in_word(guess, secret_word):
                print(f"Your guess of \"{guess}\" is in the word!")
            else:
                incorrect_guesses += 1
                print(f"Your guess of \"{guess}\" was not in the word!\n"
                      f"You have {max_incorrect - incorrect_guesses} guesses left")

            # Check if the word is guessed
            if is_word_guessed(secret_word, letters_guessed):
                print(f"You won! The word was \"{secret_word}\"")
                break
            elif incorrect_guesses >= max_incorrect:
                print(f"Oh no! You ran out of guesses. The word was \"{secret_word}\"")
                break
            else:
                word_so_far = get_guessed_word(secret_word, letters_guessed)
                print(f"The word so far is: {word_so_far or blank_word}\n")

        # Ask the player if they want to play again.
        wants_new_game = input("\nWant to play again? ")
        if wants_new_game.lower() == "yes":
            os.system("clear")
            main()

    except FileNotFoundError:
        print("Could not find the words.txt file!")
    except IndexError:
        print("No words found in words.txt!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
