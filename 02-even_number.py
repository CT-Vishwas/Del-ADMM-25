#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate Even Number

num = int(input('Enter a number: '))

remainder = num % 2

if remainder == 0:
    print(f'The number {num} is Even')
    print('I am still inside the if block')
else:
    print(f'The number {num} is odd')

print('I am outside the if block')