def T(n):
    i = 1
    while i <= n:
        i *= 2
    i //= 2
    l = n - i
    return 2 * l + 1


n = 9
print(T(n))
