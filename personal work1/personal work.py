#1
def Hanoi_plus(n, x, y, z):
    if n == 1:
        print(f"{x}->{y}")
        print(f"{y}->{z}")
        return
    Hanoi_plus(n - 1, x, y, z)
    print(f"{x}->{y}")
    Hanoi_plus(n - 1, z, y, x)
    print(f"{y}->{z}")
    Hanoi_plus(n - 1, x, y, z)


Hanoi_plus(3, "A", "B", "C")

#2(1)
def circle(n):
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
  return a[0]

#2(2)
def T_second(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * T_second(n // 2) - 1
    return 2 * T_second((n - 1) // 2) + 1

#2(3)
def T_third(n):
    i = 1
    while i <= n:
        i *= 2
    i //= 2
    l = n - i
    return 2 * l + 1

#3
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

