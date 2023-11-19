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
