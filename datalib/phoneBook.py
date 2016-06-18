#!/usr/bin/python
"""
    Date: June 16, 2016
    Author: Gokul Rangarajan
    Description:    Module to handle Phone book
"""
from iolib.iputil import acceptint

book = []
NAME = 'Name'
CELL = 'Cell'


def addcontact(name, phone):
    entry = {NAME: name, CELL: phone}
    book.append(entry)
    pass


def countContact():
    return len(book)

def phonebook():
    print("\n\t\tEntering Phone book")
    print("\t\t~~~~~~~~~~~~~~~~~~~")
    print("\t\t 1.  Add a contact")
    print("\t\t 2.  Display phone book")
    print("\t\t 3.  Count contact")
    print("\t\t 0.  Exit PhoneBook")
    menu = None
    while (None == menu or menu != 0):
        mnu = 'Select operation:'
        menu = acceptint(mnu)
        if 3 == menu:
            print("Size of PhoneBook is: %d" % len(book))
    return
