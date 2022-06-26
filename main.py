import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 6
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #lettes used
        print('Your have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #what currant word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Your letter is not in the word!")
        elif user_letter in used_letters:
            print("You have already used the letter") 
        else:
            print("Invalid character")
        
    if lives == 0:
        print("You died sorry, the word is ",word)
    else:
        print("Yay! you guessed the word",word,'!!')

hangman()
# print(get_valid_word(words))