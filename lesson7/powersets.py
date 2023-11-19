def powersets(s):
    if len(s) == 1:
        for x in s:
            return {(x,)}
    dt = {()}
    for x in s:
        dt = dt.union(powersets(s - {x}))
    dt.add(tuple(s))
    return dt


a = {1, 2, 3}
print(powersets(a))
