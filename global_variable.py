"""
File_name: global_variable.py
Name: Bao Nguyen <btn6364@rit.edu>
Class: CSCI 141
Assignment: Project
Language: Python 3
"""


import re
CAPITAL_ALPHABET = list(chr(code) for code in range(ord('A'),ord('Z')+1))
LOW_ALPHABET =  list(chr(code) for code in range(ord('a'),ord('z')+1))
def store_adjacent_keys():
    """
    Store all the adjacent keys of all 26 keys of the QWERTY keyboard.
    :return: A dictionary of pairs of a key and a list of all its adjacent keys
    """
    adjacent_dict = {}
    with open('keyboard-letters.txt') as file:
        for line in file:
            lst = line.strip().split()
            adjacent_dict[lst[0]] = lst[1:]
    return adjacent_dict
KEY_ADJACENCY_FILE = store_adjacent_keys()
def store_legal_words():
    """
    Store legal words from provided file.
    :return: A set of all legal words
    """
    lst = set()
    with open('american-english.txt') as file:
        for line in file:
            lst.add(line.strip())
    return lst
LEGAL_WORD_FILE = store_legal_words()

def strip_punctuation(st):
    """
    Strip off the punctuations from the front and the end of a string
    :param st: Any string
    :return: the left, right punctuations of the string and the string without punctuations.
    """
    string_strip = ""
    if not re.search('[a-zA-Z0-9]',st):
        return st,"",""
    elif re.search('[a-zA-Z0-9]',st):
        lst_punc = re.split('([a-zA-Z0-9])',st)
        for item in lst_punc[1:-1]:
            string_strip = string_strip + item
        return lst_punc[0],string_strip,lst_punc[-1]


def contain_decimal(st):
    """
    Check if there is any number in the string
    :param st: The checking string
    :return: True if there is number in the string and False otherwise.
    """
    return re.search('\d',st)