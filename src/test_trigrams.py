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
    assert find_and_replace_specials('this *-# has *(#$ special @)# chars') == 'this     has      special     chars'


def test_create_tuples():
    """docstring."""
    from trigrams import create_tuples
    assert