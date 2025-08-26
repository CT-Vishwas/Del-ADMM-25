#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Reading a File

try:
    with open('movies/movies.csv','rt', encoding='utf-8') as f: 
        data = f.readlines()
        print(len(data))
except FileNotFoundError:
    print('File you are trying to read is not available')