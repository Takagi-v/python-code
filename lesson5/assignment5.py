#1.	给定一个list的数，求其 和 和 乘积
def list_sum_mul(a):
    mul = 1
    for i in a:
        mul *= i
    return sum(a), mul

#2.	给定两个列表，判断两个列表中是否有一个包含另一个的所有元素，返回True以及较大的list, 否则返回False.
def check_inclu(a, b):
    if len(a) > len(b):
        c = a
        a = b
        b = c
    for i in a:
        if not i in b:
            return False
    return b

#3.	Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
for i in range(2, 10, 2):
    for j in range(0, 10, 2):
        for s in range(0, 10, 2):
            for o in range(0, 10, 2):
                print(i, end="")
                print(j, end="")
                print(s, end="")
                print(o, end=" ")

#4.	With a given list [12, 24, 35, 24, 88, 120, 155, 88, 120, 155], write a program to print this list after removing all duplicate values with original order reserved.
a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
res = []
[res.append(i) for i in a if i not in res]
print(res)

#5.	用列表实现如下两个函数:给定一个 正整数，将整数中的数字进行反转；给定一个 负整数，将整数中的数字进行反转。
n = int(input())
lst = []
cnt = 1
if n < 0:
    cnt = 0
    n = abs(n)
while n > 0:
    x = n % 10
    n //= 10
    lst.append(x)
if not cnt:
    print("-", end="")
for i in range(0, len(lst)):
    print(lst[i], end="")

#6.	请实现以下功能：写出一个函数，该函数的返回值为两个lists的交集，如果没有交集，则返回False并打印出“no intersection”
def intersection(a, b):
    lst = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                lst.append(i)
                cnt = 1
    return lst if cnt == 1 else False


a = input()
b = input()
a = a[1 : len(a) - 1]
b = b[1 : len(b) - 1]
lst_a = a.split(", ")
lst_b = b.split(", ")
for i in range(len(lst_a)):
    lst_a[i] = int(lst_a[i])
for i in range(len(lst_b)):
    lst_b[i] = int(lst_b[i])
print(intersection(lst_a, lst_b))
if not intersection(lst_a, lst_b):
    print("no intersection")

#7.	Write a Python program to construct the following pattern, using a nested for loop.
def print_star(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(i, 0, -1):
            print("*", end="")
        print()


n = int(input())
print_star(n)

#8.	Given a positive integer n, count the total number of digits in a number. 
def count_digit(n):
    lst = [0] * 10
    while n > 0:
        x = n % 10
        lst[x] += 1
        n //= 10
    return lst


n = int(input())
a = count_digit(n)
print(a)

#9.	Find the sum of the series 2 +22 + 222 + 2222 + 2…..2: there are n 2’s in the last term.
def sum_of_two(n):
    sum = 0
    x = 2
    for i in range(n):
        sum += x
        x = x * 10 + 2
    return sum


n = int(input())
print(sum_of_two(n))

#10.	使用list创建两个矩阵如下，即1，2，…,10的排列
n = int(input())
ma1 = [[0] * n for i in range(n)]
for i in range(0, n):
    for j in range(0, n):
        ma1[i][j] = i + 1
ma2 = [[0] * n for i in range(n)]
for i in range(0, n):
    for j in range(0, n):
        ma2[i][j] = j + 1
print(ma1)
print(ma2)

#11.	给定一个列表A，假定A具有结构：存在0<=i<=n-1(n为列表长度)，满足A[0]<=A[1]<= ... <= A[i] >= A[i+1]>=...>=A[n-1], 输入A，输出满足上述条件的最小的i
def find_min(lst):
    maxx = -1e6
    for i in range(0, len(lst)):
        if lst[i] >= maxx:
            maxx = lst[i]
    for i in range(0, len(lst)):
        if lst[i] == maxx:
            return i


a = [1, 2, 3, 4, 4, 5, 5, 5, 4, 3, 2]
print(find_min(a))

#12.	Sieve of Eratosthenes (筛法)
def get_prime():
    global cnt
    for i in range(2, n + 1):
        if not st[i]:
            primes[cnt] = i
            cnt += 1
        for j in range(cnt):
            if primes[j] > (n / i):
                break
            st[primes[j] * i] = True
            if i % primes[j] == 0:
                break


primes = [0] * 1000000
st = [False] * 10000000
n = 1000000
cnt = 0
a = int(input())
get_prime()
print(not st[a])
for i in range(0, cnt):
    print(primes[i], end=" ")

