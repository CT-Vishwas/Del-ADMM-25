#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Handling csv File

import csv
import re

def extract_year(titleyear: str)-> dict:
    # title = titleyear[:titleyear.find('(')]
    # year = titleyear[titleyear.find('(')+1:-1]
    # return {'title': title, 'year': year}

    pattern = r"^(.+)\s\((\d{4})\)$"
    match = re.match(pattern, titleyear)

    d1 = {}
    if match:
        d1['title'] = match.group(1)
        d1['year'] = match.group(2)

    return d1

def process_movies_csv(csv: dict):
    for row in csv:
        print(extract_year(row['title']))

if __name__ == '__main__':
    FILEPATH = 'movies/movies.csv'
    with open(FILEPATH, encoding='utf-8') as fh:
        csv_reader = csv.DictReader(fh)
        # print(csv_reader.fieldnames)
        process_movies_csv(csv_reader)
        # print(csv_reader.__dict__)
        # for row in csv_reader:
        #     print(row['title'])




# if __name__ == '__main__':
#     FILEPATH = 'movies/movies.csv'
#     with open(FILEPATH, encoding='utf-8') as fh:
#         # csv_reader = csv.reader(fh)
#         # csv_reader = fh.readlines().split(',')
#         num_of_rows = 10
#         count = 1
#         for row in csv_reader:
#             print(row)
#             count += 1
#             if count == num_of_rows:
#                 break

