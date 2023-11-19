#1. 实现定义在自然数上面的函数f(n):f(0)=1,f(1)=1,f(n) = f(f(n//2))+1
def f(n):
    return 1 if n == 0 or n == 1 else f(f(n // 2)) + 1

#2.	计算如下递归关系式, 分别用函数和循环解决
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

lst=[]
for i in range(0,n+1):
    lst.append([0]*(n+1))
for i in range(0, n + 1):
    lst[i][0] = 1
    lst[0][i] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        lst[i][j] = lst[i][j - 1] + lst[i - 1][j] - lst[i - 1][j - 1]
print(lst[n][n])
print(f(n, n))

#3.	Write a Python program of recursion list sum.
def list_sum(lst):
    if len(lst) == 0:
        return 0
    ans = 0
    for x in lst:
        if type(x) == type(0):
            ans += x
        if type(x) == type([]):
            ans += list_sum(x)
    return ans


a = [1, 2, [3, 4], [5, 6]]
print(list_sum(a))

#4.	Given a recursion list of numbers, determine the times of each number. 
def count_numbers(a):
    if len(a) == 0:
        return {}
    dt = {}
    for x in a:
        if type(x) == type(0):
            if x in dt:
                dt[x] += 1
            if x not in dt:
                dt[x] = 1
        if type(x) == type([x]):
            dt1 = count_numbers(x)
            for i in dt1:
                dt[i] += dt1[i]
    return dt


a = [1, 2, 3, 4, 5, 6, [3, 4, 5, 6], [5, 6]]
print(count_numbers(a))

#5. Implement the function Hadamard(k), which returns the Hadamard matrix H_(2^k ) for a given non-negative integer k.
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

#6.	Implement a function Powerset(S) to find a list of all subsets of the given set S (in any order you like).
def powersets(s):
    if len(s) == 1:
        for x in s:
            return {(x,)}
    dt = {()}
    for x in s:
        dt = dt.union(powersets(s - {x}))
    dt.add(tuple(s))
    return dt


a = {1, 2, 3, 4}
print(powersets(a))
