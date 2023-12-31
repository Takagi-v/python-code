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


def listtostr(sign, lst):
    s = "".join(map(str, lst))
    return s if sign == 1 else "-" + s


def div(str1, str2):
    lst1 = [int(digit) for digit in str1]
    lst2 = [int(digit) for digit in str2]
    quotient, remainder = div_list(lst1, lst2)
    return listtostr(1, quotient), listtostr(1, remainder)


a = "8773849905050493"
b = "123"
print(div(a, b))
