#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Character Frequency Counter

def freq_counter(inp: str) -> dict:
    '''Count the frequency of characters'''
    counter = {}
    for chr in inp:
        if not chr.isspace():
            counter[chr] = counter.get(chr, 0) + 1
        # counter[chr] = counter[chr]+1
    
    return counter


if __name__ == '__main__':
    input_string = input("Enter the String: ")
    counts = freq_counter(input_string)
    print(f'Character|Count')
    print('-'*30)
    for k,v in counts.items():
        print(k,'|',v)

