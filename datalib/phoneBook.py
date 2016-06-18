#!/usr/bin/python
'''
    Date: June 16, 2016
    Author: Gokul Rangarajan
    Description:    Module to handle Phone book
'''
from iolib.iputil import acceptint


def phonebook():
    print("\n\t\tEntering Phone book")
    print("\t\t~~~~~~~~~~~~~~~~~~~")
    print("\t\t 1.  Add a contact")
    print("\t\t 2.  Display phone book")
    print("\t\t 3.  Count contact")
    mnu = 'Select operation:'
    menu = acceptint(mnu)

    return
