# 5.	用列表实现如下两个函数:给定一个 正整数，将整数中的数字进行反转；给定一个 负整数，将整数中的数字进行反转。
n = int(input())
lst = []
cnt = 1
if n < 0:
    cnt = 0
    n = abs(n)
while n > 0:
    x = n % 10
    n //= 10
    lst.append(x)
if not cnt:
    print("-", end="")
for i in range(0, len(lst)):
    print(lst[i], end="")
