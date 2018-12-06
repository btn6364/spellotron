"""
File_name: test_adjacent_key.py
Name: Bao Nguyen <btn6364@rit.edu>
Class: CSCI 141
Assignment: Project
Language: Python 3
"""

from global_variable import *

def test_adjacent_key(word):
    """
    Fix the adjacent-key spell errors of the word
    :param word: Any word
    :return: The word if it is legal, Number if it contains number on it and the fixed word it is illegal.
    """
    (left_punc, word_strip, right_punc) = strip_punctuation(word)
    if word_strip == "":
        return word
    if contain_decimal(word_strip):
        return 'Number'
    first_letter = word_strip[0]
    if first_letter in CAPITAL_ALPHABET:
        word_strip = word_strip.lower()
    if word_strip in LEGAL_WORD_FILE:
        return word
    else:
        for idx in range(len(word_strip)):
            character = word_strip[idx]
            if not character.isupper() and not character.islower():
                pass
            else:
                for item in KEY_ADJACENCY_FILE[character]:
                    fixed_word = word_strip[:idx] + item + word_strip[idx+1:]
                    if fixed_word in LEGAL_WORD_FILE:
                        if first_letter in CAPITAL_ALPHABET:
                            fixed_word = fixed_word.capitalize()
                        return left_punc + fixed_word + right_punc
        if fixed_word not in LEGAL_WORD_FILE:
            return None