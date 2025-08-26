#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate the Simple Interest v1.5
# si = (p*t*r) / 100

principal = 1000000
rate_of_interest = 0.07 # Percentage converted to decimal
time_in_months = 36

simple_interest = (principal * rate_of_interest * time_in_months) / 100

print('Simple interest is: '+ str(simple_interest))
