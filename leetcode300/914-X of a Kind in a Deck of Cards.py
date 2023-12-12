class Solution:
    def hasGroupsSizeX(self, deck):
        from math import gcd
        from collections import Counter
        from functools import reduce

        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2


# 为啥引用要在函数里啊。。。。
'''
from functools import reduce

# 二元操作函数：求两个数的和
def add(x, y):
return x + y

# 要进行操作的可迭代对象
numbers = [1, 2, 3, 4, 5]

# 使用reduce()函数求可迭代对象中所有元素的和
result = reduce(add, numbers)
print("Sum of numbers:", result) # 输出：Sum of numbers: 15
'''