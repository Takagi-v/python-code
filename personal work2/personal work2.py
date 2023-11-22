import time
#1. Brute Force

def prime_brute_force():
    time_start = time.time()
    number_pn = 0
    for i in range(2, 1000000 + 1):
        tmp = 1
        for j in range(2, i):
            if i % j == 0:
                tmp = 0
                break
        if tmp:
            prime.append(i)
    number_pn=len(prime)
    time_end = time.time()
    return time_end - time_start, number_pn


prime = []
print(prime_brute_force())

#2. Optimize Brute Force
def prime_optimize_brute_force():
    time_start = time.time()
    number_pn = 0
    for i in range(2, 1000000 + 1):
        tmp = 1
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                tmp = 0
                break
        if tmp:
            prime.append(i)
    number_pn=len(prime)
    time_end = time.time()
    return time_end - time_start, number_pn


prime = []
print(prime_optimize_brute_force())

#3. Optimize Factor
def prime_optimize_factor():
    time_start = time.time()
    number_pn = 0
    k = 1
    while 6 * k + 1 < 10**6:
        x, y = 6 * k + 1, 6 * k - 1
        x1, y1 = 1, 1
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                x1 = 0
                break
        for i in range(2, int(y**0.5)+1):
            if y % i == 0:
                y1 = 0
        if x1:
            prime.append(x)
        if y1:
            prime.append(y)
        k += 1
    number_pn=len(prime)
    time_end = time.time()
    return time_end - time_start, number_pn


prime = [2,3]

print(prime_optimize_factor())

#4. Sieve of Eratosthenes
N = 10**6


def prime_sieve():
    time_start = time.time()
    number_pn = 0
    for i in range(2, int(N**0.5)+1):
        if prime[i] == 0:
            for j in range(i * i, N, i):
                prime[j] = 1
    for i in range(2, N):
        if prime[i] == 0:
            primes.append(i)
    number_pn=len(primes)
    time_end = time.time()
    return time_end - time_start, number_pn


prime = [0] * N
primes = []
print(prime_sieve())

#5. Miller-Rabin
def prime_Miller_Rabin(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    k = 0
    t = n - 1
    while t & 1 == 0:
        k += 1
        t >>= 1
    s = [2, 3]
    for j in s:
        a = j
        b = pow(a, t, n)
        tmp = 0
        if b == 1:
            continue
        for i in range(k):
            if b == n - 1:
                tmp = 1
                break
            else:
                b = (b * b) % n
        if tmp == 1:
            continue
        else:
            return False
    return True


def primes_check():
    time_start = time.time()
    number_pn = 2
    for i in range(5, 10**6):
        if prime_Miller_Rabin(i):
            number_pn += 1
    time_end = time.time()
    return time_end - time_start, number_pn


print(primes_check())