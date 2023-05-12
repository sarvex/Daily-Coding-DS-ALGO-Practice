import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxsum = -99
    
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bot = sum(arr[i+2][j:j+3])
            
            hourglass = top+mid+bot
            
            maxsum = max(hourglass,maxsum)
    return maxsum
    
if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        arr = [list(map(int, input().rstrip().split())) for _ in range(6)]
        result = hourglassSum(arr)

        fptr.write(str(result) + '\n')
