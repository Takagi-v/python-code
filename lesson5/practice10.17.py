def my_sum(n):
    sum1 = 0
    for i in range(n + 1):
        sum1 += i
    sum2 = 0
    cnt = 0
    while cnt <= n:
        sum2 += cnt
        cnt += 1
    sum3 = 0
    lst = [x for x in range(1, n + 1)]
    sum3 = sum(lst)
    return sum1, sum2, sum3


def my_AG(a, d, n):
    sum1 = 0
    for i in range(n + 1):
        sum1 = sum1 + a + d * i
    sum2 = 0
    cnt = 1
    while cnt <= n:
        sum2 = sum2 + a + d * cnt
        cnt += 1
    sum3 = 0
    lst = [a + d * x for x in range(1, n + 1)]
    sum3 = sum(lst)


def my_power(x, n):
    sum1 = 1
    for i in range(n):
        sum1 *= x
    sum2 = 1
    cnt = 1
    while cnt <= n:
        sum2 *= x
        cnt += 1


def my_polynomial(a, x, n):
    sum1 = 0
    lst = [a[i] * x**i for i in range(n + 1)]
    sum1 = sum(lst)
