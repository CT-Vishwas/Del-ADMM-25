#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# IP address validator

MAX_FIELDS = 4
MIN_VAL = 0
MAX_VAL = 255
SEPERATOR = '.'

def is_valid_ip(ipaddress):
    num_lst = ipaddress.split(SEPERATOR)
    
    if len(num_lst) != MAX_FIELDS:
        return False

    for field in num_lst:

        if not field.isnumeric():
            return False
        
        if not (int(field) >= MIN_VAL and int(field) <= MAX_VAL):
            return False
        
    return True


if __name__ == '__main__':
    ipaddress = input('Enter the IPv4 address: ')
    if is_valid_ip(ipaddress):
        print(f"The address {ipaddress} is VALID")
    else:
        print(f"The address {ipaddress} is INVALID")