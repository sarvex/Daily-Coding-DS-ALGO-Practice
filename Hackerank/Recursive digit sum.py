#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    n = str(sum(int(i) for i in n) * k);
    if len(n) > 1:
        n = sum(int(i) for i in n);
        k = 1;
        return superDigit(str(n),k);
    return n;


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        nk = input().split()

        n = nk[0]

        k = int(nk[1])

        result = superDigit(n, k)

        fptr.write(str(result) + '\n')
