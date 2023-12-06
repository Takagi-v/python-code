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

def pow_list(lst1,n):
    num=[1]
    for i in range(n):
        num=mul_list(num,lst1)
    return num

def pow1(str1,n):
    sign,lst1=strtolist(str1)
    ans=pow_list(lst1,n)
    return listtostr(1,ans)


