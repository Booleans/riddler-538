import numpy as np

with open('data/word-list.txt') as f:
    WORDS = tuple(word.strip().upper() for word in f if len(word.strip()) == 5)

words = np.array([tuple(word) for word in WORDS])
words_five_characters = tuple(word for word in WORDS if len(set(word)) == 5)

target = np.array(tuple('ABOUT'))
guess  = np.array(tuple('ADIEU'))

position_match = (guess == target)
potential_words = words[np.all(words[:, position_match] == guess[position_match], axis=1)]
letters_in_word = np.isin(guess, target)
letters_in_incorrect_position = guess[np.logical_xor(letters_in_word, position_match)]

np.logical_xor(letters_in_word, position_match)
