#4.	Given a recursion list of numbers, determine the times of each number. 
def count_numbers(a):
    if len(a) == 0:
        return {}
    dt = {}
    for x in a:
        if type(x) == type(0):
            if x in dt:
                dt[x] += 1
            if x not in dt:
                dt[x] = 1
        if type(x) == type([x]):
            dt1 = count_numbers(x)
            for i in dt1:
                dt[i] += dt1[i]
    return dt


a = [1, 2, 3, 4, 5, 6, [3, 4, 5, 6], [5, 6]]
print(count_numbers(a))
