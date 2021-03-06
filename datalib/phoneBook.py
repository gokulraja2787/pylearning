#!/usr/bin/python
"""
    Date: June 16, 2016
    Author: Gokul Rangarajan
    Description:    Module to handle Phone book
"""
from iolib.iputil import acceptint, acceptstring

book = []
NAME = 'Name'
CELL = 'Cell'


def addcontact(name, phone):
    entry = {NAME: name, CELL: phone}
    book.append(entry)


def countcontacts():
    return len(book)


def listcontacts():
    for b in book:
        print("%s : %s\n" % (b[NAME], b[CELL]))



def phonebook():
    print("\n\t\tEntering Phone book")
    print("\t\t~~~~~~~~~~~~~~~~~~~")
    menu = None
    while (None == menu or menu != 0):
        print("\t\t 1.  Add a contact")
        print("\t\t 2.  Display phone book")
        print("\t\t 3.  Count contact")
        print("\t\t 0.  Exit PhoneBook")
        mnu = 'Select operation:'
        menu = acceptint(mnu)
        if 1 == menu:
            mnu = 'Enter the Name: '
            name = acceptstring(mnu)
            mnu = 'Enter the Phone Number:'
            phone = acceptint(mnu)
            addcontact(name, phone)
        elif 2 == menu:
            listcontacts()
        elif 3 == menu:
            print("Size of PhoneBook is: %d" % countcontacts())
    return
