def chess(x, y, x1, y1, a):
    print(x, y, x1, y1, a)
    if a == 0:
        return
    a1 = a - 1
    s = 2**a1
    if x1 < x + s and y1 < y + s:
        print(4)
        m[y + s][x + s - 1] = 4
        m[y + s - 1][x + s] = 4
        m[y + s][x + s] = 4
        print(m)
        chess(x, y, x1, y1, a1)
        chess(x, y + s, x + s - 1, y + s, a1)
        chess(x + s, y, x + s, y + s - 1, a1)
        chess(x + s, y + s, x + s, y + s, a1)
    if x1 < x + s and y1 >= y + s:
        print(2)
        m[y + s - 1][x + s - 1] = 2
        m[y + s][x + s] = 2
        m[y + s - 1][x + s] = 2
        print(m)
        chess(x, y, x + s - 1, y + s - 1, a1)
        chess(x, y + s, x + s - 1, y + s, a1)
        chess(x + s, y, x + s, y + s - 1, a1)
        chess(x + s, y + s, x1, y1, a1)
    if x1 >= x + s and y1 < y + s:
        print(3)
        m[y + s][x + s - 1] = 3
        m[y + s - 1][x + s - 1] = 3
        m[y + s][x + s] = 3
        print(m)
        chess(x, y, x + s - 1, y + s - 1, a1)
        chess(x, y + s, x + s - 1, y + s, a1)
        chess(x + s, y, x1, y1, a1)
        chess(x + s, y + s, x + s, y + s, a1)
    if x1 >= x + s and y1 >= y + s:
        print(1)
        m[y + s][x + s - 1] = 1
        m[y + s - 1][x + s] = 1
        m[y + s - 1][x + s - 1] = 1
        print(m)
        chess(x, y, x + s - 1, y + s - 1, a1)
        chess(x, y + s, x + s - 1, y + s, a1)
        chess(x + s, y, x + s, y + s - 1, a1)
        chess(x + s, y + s, x1, y1, a1)


def GridCover(k, x1, y1):
    chess(0, 0, x1, y1, k)


k = int(input())
x1 = int(input())
y1 = int(input())
m = []
for i in range(0, 2**k):
    m.append([0] * 2**k)
GridCover(k, x1, y1)
print(m)
