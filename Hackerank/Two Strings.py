# Two Strings program in Python3
import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# When we use & on sets it returns common elements, it's used in if statement 
def twoStrings(s1, s2):
    return 'YES' if set(s1) & set(s2) else 'NO'

  
# below code will be autogenerated
if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        q = int(input().strip())

        for _ in range(q):
            s1 = input()

            s2 = input()

            result = twoStrings(s1, s2)

            fptr.write(result + '\n')


# ----------------------------
# Sample input1:
# 2
# hello
# world
# hi
# world
# ----------------------------
# Sample output:
# YES
# NO
# ----------------------------
# Sample input2:
# 1
# program
# anagram
# ----------------------------
# Sample output:
# YES
# ----------------------------
