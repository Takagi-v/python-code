import time


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
    time_end = time.time()
    number_pn=len(prime)
    return time_end - time_start, number_pn


prime = [2,3]

print(prime_optimize_factor())
