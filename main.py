import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word

# print(get_valid_word(words))