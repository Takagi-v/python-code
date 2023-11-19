def count_digit(n):
    lst = [0] * 10
    while n > 0:
        x = n % 10
        lst[x] += 1
        n //= 10
    return lst


n = int(input())
a = count_digit(n)
print(a)
