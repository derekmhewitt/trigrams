# -*- coding: utf-8 -*-
"""docstring."""
import io
import re
import random


def pull_in_file(filename):
    """docstring."""
    file = io.open(filename)
    content = file.read()
    file.close()
    return content


def find_and_replace_specials(content):
    """docstring."""
    return re.sub('[-\\()!@#$%^&*;"<>|/,.1234567890_=+:]', ' ', content)


def create_tuples(t):
    return zip(t, t[1:], t[2:])


def generate_dictionary(tuples):
    d = {}
    for a, b, value in tuples:
        d.setdefault((a, b), []).append(value)
    return d


def process_file(filename):
    s = find_and_replace_specials(pull_in_file(filename))
    return generate_dictionary(create_tuples(s.split()))


def pick_first_two_words(dictionary):
    return random.choice(list(dictionary))


def new_starting_point(dictionary):
    return pick_first_two_words(dictionary)[0]


def generate_sentence(dictionary, length):
    result = ""
    word1, word2 = pick_first_two_words(dictionary)
    for i in range(length):
        result += '{} '.format(word1)
        possible_words = dictionary.get((word1, word2), False)
        if possible_words:
            word1, word2 = word2, random.choice(possible_words)
        else:
            word1, word2 = pick_first_two_words(dictionary)
    return result


print(generate_sentence(process_file('filetest.txt'), 50))
