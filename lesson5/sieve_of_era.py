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
for i in range(0, cnt):
    print(primes[i], end=" ")
print(not st[a])
