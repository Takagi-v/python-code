import time


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
    time_end = time.time()
    return time_end - time_start, number_pn


prime = []
print(prime_brute_force())
