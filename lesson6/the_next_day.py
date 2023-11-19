def check_run(y):
    if y % 4 == 0:
        if y % 400 == 0:
            return True
        if y % 100 == 0:
            return False
        return True


def the_next_day(y, m, d):
    if m == 12 and d == 31:
        return y + 1, 1, 1
    dt = {
        "1": 31,
        "2": 28,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 30,
        "9": 31,
        "10": 30,
        "11": 31,
        "12": 30,
    }
    if check_run(y) and m == 2 and d == 29:
        return y, 3, 1
    if d == dt[m]:
        return y, m + 1, 1
    return y, m, d + 1


y, m, d = 1212, 2, 29
print(the_next_day(y, m, d))
y, m, d = 2009, 12, 31
print(the_next_day(y, m, d))
