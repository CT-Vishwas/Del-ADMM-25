#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Script to calculate rent per sq ft in house rent dataset

import csv
import numpy as np

if __name__ == '__main__':
    filePath = 'house_rent.csv'
    # Read the file
    rents = []
    sizes = []
    with open(filePath) as fh:
        csv_reader = csv.DictReader(fh)
        for row in csv_reader:
            rents.append(row['Rent'])
            sizes.append(row['Size'])
    
    rents_arr = np.array(rents, dtype='f')
    sizes_arr = np.array(sizes,dtype='f')

    rents_per_sq_ft = rents_arr/sizes_arr
    print('Rents per sq ft: ')
    for idx in range(10):
        print(f"{rents_per_sq_ft[idx]:.2f}")

