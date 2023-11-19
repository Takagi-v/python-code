import copy


def hadamard(k):
    lst = [[0] * 2**k] * 2**k
    if k == 0:
        return [[1]]
    lst1 = hadamard(k - 1)
    lst2 = copy.deepcopy(lst1)
    for i in range(0, len(lst2)):
        for j in range(0, len(lst2[i])):
            lst2[i][j] = -lst2[i][j]
    for i in range(1, 2 ** (k - 1) + 1):
        lst[i - 1] = lst1[i - 1] * 2
        lst[2 ** (k - 1) + i - 1] = lst1[i - 1] + lst2[i - 1]
    return lst


print(hadamard(3))
