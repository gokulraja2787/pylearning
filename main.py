#!/usr/bin/python
"""
    Author: Gokul Rangarajan
    Date:   May 7, 2016
    Description: First Project attempt
"""
from datalib.phoneBook import phonebook
from iolib.iputil import acceptint
from mathlib.fact import factorial
from mathlib.fibonacci import fibn

print("Welcome")
menu = None

while (None == menu or menu != 0):
    print('Operation Menu:')
    print('1. Factorial')
    print('2. Fibonacci')
    print('3. Enter phone book')
    print('0. Exit')
    mnu = 'Select operation:'
    menu = acceptint(mnu)
    if (1 == menu):
        n = acceptint('Enter a value for n: ')
        try:
            result = factorial(n)
            print("The result is %d" % result)
        except Exception as e:
            print(e)
    elif (2 == menu):
        n = acceptint('Enter the number of sequence: ')
        fibn(n)
    elif (3 == menu):
        phonebook()
    else:
        print('Ending')
print("Exit")
