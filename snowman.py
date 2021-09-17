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
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    secret_word_letters = [letter for letter in secret_word]

    word_so_far = ""
    for letter in secret_word_letters:
        if letter in letters_guessed:
            word_so_far += letter
        else:
            word_so_far += "_"
    return word_so_far


def is_guess_in_word(guess, secret_word):
    return guess in secret_word


def spaceman(secret_word):
    letters_guessed = []

    blank_word = re.sub(r".", "_", secret_word)
    print(f"The word is: {blank_word}")

    while True:
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
