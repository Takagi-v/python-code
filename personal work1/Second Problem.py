def T(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * T(n // 2) - 1
    return 2 * T((n - 1) // 2) + 1


print(T(3))
