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
    num1 = lst1[::-1]
    num2 = lst2[::-1]
    if num1 == num2:
        return 1, [0]
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


def mul_list(lst1, lst2):
    num1 = lst1[::-1]
    num2 = lst2[::-1]
    num = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        carry = 0
        for j in range(len(num2)):
            temp = num1[i] * num2[j] + num[i + j] + carry
            num[i + j] = temp % 10
            carry = temp // 10
        num[i + len(num2)] += carry
    while len(num) > 0 and num[-1] == 0:
        num.pop()
    return num[::-1]


def div_list(lst1, lst2):
    num1 = lst1
    num2 = lst2
    quotient = []
    remainder = num1.copy()
    if sub_list(num1[0 : len(num2)], num2)[0] == 1:
        t = len(num1) - len(num2) + 1
    else:
        t = len(num1) - len(num2)
    for i in range(t):
        divisor = num2
        sign, temp = sub_list(remainder, divisor)
        while sign == 1:
            divisor += [0]
            sign, temp = sub_list(remainder, divisor)
        divisor.pop()
        q, l = 0, 0
        sign, flag = sub_list(remainder, mul_list([q], divisor))
        while sign == 1:
            q += 1
            if mul_list([q], divisor) == remainder:
                l = 1
                break
            sign, flag = sub_list(remainder, mul_list([q], divisor))
        if l == 1:
            quotient.append(q)
            remainder = "0"
            break
        temp = mul_list([q - 1], divisor)
        sing, remainder = sub_list(remainder, temp)
        quotient.append(q - 1)
    return quotient, remainder


def pow_list(lst1, n):
    num = [1]
    for i in range(n):
        num = mul_list(num, lst1)
    return num


def add(str1, str2):
    sign1, lst1 = strtolist(str1)
    sign2, lst2 = strtolist(str2)
    if sign1 == sign2:
        ans = add_list(lst1, lst2)
        return listtostr(1, ans) if sign1 == 1 else listtostr(-1, ans)
    if sign1 == -1:
        ans = sub_list(lst2, lst1)
        return listtostr(ans[0], ans[1])
    if sign1 == 1:
        ans = sub_list(lst1, lst2)
        return listtostr(ans[0], ans[1])


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


def mul(str1, str2):
    if str1 == "0" or str2 == "0":
        return "0"
    sign1, lst1 = strtolist(str1)
    sign2, lst2 = strtolist(str2)
    ans = mul_list(lst1, lst2)
    return listtostr(1, ans) if sign1 == sign2 else listtostr(-1, ans)


def div(str1, str2):
    sign1, lst1 = strtolist(str1)
    sign2, lst2 = strtolist(str2)
    if lst2 == [0]:
        return "Oops! It is a wrong caculation."
    if lst1 == [0]:
        return [0], [0]
    sign, ans = sub_list(lst1, lst2)
    if sign == -1:
        return [0], lst1
    quotient, remainder = div_list(lst1, lst2)
    return listtostr(1, quotient), listtostr(1, remainder)


def pow(str1, n):
    sign, lst1 = strtolist(str1)
    ans = pow_list(lst1, n)
    return listtostr(1, ans)
