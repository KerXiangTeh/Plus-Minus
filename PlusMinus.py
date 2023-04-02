#!/bin/python3

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arrSize = len(arr)
    neg = 0
    pos = 0
    zero = 0
    
    for num in arr:
        if num > 0 : pos += 1
        elif num < 0: neg += 1
        elif num == 0: zero += 1
        else: raise ValueError("Invalid input: {}".format(num))
    
    negRatio = neg/arrSize
    posRatio = pos/arrSize
    zeroRatio = zero/arrSize
    
    print(f"{posRatio:.6f}")
    print(f"{negRatio:.6f}")
    print(f"{zeroRatio:.6f}")
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
