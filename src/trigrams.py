# -*- coding: utf-8 -*-
"""Trigrams.py generates pseudo random text outputgiven a large
text file input.
"""

import io
import re
import random
import sys


def pull_in_file(filename):
    """Read the text from the filename it's given."""
    file = io.open(filename)
    content = file.read()
    file.close()
    return content


def find_and_replace_specials(content):
    """Function replaces special characters with whitespace."""
    return re.sub('[-\\()!@#$%^&*;"<>|/1234567890_=+:]', ' ', content)


def generate_dictionary(tups):
    """Function generates a dictionary from our tuples."""
    d = {}
    for a, b, value in zip(tups, tups[1:], tups[2:]):
        d.setdefault((a, b), []).append(value)
    return d


def process_file(filename):
    """Function calls above functions in order to process the file into a
    dictionary for use in following functions.
    """
    s = find_and_replace_specials(pull_in_file(filename))
    return generate_dictionary(s.split())


def pick_first_two_words(dictionary):
    """Function picks a random starting place in our dictionary."""
    return random.choice(list(dictionary))


def next_sentence_state(dictionary, word1, word2):
    """Generates the next state for generate_sentence. Purely a helper
    function for generate_sentence.
    """
    possible_words = dictionary.get((word1, word2), False)
    if possible_words:
        word1, word2 = word2, random.choice(possible_words)
    else:
        word1, word2 = pick_first_two_words(dictionary)
    return word1, word2


def generate_sentence(dictionary, length):
    """Return a generated sentence of the given length"""
    result = ""
    word1, word2 = pick_first_two_words(dictionary)
    for i in range(length):
        result += '{} '.format(word1)
        word1, word2 = next_sentence_state(dictionary, word1, word2)
    return result


def generate_from_args():
    """Generate a sentence from the command line.
    """
    try:
        arg1 = sys.argv[1]
        arg2 = int(sys.argv[2])
        print(generate_sentence(process_file(arg1), arg2))
    except ValueError:
        print('User supplied invalid length argument.')


def help():
    print('USAGE:')
    print('  python trigrams.py input length')
    print('where input is a text file and length is the number')
    print('of words to generate.')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        generate_from_args()
    else:
        help()
