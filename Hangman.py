import random
from words import words
import string

def activ_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = activ_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('You already used these letters ', ' '.join(used_letters))
        # jakie jest szukane słowo
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letters = input('Guess a letter: ').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
        elif user_letters in used_letters:
            print('You already used this letter. Please try again.')
        else:
            print('Error invalid character. Please try again.')
    print(f'Yeah!! You guess corret word {word}!!')


hangman()
