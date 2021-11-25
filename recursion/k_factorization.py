import itertools

def kFactorization(n, A, summit=True):
    if n == 1:
        return True, []
    if n < 1:
        return False, -1
    
    probabilities = []
    temp_list1 = []
    temp_list2 = []
    temp_list3 = []

    for a in A:
        new_n = n / a
        sol, res = kFactorization(new_n, A, False)
        if sol:
            res = [new_n] + res
            probabilities.append(res)
        
    for p in probabilities:
        for prob in p:
            if not isinstance(prob, list):
                temp_list1.append(prob)
            else:
                temp_list2.append(prob)

        for i in temp_list2:
            res = i + temp_list1
            temp_list3.append(res)
    
    probabilities = temp_list3

    if not len(probabilities) == 0:
        return True, probabilities
    else:
        return False, -1
    


ans, items = kFactorization(12, [2, 3])

print(items)
