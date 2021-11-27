# problem link: https://www.hackerrank.com/challenges/k-factorization/problem?isFullScreen=false
# to test the code please go to the following link and copy paste the codes below and submit it


import math
import os
import random
import re
import sys

#
# Complete the 'kFactorization' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY A
#


def stepsToFollow(n, A, memo  = {}):
    # base cases
    if n == 1: return True, [1]
    if n < 1: return False, -1
    if n in memo:
        if not memo[n]:
            return False, -1
        return True, memo[n]
    # actual logic
    optimalRes = []
    for num in A:
        if n % num == 0:
            new_n = int(n / num) 
            sol, res = stepsToFollow(new_n, A, memo)
            if sol:
                res = res + [n]
                if len(optimalRes) == 0:
                    optimalRes = res
                if len(res) < len(optimalRes):
                    optimalRes = res
                if len(res) == len(optimalRes):
                    if sorted(res) == sorted(optimalRes):
                        optimalRes = sorted(res)
                    else:
                        isTrue = True
                        res = sorted(res)
                        optimalRes = sorted(optimalRes)
                        for i in range(len(res)):
                            if res[i] > optimalRes[i]:
                                isTrue = False
                        if isTrue:
                            optimalRes = res
    memo[n] = optimalRes
    if len(optimalRes) == 0:
        memo[n] = False
        return False, -1
    else: 
        return True, optimalRes
    
def  kFactorization(n, A):
    sol, res = stepsToFollow(n, A)
    if sol:
        return res
    else:
        return [-1]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
