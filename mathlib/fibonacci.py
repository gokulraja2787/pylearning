#!/usr/bin/python
'''
    Author: Gokul Rangarajan
    Date:   May 12, 2016
    Description: Module to calculate fibonacci series
    for given n numbers
'''
SERIES_1 = 0
SERIES_2 = 1


def fibn(n):
    if n <= 0:
        raise Exception("n cannot be 0, imaginary number")
    print("The fibonacci series are: ")
    if n >= 1:
        print("%d" % SERIES_1)
    if n >= 2:
        print(" %d" % SERIES_2)
    n -= 2
    prev = SERIES_2
    cnt = SERIES_1 + SERIES_2
    while n > 0:
        print(" %d" % cnt)
        n -= 1
        tmp = cnt
        cnt += prev
        prev = tmp
