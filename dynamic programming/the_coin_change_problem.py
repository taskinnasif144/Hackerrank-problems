# problem link: https://www.hackerrank.com/challenges/coin-change/problem?isFullScreen=false
# to test the code please go to the following link and copy paste the codes below and submit it


import math
import os
import random
import re
import sys


def getWays(amount, coins, memo={}):
    # base cases
    if amount == 0: return 1
    if amount < 0: return 0

    #part of dynamic
    memoChecker = str(amount) + str(coins)
    if memoChecker in memo:
        return memo[memoChecker]

    # sortings
    coins = sorted(coins)

    #Logics
    total = 0
    for coin in coins:
        res = getWays(amount - coin, coins[coins.index(coin):], memo)
        total += res
    memo[memoChecker] = total
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
