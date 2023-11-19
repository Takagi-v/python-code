# 	实现定义在自然数上面的函数f(n):f(0)=1,f(1)=1,f(n) = f(f(n//2))+1
def f(n):
    return 1 if n == 0 or n == 1 else f(f(n // 2)) + 1


print(f(0))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
