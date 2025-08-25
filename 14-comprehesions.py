#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to demonstrate comprehensions

import csv

if __name__ == '__main__':
    filePath = 'house_rent.csv'
    # Read the file

    with open(filePath) as fh:
        csv_reader = csv.DictReader(fh)
        dict_prices = {idx: row for idx, row in enumerate(csv_reader) if int(row['Rent']) > 10000}
        
    for k,v in dict_prices.items():
        print(k,':',v)