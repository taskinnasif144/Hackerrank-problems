def powerSum(x, n, a=1, lim=0):
    # base cases
    if x == 0:
        return 1
    if x < 0:
        return 0
    # actual logic
    if lim == 0:
        lim = int(x ** (1 / n))
    sum = 0
    for i in range(a, lim + 1):
        new_x = x - (i ** n)
        a = a + 1
        val = powerSum(new_x, n, a, lim)
        sum += val
    return sum


print(power_sum(100, 2))
