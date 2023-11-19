#3.	Write a Python program of recursion list sum.
def list_sum(lst):
    if len(lst) == 0:
        return 0
    ans = 0
    for x in lst:
        if type(x) == type(0):
            ans += x
        if type(x) == type([]):
            ans += list_sum(x)
    return ans


a = [1, 2, [3, 4], [5, 6]]
print(list_sum(a))
