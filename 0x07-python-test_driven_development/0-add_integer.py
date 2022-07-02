#!/usr/bin/python3
"""
    This is the add_integer module
    This module gives one function that adds two integers, add_integer(a, b)
"""


def add_integer(a, b=98):
    """Returns the sum of 2 numbers"""
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
