import time


def prime_Miller_Rabin(n):
    time_start = time.time()
    number_pn = 0
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    k = 0
    t = n - 1
    while t & 1 == 0:
        k += 1
        t >>= 1
    s=[2,3,5]
    for j in s:
        a = j
        b = pow(a, t, n)
        tmp = 0
        if b == 1:
            continue
        for i in range(k):
            if b==n-1:
                tmp = 1
                break
            else:
                b = (b * b) % n
        if tmp == 1:
            continue
        else:
            return False
    time_end = time.time()
    return True, time_end - time_start, number_pn,t,k

n= 900900900900990990990991
print(prime_Miller_Rabin(n))
