import time

N = 10**6


def prime_sieve():
    time_start = time.time()
    number_pn = 0
    for i in range(2, int(N**0.5)):
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
