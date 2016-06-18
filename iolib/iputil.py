#!/usr/bin/python
'''
    Author: Gokul Rangarajan
    Date:   May 12, 2016
    Description: Input Utility
'''


def acceptint(msg):
    if (None == msg) or (not isinstance(msg, str)) or (msg.strip() == ''):
        msg = 'Enter a Integer value: '
    n = None
    while (None == n):
        n = input(msg)
        try:
            n = int(n)
        except ValueError:
            print("Invalid input")
            n = None
    return n


def acceptstring(msg):
    if (None == msg) or (not isinstance(msg, str)) or (msg.strip() == ''):
        msg = "Enter a value: "
    n = None
    while (None == n):
        n = input(msg)
    return n
