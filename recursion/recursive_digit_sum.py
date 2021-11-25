def superDigit (n, k):
    if int(n) < 10:
        return n
    sum = 0
    for i in n:
        sum += int(i)
    sum = sum * k
    if sum >= 10:
        return superDigit(str(sum), 1)
    return sum
    



res = superDigit('148', 3)
print(res)


def kFactorization(n, A):
    if n == 1:
        return True, []
    if n < 1:
        return False, -1
    
    for a in A:
        factor = n/a
        sol, res = kFactorization(factor, A)
        if sol:
            return True, [factor] + res
    return False, -1


ans = kFactorization(12, [2, 3, 4])

print(ans)

for prob in probabilities:
        if not isinstance(prob, list):
            temp_list1.append(prob)
        else:
            for p in prob:
                temp_list2.append(p)