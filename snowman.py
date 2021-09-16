import random
import re
import sys
import os

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(" ")
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    # TODO: check if the letter guess is in the secret word

    pass


def spaceman(secret_word):
    letters_guessed = []
    word_guessed = False

    blank_word = re.sub(r".", "_", secret_word)
    print(f"The word is: {blank_word}")

    while not word_guessed:
        guess = input("Guess a letter!\n")
        os.system("clear")

        if len(guess) > 1:
            print("Please only guess one letter at a time!")
            continue
        letters_guessed.append(guess)

        guess_in_word = is_guess_in_word(guess, secret_word)
        if guess_in_word:
            print(f"Your guess of \"{guess}\" is in the word!")
        else:
            print(f"Your guess of \"{guess}\" was not in the word!")

        if is_word_guessed(secret_word, letters_guessed):
            print(f"You won! The word was \"{secret_word}\"")
            break
        else:
            word_so_far = get_guessed_word(secret_word, letters_guessed)
            print(f"The word so far is: {word_so_far or blank_word}\n")


if __name__ == "__main__":
    try:
        secret_word = load_word()
        spaceman(secret_word)
    except KeyboardInterrupt:
        sys.exit()
