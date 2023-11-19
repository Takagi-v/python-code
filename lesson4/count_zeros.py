# Given a positive integer n, count how many zeros at its end.
def count_zeros(n):
    cnt = 0
    while n > 0:
        if n % 10 == 0:
            cnt += 1
            n //= 10
        else:
            return cnt


n = int(input())
print(count_zeros(n))
