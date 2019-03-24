#!/usr/bin/python
"""
    Author: Gokul Rangarajan
    Date:   March 23, 2019
    Description: class Mathlib
"""


class MathUtil:

    def __init__(self):
        self.SERIES_1 = 0
        self.SERIES_2 = 1

    def factorial(self, n):
        if n < 0:
            raise Exception('n cannot be less than 0')
        if 0 == n or 0 == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def fibonacci(self, n):
        result = []
        if n <= 0:
            raise Exception("n cannot be 0, imaginary number")
        print("The fibonacci series are: ")
        if n >= 1:
            result.append(self.SERIES_1)
        if n >= 2:
            result.append(self.SERIES_2)
        n -= 2
        prev = result[1]
        cnt = sum(result)
        while n > 0:
            result.append(cnt)
            n -= 1
            tmp = cnt
            cnt += prev
            prev = tmp
        return result

    def prime_xy(self, rangex, rangey):
        result = []
        if rangey > rangex:
            print("%i is %j", rangey, rangex)
        for num in range(rangex, rangey):
            for i in range(2, num-1):
                if num%i == 0:
                    break;
            else:
                result.append(num)
        return result
