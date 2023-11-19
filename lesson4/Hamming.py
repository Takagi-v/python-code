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
