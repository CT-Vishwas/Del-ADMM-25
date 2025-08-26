#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate the Simple Interest v1.5
# si = (p*t*r) / 100

principal = float(input('Enter the Principal amount: '))
rate_of_interest = float(input('Enter the rate of interest in decimal (Ex: 7% is 0.07): ')) # Percentage converted to decimal
time_in_months = int(input('Enter time in months(Ex: 3 yrs is 36 months): '))

simple_interest = (principal * rate_of_interest * time_in_months) / 100

# print('Simple interest is: '+ str(simple_interest))
# print('Simple interest is:', simple_interest)
# print('Simple interest for %.2f principal %i months with %.2f rate is: %.2f'%(principal, time_in_months, rate_of_interest, simple_interest))
# print('Simple interest for {0} principal {1} months with {2} rate is: {3}'.format(principal, time_in_months, rate_of_interest, simple_interest))
print(f'Simple interest for {principal:.2f} principal {time_in_months} months with {rate_of_interest:.2f} rate is: {simple_interest:.2f}')