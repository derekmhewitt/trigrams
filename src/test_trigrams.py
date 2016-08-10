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
