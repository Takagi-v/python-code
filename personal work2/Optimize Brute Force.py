import time


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
