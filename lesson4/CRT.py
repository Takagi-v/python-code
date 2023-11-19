# China Remainder Theorem (中国剩余定理)今有物不知其数,三三数之剩二,五五数之剩三,七七数之剩二,问物几何?
n = 23
while n < 100000:
    if n % 3 == 2 and n % 5 == 3 and n % 7 == 2:
        print(n, end=" ")
    n += 105
