# 判断给定的三个数a, b, c能不能构成一个三角形,直接输出True 和 False即可。
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


x = int(input())
y = int(input())
z = int(input())
print(is_triangle(x, y, z))

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

# 给定一个自然数n, 判断n是不是质数
# n=int(input())
# cnt=0
# prime=[0]
# def ge_prime(n):
#  vis=[0]*100
#  for i in range(2,n+1):
#    if vis[i]!=0:
#      prime.append(i)
#      cnt+=1
#    for j in range(0,int(cnt)) and i*prime[j]<=n:
#      vis[i*prime[j]]=True
#      if i%prime[j]==0:
#        break
# ge_prime(n)
# for i in range(0,cnt):
#  print(prime[i])
import math

n = int(input())
a = math.sqrt(n)


def is_prime(x):
    i = 1
    while i < a:
        i += 1
        if n % i <= 1e-6:
            return False
    return True


print(is_prime(n))

# 判断一个年份是不是回文年，譬如 2002， 1991， 1221都是回文
def is_palindrome_year(year):
    if year < 10:
        return True
    if year < 100:
        a = year % 10
        year //= 10
        b = year
        if a == b:
            return True
        return False
    if year < 1000:
        a = year % 10
        year //= 10
        year //= 10
        c = year
        if a == c:
            return True
        else:
            return False
    a = year % 10
    year //= 10
    b = year % 10
    year //= 10
    c = year % 10
    year //= 10
    d = year
    if a == d and b == c:
        return True
    else:
        return False


n = int(input())
print(is_palindrome_year(n))

#实现函数
import math
def f(x):
  if x < -2:
    return x**4
  if x >= -2 and x < 2:
    return math.sin(x)
  if x > 2:
    return math.e**x
n=float(input())
print(f(n))

# 	Write a program to read a series of numbers from the console, such that if the input number x:
def f():
    x = int(input())
    while x != 0:
        if x == -1:
            x = int(input())
            continue
        while x != 0:
            print(x % 10, end="")
            x //= 10
        x = int(input())
    return


f()



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

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different
def Hamming(a, b):
    c = a ^ b
    cnt = 0
    while c != 0:
        if c % 2 == 1:
            cnt += 1
        c >>= 1
    return cnt


x = int(input())
y = int(input())
print(Hamming(x, y))

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

# China Remainder Theorem (中国剩余定理)今有物不知其数,三三数之剩二,五五数之剩三,七七数之剩二,问物几何?
n = 23
while n < 100000:
    if n % 3 == 2 and n % 5 == 3 and n % 7 == 2:
        print(n, end=" ")
    n += 105

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
