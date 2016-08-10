# -*- coding: utf-8 -*-
"""docstring."""
import pytest


def test_pull_in_file():
    """docstring."""
    from trigrams import pull_in_file
    assert pull_in_file('filetest.txt') == 'this is a test file'


def test_find_and_replace_specials():
    """docstring."""
    from trigrams import find_and_replace_specials
    result = find_and_replace_specials('this *-# has *(#$ special @)# chars')
    out = 'this     has      special     chars'
    assert result == out


def test_create_tuples_1():
    """docstring."""
    from trigrams import create_tuples
    input_list = ['hello', 'world', 'test']
    out = [('hello', 'world', 'test')]
    assert list(create_tuples(input_list)) == out


def test_create_tuples_2():
    """docstring."""
    from trigrams import create_tuples
    input_list = ['hello', 'world', 'test', 'tttest']
    out = [('hello', 'world', 'test'), ('world', 'test', 'tttest')]
    assert list(create_tuples(input_list)) == out


def test_generate_dictionary_1():
    from trigrams import generate_dictionary
    tuples = [('hello', 'world', 'test'), ('world', 'test', 'tttest')]
    assert generate_dictionary(tuples) == {
        ('hello', 'world'): ['test'],
        ('world', 'test'): ['tttest']
    }


def test_generate_dictionary_2():
    from trigrams import generate_dictionary
    tuples = [
        ('I', 'wish', 'I'),
        ('wish', 'I', 'may'),
        ('I', 'may', 'I'),
        ('may', 'I', 'wish'),
        ('I', 'wish', 'I'),
        ('wish', 'I', 'might')
    ]
    assert generate_dictionary(tuples) == {
        ('I', 'wish'): ['I', 'I'],
        ('wish', 'I'): ['may', 'might'],
        ('may', 'I'):  ['wish'],
        ('I', 'may'):  ['I']
    }


def test_process_file():
    from trigrams import process_file
    assert process_file('filetest.txt') == {
        ('a', 'test'): ['file'],
        ('is', 'a'): ['test'],
        ('this', 'is'): ['a']
    }


def test_pick_first_two_words():
    from trigrams import pick_first_two_words
    assert pick_first_two_words({(1, 2): 3}) == (1, 2)
