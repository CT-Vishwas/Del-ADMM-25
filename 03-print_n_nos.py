#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to print 10 numbers
# Script to calculate sum of n numbers

# the number of steps - for
# exit condition - while

# start value is 0 by default
# n-1 is the end value
# for i in range(10):
#     print(i)

# set the start value, set the step value
# for i in range(1, 11, 2):
#     print(i)

# Print decreasing values
# for i in range(25, 0, -2):
#     print(i, end='-')

# initialization, condn, inc/dec
# x = 0
# while x < 10:
#     print(x, end=' ')
#     #x += 1

total = 0
while True:
    num = int(input('Enter a number: '))
    if num == -999:
        break
    else:
        total += num

print(f'The sum is: {total}')