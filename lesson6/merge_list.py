def merge_list(a, b):
    c = a + b
    c.sort()
    return c


a = [1, 2, 3]
b = [-1, 2, 4]
print(merge_list(a, b))
