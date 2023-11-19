def list_sum_mul(a):
    mul = 1
    for i in a:
        mul *= i
    return sum(a), mul


def check_inclu(a, b):
    if len(a) > len(b):
        c = a
        a = b
        b = c
    for i in a:
        if not i in b:
            return False
    return b

a=[1,2,3,4,5]
b=[1,2,6]
print(check_inclu(a,b))