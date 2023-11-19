a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
res = []
[res.append(i) for i in a if i not in res]
print(res)
