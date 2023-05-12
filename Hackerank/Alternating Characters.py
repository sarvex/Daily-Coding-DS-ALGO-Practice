#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    return sum(1 for i in range(1,len(s)) if s[i]==s[i-1])

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        q = int(input())
        for _ in range(q):
            s = input()
            result = alternatingCharacters(s)
            fptr.write(str(result) + '\n')
