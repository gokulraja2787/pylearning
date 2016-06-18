#!/usr/bin/python
"""
    Author: Gokul Rangarajan
    Date:   May 7, 2016
    Description: Module to run factorial
"""


def factorial(n):
    if n < 0:
        raise Exception('n cannot be less than 0')
    if 0 == n or 0 == 1:
        return 1
    else:
        return n * factorial(n - 1)
