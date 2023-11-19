#判断对于一个给定整数n，3n+1猜想成立
def is_valid(n):
    while n != 1:
        if n % 2 == 1:
            n = n * 3 + 1
        if n % 2 == 0:
            while n % 2 == 0:
                n = n // 2
    return True


x = int(input())
print(is_valid(x))
