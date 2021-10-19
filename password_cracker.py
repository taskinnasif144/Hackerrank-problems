#problem link: https://www.hackerrank.com/challenges/password-cracker/problem?isFullScreen=true

import math
import os
import random
import re
import sys
sys.setrecursionlimit(200000)
# here the set recussion limit is a very important part, all tho the time complexity and space complexicity
# is o(n) but the n being too long, we need to set the recustion limit to higher digits


memo = {}
def stepsToSolve(passwords, loginAttempt):
    global memo

    if loginAttempt == '':
        return True, []
    if loginAttempt in memo:
        return False, []
    
    for password in passwords:
        if loginAttempt.startswith(password):
            memo[loginAttempt] = True
            sol, words = stepsToSolve(passwords, loginAttempt[len(password):])
            if sol: 
                return True, [password] + words
    return False, []

def passwordCracker(passwords, loginAttempt):
    global memo
    memo = {}
    sol, words = stepsToSolve(passwords, loginAttempt)
    if sol:
        return ' '.join(words)
    else:
        return "WRONG PASSWORD"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)

        fptr.write(result + '\n')

    fptr.close()