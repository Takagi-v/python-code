# 2.	计算如下递归关系式, 分别用函数和循环解决
def count1(n):
    if n == 1 or n == 0:
        return 1
    return count1(n - 1) + count1(n - 2)


def count2(n):
    if n == 1 or n == 0 or n == 2:
        return 1
    return count2(n - 1) + 2 * count2(n - 2) - count2(n - 3)


def count3(n):
    if n == 0:
        return 2
    if n == 1:
        return 3
    return count3(n - 1) * count3(n - 2)


def f(m, n):
    if m == 0 or n == 0:
        return 1
    return f(m, n - 1) + f(m - 1, n) - f(m - 1, n - 1)


lst = [1, 1]
n = 10
for i in range(2, n + 1):
    lst.append(lst[i - 1] + lst[i - 2])
print(lst[n])
print(count1(n))

lst = [1, 1, 1]
for i in range(3, n + 1):
    lst.append(lst[i - 1] + lst[i - 2] * 2 - lst[i - 3])
print(lst[n])
print(count2(n))

lst = [2, 3]
for i in range(2, n + 1):
    lst.append(lst[i - 1] * lst[i - 2])
print(lst[n])
print(count3(n))

lst = [[0] * (n + 1)] * (n + 1)
for i in range(0, n + 1):
    lst[i][0] = 1
    lst[0][i] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        lst[i][j] = lst[i][j - 1] + lst[i - 1][j] - lst[i - 1][j - 1]
print(lst[n][n])
print(f(n, n))
