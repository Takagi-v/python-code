def intersection(a, b):
    lst = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                lst.append(i)
                cnt = 1
    return lst if cnt == 1 else False


a = input()
b = input()
a = a[1 : len(a) - 1]
b = b[1 : len(b) - 1]
lst_a = a.split(", ")
lst_b = b.split(", ")
for i in range(len(lst_a)):
    lst_a[i] = int(lst_a[i])
for i in range(len(lst_b)):
    lst_b[i] = int(lst_b[i])
print(intersection(lst_a, lst_b))
if not intersection(lst_a, lst_b):
    print("no intersection")
