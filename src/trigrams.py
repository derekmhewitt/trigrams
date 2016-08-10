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
