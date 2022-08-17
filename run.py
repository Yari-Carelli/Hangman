import random
from words import words

def get_word():
    word = random.choice(word_list)
    return word.upper()