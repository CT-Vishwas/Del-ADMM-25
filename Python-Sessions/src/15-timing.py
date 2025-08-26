#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to timing a function

from utilities import timer


@timer
def my_function():
    total = 0
    for i in range(10**7):
        total += i
    return total

if __name__ == '__main__':
    print("Result: ", my_function())

