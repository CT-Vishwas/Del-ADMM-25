#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to sum 10 numbers

nums = list(map(int, input('Enter the numbers seperated by spaces: ').split()))
print('The sum of numbers is: ',sum(nums))
nums.sort(reverse=True)
second_highest = nums[1]
print('The second highest number is: ',second_highest )