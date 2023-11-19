# 	 Pascal三角（中国又名杨辉三角），每一行对应于多项式(a+b)^n的系数。
# def Pascal_triangle(n): # 按照上图输出大小为n的杨辉三角
# (a). 实现def fractal(n): n!
# (b). 数学中n个元素选取k种, choose(n,k)=n!/(k!(n-k)#!)  ，实现def choose(n,k)
# (c). 在此基础上，输出Pascal 三角


def fractal(n):
    ans = 1
    while n != 0:
        ans *= n
        n -= 1
    return ans


def choose(n, k):
    return fractal(n) // (fractal(k) * fractal(n - k))


n = int(input())
for i in range(1, n + 1, 1):
    for j in range(0, i + 1, 1):
        print(choose(i, j), end=" ")
    print()
