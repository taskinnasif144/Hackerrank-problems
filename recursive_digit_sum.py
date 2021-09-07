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