def strtolist(s):
    sign = 1
    if s[0] == "-":
        sign = -1
        s = s[1:]
    lst = [int(digit) for digit in s]
    return sign, lst


def listtostr(sign, lst):
    s = "".join(map(str, lst))
    return s if sign == 1 else "-" + s


def add_list(lst1, lst2):
    num1, num2 = lst1[::-1], lst2[::-1]
    num = []
    x = 0
    while len(num1) < len(num2):
        num1.append(0)
    while len(num2) < len(num1):
        num2.append(0)
    for i in range(len(num1)):
        num.append((num1[i] + num2[i] + x) % 10)
        x = (num1[i] + num2[i]) // 10
    if x == 1:
        num.append(1)
    return num[::-1]


def sub_list(lst1, lst2):
    if lst1 == lst2:
        return 1, [0]
    num1 = lst1[::-1]
    num2 = lst2[::-1]
    sign = 1
    if len(num1) < len(num2):
        num1, num2 = num2, num1
        sign = -1
    if len(num1) == len(num2):
        k = len(num1) - 1
        while num1[k] == num2[k]:
            k -= 1
        if num1[k] < num2[k]:
            sign = -1
            num1, num2 = num2, num1
    num = []
    x = 0
    while len(num1) < len(num2):
        num1.append(0)
    while len(num2) < len(num1):
        num2.append(0)
    for i in range(len(num1)):
        dif = num1[i] - num2[i] - x
        if dif < 0:
            x = 1
            dif += 10
        else:
            x = 0
        num.append(dif)
    while len(num) > 1 and num[-1] == 0:
        num.pop()
    return sign, num[::-1]


def sub(str1, str2):
    sign1, lst1 = strtolist(str1)
    sign2, lst2 = strtolist(str2)
    if sign1 == sign2 == -1:
        ans = sub_list(lst2, lst1)
        return listtostr(ans[0], ans[1])
    if sign1 == sign2 == 1:
        ans = sub_list(lst1, lst2)
        return listtostr(ans[0], ans[1])
    else:
        ans = add_list(lst1, lst2)
        return listtostr(1, ans) if sign1 == 1 else listtostr(-1, ans)


print(sub("1232", "12323"))
