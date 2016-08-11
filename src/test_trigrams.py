# -*- coding: utf-8 -*-
"""Here we test our functions from trigrams.py."""
import pytest

GENERATE_SENTENCE_TEST_TABLE = [
    7,
    4,
    12
]


def test_pull_in_file():
    """Function tests pull_in_file function with test file."""
    from trigrams import pull_in_file
    assert pull_in_file('filetest.txt') == 'this is a test file'


def test_find_and_replace_specials():
    """Function tests find_and_replace_specials function with special
    characters and text.
    """
    from trigrams import find_and_replace_specials
    result = find_and_replace_specials('this *-# has *(#$ special @)# chars')
    out = 'this     has      special     chars'
    assert result == out


def test_generate_dictionary_1():
    """Function tests generate_dictionary with test data."""
    from trigrams import generate_dictionary
    sentence = 'hello world test tttest'.split()
    assert generate_dictionary(sentence) == {
        ('hello', 'world'): ['test'],
        ('world', 'test'): ['tttest']
    }


def test_generate_dictionary_2():
    """Function tests generate_dictionary with test data."""
    from trigrams import generate_dictionary
    sentence = 'I wish I may I wish I might'.split()
    assert generate_dictionary(sentence) == {
        ('I', 'wish'): ['I', 'I'],
        ('wish', 'I'): ['may', 'might'],
        ('may', 'I'): ['wish'],
        ('I', 'may'): ['I']
    }


def test_process_file():
    """Function tests process_file with test data."""
    from trigrams import process_file
    assert process_file('filetest.txt') == {
        ('a', 'test'): ['file'],
        ('is', 'a'): ['test'],
        ('this', 'is'): ['a']
    }


def test_pick_first_two_words():
    """Function tests pick_first_two_words with test data."""
    from trigrams import pick_first_two_words
    assert pick_first_two_words({(1, 2): 3}) == (1, 2)


@pytest.mark.parametrize('n', GENERATE_SENTENCE_TEST_TABLE)
def test_generate_sentence(n):
    """Function tests generate_sentence with test data."""
    from trigrams import generate_sentence
    d = {
        ('a', 'test'): ['file'],
        ('is', 'a'): ['test'],
        ('this', 'is'): ['a']
    }
    assert len(generate_sentence(d, n).split()) == n
