def find_min(lst):
    maxx = -1e6
    for i in range(0, len(lst)):
        if lst[i] >= maxx:
            maxx = lst[i]
    for i in range(0, len(lst)):
        if lst[i] == maxx:
            return i


a = [1, 2, 3, 4, 4, 5, 5, 5, 4, 3, 2]
print(find_min(a))
