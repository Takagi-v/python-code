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