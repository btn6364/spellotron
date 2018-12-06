"""
File_name: spellotron.py
Name: Bao Nguyen <btn6364@rit.edu>
Class: CSCI 141
Assignment: Project
Language: Python 3
"""


from test_adjacent_key import *
from test_missing_key import *
from test_extra_key import *
import sys

def ordered_correction(word):
    """
    Order of Correction Attempts. From adjacent key -> missing key -> extra key
    :param word: Any word
    :return: the word if it is legal and the first fixed word otherwise
    """
    adjacent_fix = test_adjacent_key(word)
    missing_fix = test_missing_key(word)
    extra_fix = test_extra_key(word)
    if adjacent_fix == 'Number' or adjacent_fix == word:
        return word
    elif adjacent_fix == None:
        if missing_fix == 'Number' or missing_fix == word:
            return word
        elif missing_fix == None:
            if extra_fix == 'Number' or extra_fix == word:
                return word
            elif extra_fix == None:
                return 'Unknown'
            else:
                return extra_fix
        else:
            return missing_fix
    else:
        return adjacent_fix

def words_process(text_source):
    """
    Process the file according to the words command line
    :param text_source: The source needed to read from
    :return: None
    """
    read_word, correct_word, unknown_word = 0, 0, 0
    correct_lst, unknown_lst = [], []
    for line in text_source:
        lst = line.strip().split()
        for word in lst:
            read_word += 1
            fix = ordered_correction(word)
            if fix == word:
                pass
            elif fix == 'Unknown':
                unknown_word += 1
                unknown_lst.append(word)
            else:
                correct_word += 1
                correct_lst.append(word)
                print(word, '->', fix)
    print()
    print(str(read_word), 'words read from file.')
    print()
    print(str(correct_word),'Corrected Words.')
    print(correct_lst)
    print(str(unknown_word),'Unknown Words.')
    print(unknown_lst)


def replace(lst,replacement,value):
    """
    Replace a value in a list with its replacement
    :param lst: Any non-empty lst
    :param replacement: The replace value
    :param value: The original value
    :return: The new list with replacement.
    """
    for idx in range(len(lst)):
        if lst[idx] == value:
            lst[idx] = replacement
    return lst


def lines_process(text_source):
    """
    Process the file according to the lines command line.
    :param text_source: The source needed to read from.
    :return: None
    """
    read_word, correct_word, unknown_word = 0, 0, 0
    correct_lst, unknown_lst = [], []
    for line in text_source:
        lst = line.strip().split()
        for word in lst:
            read_word += 1
            fix = ordered_correction(word)
            if fix == word:
                pass
            elif fix == 'Unknown':
                unknown_word += 1
                unknown_lst.append(word)
            else:
                correct_word += 1
                correct_lst.append(word)
                lst = replace(lst,fix,word)
        print(" ".join(lst))
    print()
    print(str(read_word), 'words read from file.')
    print()
    print(str(correct_word), 'Corrected Words.')
    print(correct_lst)
    print(str(unknown_word), 'Unknown Words.')
    print(unknown_lst)



def main():
    """
    The main function that implement the use of the command lines.
    :return: None
    """
    command_set = ['words','lines']
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: python3.7 spellotron.py words/lines [filename]', file=sys.stderr)
    elif len(sys.argv) == 2:
        if sys.argv[0] != 'spellotron.py' or sys.argv[1] not in command_set:
            print('Usage: python3.7 spellotron.py words/lines [filename]', file=sys.stderr)
        else:
            text_source = sys.stdin
            if sys.argv[1] == 'words':
                words_process(text_source)
            elif sys.argv[1] == 'lines':
                lines_process(text_source)
    else: #len(sys.argv) == 3
        if sys.argv[0] != 'spellotron.py' or sys.argv[1] not in command_set:
            print('Usage: python3.7 spellotron.py words/lines [filename]', file=sys.stderr)
        else:
            text_source = open(sys.argv[2])
            if sys.argv[1] == 'words':
                words_process(text_source)
            elif sys.argv[1] == 'lines':
                lines_process(text_source)
            text_source.close()

if __name__ == '__main__':
    main()




