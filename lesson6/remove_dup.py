def remove_dup(a):
    b = set(a)
    c = list(sorted(b))
    c.reverse()
    return c


a = [3, 2, 1, 4, 2, 3, 5]
print(remove_dup(a))
