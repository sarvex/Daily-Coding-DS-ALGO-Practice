#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the pangrams function below.
ascii_array = []
def pangrams(s):
    lower_s = s.lower()
    for i in range(len(lower_s)):
        ascii_array.append(ord(lower_s[i]))
    return next(
        ("not pangram" for i in range(97, 123) if i not in ascii_array),
        'pangram',
    )

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        s = input()
        result = pangrams(s)
        fptr.write(result + '\n')
