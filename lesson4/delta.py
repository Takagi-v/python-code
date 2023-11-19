# 给定的三个数a, b, c，判断ax^2+bx+c 有几个实数根,返回根的数量。
import math


def delta(a, b, c):
    d = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if d > 0:
        return 2, x1, x2
    if d == 0:
        return 1, x1
    if d < 0:
        return 0


x = int(input())
y = int(input())
z = int(input())
print(delta(x, y, z))
