n = int(input())
a = list(range(1, n + 1))
b = []
i = len(a)
num = 1
while i > 1:
    b.clear()
    for j in range(0, len(a)):
        if num % 2 == 0:
            a[j] = 0
        num += 1
    for x in a:
        if x != 0:
            b.append(x)
    a = b.copy()
    i = len(a)
print(a[0])
