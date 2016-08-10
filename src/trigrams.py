# -*- coding: utf-8 -*-
"""docstring."""
import io
import re


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
        d.setdefault((a,b), []).append(value)
    return d


def process_file(filename):
    s = find_and_replace_specials(pull_in_file(filename))
    return generate_dictionary(create_tuples(s.split()))
