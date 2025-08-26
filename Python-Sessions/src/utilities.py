#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Some Utilities
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time= time.time()
        result =func(*args, **kwargs)
        end_time = time.time()
        print("Execution time: ", end_time - start_time, 'seconds')

        return result
    return wrapper