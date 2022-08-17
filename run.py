import random
from words import words

def get_word():
    word = random.choice(word_list)
    return word.upper()

    def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
     print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")