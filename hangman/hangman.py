import random
import string
from words import words

def get_word(words):
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word

def hangman():
    # initialize variables
    word = get_word(words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()
    lives = 6

    # get user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print(f'You have {lives} lives.')
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word ]
        
        print('Word: ', ' '.join(word_list))

        user_letter = input('\n\nGuess a letter: ').upper()

        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print(f'\n\nThe letter {user_letter} is not in the word.')
                lives = lives - 1 
        elif user_letter in used_letters:
            print(f'\nYou already guessed that letter')
        else: 
            print (f'\nInvalid letter')


    if lives == 0: print(f'\n\nYou lost! The word was {word}')
    else: print('\n\nYes! the word was: ',' '.join(word))

hangman()